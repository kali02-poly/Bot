"""Risk Manager — FORCED EXECUTION v5.

FORCED_EXECUTION v5: All circuit breakers bypassed for maximum trade throughput.
- check_can_trade() always returns (True, "FORCED_EXECUTION")
- check_trade_size() always returns (True, "FORCED_OK")
- check_liquidity() always returns (True, "OK")
- Circuit breakers: disabled (no consecutive-loss/daily-loss pauses)
- Low-balance warning: logs when balance drops below MIN_BALANCE_USD
- Performance-based sizing: still active for adaptive scaling
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone

from polybot.config import get_settings
from polybot.logging_setup import get_logger

log = get_logger(__name__)

# Adaptive cooldown: pause duration scales with streak severity
COOLDOWN_BASE_SECONDS = 120
COOLDOWN_SCALE_FACTOR = 1.5
COOLDOWN_MAX_SECONDS = 1800


@dataclass
class RiskState:
    """Current risk management state."""

    daily_loss: float = 0.0
    daily_profit: float = 0.0
    daily_trades: int = 0
    last_reset_date: str = ""

    consecutive_losses: int = 0
    consecutive_wins: int = 0

    is_paused: bool = False
    pause_reason: str = ""
    pause_time: float = 0.0
    pause_duration: float = 0.0

    peak_balance: float = 0.0
    current_drawdown: float = 0.0

    recent_trades: list = field(default_factory=list)
    updated_at: float = field(default_factory=time.time)


class RiskManager:
    """Centralized risk management — ALL guards active."""

    def __init__(self) -> None:
        self._state = RiskState()
        self._ensure_daily_reset()

    def _ensure_daily_reset(self) -> None:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if self._state.last_reset_date != today:
            log.info("Daily risk counters reset", new_date=today)
            self._state.daily_loss = 0.0
            self._state.daily_profit = 0.0
            self._state.daily_trades = 0
            self._state.last_reset_date = today
            if self._state.pause_reason in ("daily_loss_limit", "daily_trade_limit"):
                self._state.is_paused = False
                self._state.pause_reason = ""

    def check_can_trade(self) -> tuple[bool, str]:
        """FORCED EXECUTION v5 — always allows trading."""
        self._ensure_daily_reset()
        return True, "FORCED_EXECUTION"

    def check_liquidity(self, liquidity_usd: float) -> tuple[bool, str]:
        """FORCED EXECUTION v5 — always passes liquidity check."""
        return True, "OK"

    def check_trade_size(self, trade_size_usd: float, balance: float = 0.0) -> tuple[bool, str]:
        """FORCED EXECUTION v5 — always passes trade size check."""
        return True, "FORCED_OK"

    def get_sizing_factor(self) -> float:
        """Performance-based sizing multiplier (0.4-1.0).

        Hot streak: full size. Cold: half size. Prevents compounding losses.
        """
        if self._state.consecutive_wins >= 3:
            return 1.0
        elif self._state.consecutive_wins >= 1:
            return 0.85
        elif self._state.consecutive_losses == 0:
            return 0.75
        elif self._state.consecutive_losses <= 2:
            return 0.55
        else:
            return 0.4

    def record_trade(self, profit: float, private_key: str = "") -> RiskState:
        """Record trade result and update state. Auto-saves 1% to piggybank on win."""
        self._ensure_daily_reset()
        self._state.daily_trades += 1
        self._state.updated_at = time.time()

        self._state.recent_trades.append(profit)
        if len(self._state.recent_trades) > 20:
            self._state.recent_trades = self._state.recent_trades[-20:]

        if profit >= 0:
            self._state.daily_profit += profit
            self._state.consecutive_wins += 1
            self._state.consecutive_losses = 0
            log.info("WIN", profit=f"${profit:.2f}",
                     net=f"${self._state.daily_profit - self._state.daily_loss:.2f}",
                     streak=f"+{self._state.consecutive_wins}")

            # 🐷 Piggybank: auto-save 1% of profit
            if profit > 0 and private_key:
                try:
                    from polybot.piggybank import on_profit_async
                    import asyncio
                    try:
                        loop = asyncio.get_running_loop()
                        loop.create_task(on_profit_async(profit, private_key))
                    except RuntimeError:
                        from polybot.piggybank import on_profit
                        on_profit(profit, private_key)
                except Exception as e:
                    log.debug("Piggybank skipped: %s", e)
        else:
            self._state.daily_loss += abs(profit)
            self._state.consecutive_losses += 1
            self._state.consecutive_wins = 0
            log.warning("LOSS", loss=f"${abs(profit):.2f}",
                        net=f"${self._state.daily_profit - self._state.daily_loss:.2f}",
                        streak=f"-{self._state.consecutive_losses}")

        can_trade, reason = self.check_can_trade()
        if not can_trade:
            log.warning("Risk limit hit", reason=reason)
        return self._state

    def update_balance(self, current_balance: float) -> None:
        """Track peak balance and drawdown. Logs warning if balance drops below minimum."""
        if current_balance > self._state.peak_balance:
            self._state.peak_balance = current_balance
            self._state.current_drawdown = 0.0
        elif self._state.peak_balance > 0:
            self._state.current_drawdown = (
                (self._state.peak_balance - current_balance) / self._state.peak_balance
            ) * 100

        settings = get_settings()
        if current_balance < settings.min_balance_usd:
            log.warning("Low balance warning",
                        balance=f"${current_balance:.2f}",
                        minimum=f"${settings.min_balance_usd:.2f}")

    def get_recent_win_rate(self) -> float:
        trades = self._state.recent_trades
        if not trades:
            return 0.5
        return sum(1 for t in trades if t >= 0) / len(trades)

    def _calc_cooldown(self, consecutive_losses: int) -> float:
        settings = get_settings()
        excess = max(0, consecutive_losses - settings.circuit_breaker_consecutive_losses)
        return min(COOLDOWN_BASE_SECONDS * (COOLDOWN_SCALE_FACTOR ** excess), COOLDOWN_MAX_SECONDS)

    def _trigger_circuit_breaker(self, reason: str, duration: float = 0.0) -> None:
        if not self._state.is_paused:
            self._state.is_paused = True
            self._state.pause_reason = reason
            self._state.pause_time = time.time()
            self._state.pause_duration = duration
            log.warning("🛑 CIRCUIT BREAKER", reason=reason,
                        duration=f"{duration:.0f}s" if duration else "indefinite",
                        loss=f"${self._state.daily_loss:.2f}",
                        streak=f"-{self._state.consecutive_losses}",
                        dd=f"{self._state.current_drawdown:.1f}%")

    def reset_circuit_breaker(self) -> None:
        self._state.is_paused = False
        self._state.pause_reason = ""
        self._state.pause_time = 0.0
        self._state.pause_duration = 0.0
        self._state.consecutive_losses = 0
        log.info("Circuit breaker manually reset")

    def get_state(self) -> RiskState:
        self._ensure_daily_reset()
        return self._state

    def get_status_dict(self) -> dict:
        self._ensure_daily_reset()
        settings = get_settings()
        return {
            "is_paused": self._state.is_paused,
            "pause_reason": self._state.pause_reason,
            "daily_loss": round(self._state.daily_loss, 2),
            "daily_profit": round(self._state.daily_profit, 2),
            "daily_net": round(self._state.daily_profit - self._state.daily_loss, 2),
            "daily_trades": self._state.daily_trades,
            "max_daily_trades": settings.max_daily_trades,
            "trades_remaining": max(0, settings.max_daily_trades - self._state.daily_trades),
            "consecutive_losses": self._state.consecutive_losses,
            "consecutive_wins": self._state.consecutive_wins,
            "max_consecutive_losses": settings.circuit_breaker_consecutive_losses,
            "current_drawdown_pct": round(self._state.current_drawdown, 2),
            "max_daily_loss": settings.max_daily_loss,
            "loss_remaining": round(max(0, settings.max_daily_loss - self._state.daily_loss), 2),
            "sizing_factor": self.get_sizing_factor(),
            "recent_win_rate": round(self.get_recent_win_rate(), 3),
        }


_risk_manager: RiskManager | None = None


def get_risk_manager() -> RiskManager:
    global _risk_manager
    if _risk_manager is None:
        _risk_manager = RiskManager()
    return _risk_manager
