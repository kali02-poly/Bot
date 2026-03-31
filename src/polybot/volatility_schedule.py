"""Volatility Schedule — Time-aware trading intensity.

Knows the recurring high-volatility windows in crypto markets and adjusts
the bot's aggressiveness accordingly. During hot windows, the bot sizes up
and lowers its confidence threshold. During quiet hours, it's conservative
or can skip entirely.

Activate: VOLATILITY_SCHEDULE=true in Railway.

Modes (set via VOLATILITY_MODE):
  "aggressive"  — Only trade during high-vol windows, 1.5x sizing
  "adaptive"    — Trade always, but scale sizing by volatility regime (default)
  "passive"     — Trade always, ignore schedule (same as off)
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone, timedelta
from dataclasses import dataclass
from typing import Optional

from polybot.logging_setup import get_logger

log = get_logger(__name__)

# ── Recurring high-volatility windows (all times UTC) ────────────

@dataclass(frozen=True)
class VolWindow:
    """A recurring volatility window."""
    name: str
    hour_start: int    # UTC hour (0-23)
    minute_start: int  # UTC minute
    duration_min: int  # Duration in minutes
    intensity: float   # 1.0 = normal, 1.5 = hot, 2.0 = extreme
    days: tuple = (0, 1, 2, 3, 4, 5, 6)  # 0=Monday, 6=Sunday

# Weekday-only windows (Mon-Fri)
WEEKDAYS = (0, 1, 2, 3, 4)

VOLATILITY_WINDOWS: list[VolWindow] = [
    # ── US Market Open: 14:30 UTC (9:30 ET) — biggest daily spike ──
    VolWindow("US_OPEN", 14, 20, 40, 1.8, WEEKDAYS),

    # ── US Market Close: 20:50-21:10 UTC (16:00 ET) ──
    VolWindow("US_CLOSE", 20, 50, 20, 1.4, WEEKDAYS),

    # ── London Open: 08:00 UTC ──
    VolWindow("LONDON_OPEN", 7, 50, 30, 1.3, WEEKDAYS),

    # ── Asia Open: Tokyo+HK 00:00-01:00 UTC ──
    VolWindow("ASIA_OPEN", 0, 0, 60, 1.2, (0, 1, 2, 3, 4, 5, 6)),

    # ── Funding Rate Resets: 00:00, 08:00, 16:00 UTC ──
    # Liquidation cascades cluster around these
    VolWindow("FUNDING_00", 23, 55, 15, 1.3, (0, 1, 2, 3, 4, 5, 6)),
    VolWindow("FUNDING_08", 7, 55, 15, 1.3, (0, 1, 2, 3, 4, 5, 6)),
    VolWindow("FUNDING_16", 15, 55, 15, 1.3, (0, 1, 2, 3, 4, 5, 6)),

    # ── CPI / Jobs Data: 13:30 UTC (8:30 ET) — monthly, but we check daily ──
    # On non-release days this just makes the bot slightly more attentive
    VolWindow("MACRO_DATA", 13, 25, 20, 1.5, WEEKDAYS),

    # ── Sunday CME Gap: 22:00-00:00 UTC ──
    VolWindow("CME_GAP", 22, 0, 120, 1.4, (6,)),  # Sunday only
]

# ── Quiet hours: reduce sizing or skip entirely ──
# These are the dead zones where spreads widen and liquidity thins
QUIET_HOURS_UTC = [
    (3, 6),   # 03:00-06:00 UTC — global dead zone
    (11, 13), # 11:00-13:00 UTC — gap between Asia close and EU macro
]


@dataclass
class VolatilityState:
    """Current volatility regime assessment."""
    is_hot: bool = False
    is_quiet: bool = False
    active_window: str = ""
    intensity: float = 1.0          # Sizing multiplier
    confidence_offset: float = 0.0  # Added to/subtracted from min confidence
    skip_trade: bool = False        # In aggressive mode: skip during quiet


def get_current_regime(now: Optional[datetime] = None) -> VolatilityState:
    """Assess current volatility regime based on time.

    Returns VolatilityState with intensity multiplier and confidence adjustments.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    weekday = now.weekday()  # 0=Monday
    hour = now.hour
    minute = now.minute
    now_minutes = hour * 60 + minute

    state = VolatilityState()

    # Check if we're in a hot window
    for w in VOLATILITY_WINDOWS:
        if weekday not in w.days:
            continue
        window_start = w.hour_start * 60 + w.minute_start
        window_end = window_start + w.duration_min

        # Handle midnight-crossing windows
        if window_end > 1440:
            in_window = now_minutes >= window_start or now_minutes < (window_end - 1440)
        else:
            in_window = window_start <= now_minutes < window_end

        if in_window:
            # Take the highest intensity if multiple windows overlap
            if w.intensity > state.intensity:
                state.is_hot = True
                state.active_window = w.name
                state.intensity = w.intensity
                # Hot windows: lower confidence threshold (more trades)
                state.confidence_offset = -0.05 * (w.intensity - 1.0)

    # Check if we're in quiet hours
    if not state.is_hot:
        for q_start, q_end in QUIET_HOURS_UTC:
            if q_start <= hour < q_end:
                state.is_quiet = True
                state.active_window = "QUIET"
                state.intensity = 0.6  # 60% sizing
                state.confidence_offset = 0.05  # Require higher confidence
                break

    return state


def get_sizing_multiplier() -> float:
    """Get the current volatility-based sizing multiplier (0.6-1.8)."""
    return get_current_regime().intensity


def get_confidence_adjustment() -> float:
    """Get confidence threshold adjustment (-0.05 to +0.05)."""
    return get_current_regime().confidence_offset


def should_skip_trade() -> bool:
    """In aggressive mode: should we skip this window entirely?"""
    mode = os.getenv("VOLATILITY_MODE", "adaptive").lower()
    if mode != "aggressive":
        return False
    regime = get_current_regime()
    return regime.is_quiet


def is_volatility_schedule_enabled() -> bool:
    """Check if volatility schedule is active."""
    return os.getenv("VOLATILITY_SCHEDULE", "").lower() in ("true", "1", "yes")


def get_schedule_status() -> dict:
    """Status dict for logging/API."""
    regime = get_current_regime()
    return {
        "enabled": is_volatility_schedule_enabled(),
        "mode": os.getenv("VOLATILITY_MODE", "adaptive"),
        "is_hot": regime.is_hot,
        "is_quiet": regime.is_quiet,
        "window": regime.active_window,
        "intensity": regime.intensity,
        "confidence_offset": regime.confidence_offset,
    }
