"""Lightweight FastAPI dashboard — status, active trades, PnL.

No scanner widget (reduces load). Green status bar when healthy.
Shows active positions, recent trades, daily/total PnL, risk state.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from polybot.config import get_settings
from polybot.database import init_db, get_db


def _get_risk_state() -> dict[str, Any]:
    """Get risk state from database."""
    try:
        with get_db() as conn:
            row = conn.execute("SELECT * FROM risk_state ORDER BY rowid DESC LIMIT 1").fetchone()
            if row:
                return dict(row)
        return {"is_paused": 0, "daily_loss": 0, "consecutive_losses": 0}
    except Exception:
        return {"is_paused": 0, "daily_loss": 0, "consecutive_losses": 0}


def _get_today_pnl() -> dict[str, Any]:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    with get_db() as conn:
        row = conn.execute("SELECT * FROM daily_pnl WHERE date = ?", (today,)).fetchone()
        if row:
            d = dict(row)
            total = d.get("total_trades", 0)
            d["winrate"] = (d.get("winning_trades", 0) / total * 100) if total > 0 else 0
            return d
    return {"realized": 0, "unrealized": 0, "total_trades": 0, "winning_trades": 0, "losing_trades": 0, "winrate": 0}


def _get_total_pnl() -> dict[str, Any]:
    with get_db() as conn:
        row = conn.execute("""SELECT
            COALESCE(SUM(realized), 0) as total_realized,
            COALESCE(SUM(unrealized), 0) as total_unrealized,
            COALESCE(SUM(total_trades), 0) as total_trades,
            COALESCE(SUM(winning_trades), 0) as winning_trades,
            COALESCE(SUM(losing_trades), 0) as losing_trades
        FROM daily_pnl""").fetchone()
        if row:
            d = dict(row)
            total = d.get("total_trades", 0)
            d["overall_winrate"] = (d.get("winning_trades", 0) / total * 100) if total > 0 else 0
            return d
    return {"total_realized": 0, "total_unrealized": 0, "total_trades": 0, "overall_winrate": 0}


def _get_bot_status() -> dict[str, Any]:
    """Overall bot health status."""
    settings = get_settings()
    risk = _get_risk_state()
    from polybot.sniper import is_sniper_mode

    return {
        "healthy": not risk.get("is_paused", False),
        "mode": "SNIPER" if (is_sniper_mode() or settings.mode == "sniper") else settings.mode.upper(),
        "dry_run": settings.dry_run,
        "model": settings.model if hasattr(settings, "model") else "N/A",
        "paused": risk.get("is_paused", False),
        "pause_reason": risk.get("pause_reason", ""),
    }


DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>PolyBot Dashboard</title>
<meta http-equiv="refresh" content="15">
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#0d1117;color:#c9d1d9;padding:16px}
.status-bar{padding:12px 20px;border-radius:8px;font-weight:600;font-size:18px;margin-bottom:16px;display:flex;align-items:center;gap:10px}
.status-ok{background:#0d3d1f;border:1px solid #238636;color:#3fb950}
.status-warn{background:#3d2d00;border:1px solid #d29922;color:#e3b341}
.status-bad{background:#3d0d0d;border:1px solid #da3633;color:#f85149}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px;margin-bottom:16px}
.card{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:16px}
.card h3{color:#58a6ff;margin-bottom:12px;font-size:14px;text-transform:uppercase;letter-spacing:0.5px}
.stat{display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #21262d}
.stat:last-child{border-bottom:none}
.stat .label{color:#8b949e;font-size:13px}
.stat .value{font-weight:600;font-size:14px}
.positive{color:#3fb950}.negative{color:#f85149}.neutral{color:#c9d1d9}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;padding:8px;color:#58a6ff;border-bottom:2px solid #30363d;font-size:12px;text-transform:uppercase}
td{padding:6px 8px;border-bottom:1px solid #21262d}
tr:hover{background:#1c2128}
.badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:11px;font-weight:600}
.badge-win{background:#0d3d1f;color:#3fb950}
.badge-loss{background:#3d0d0d;color:#f85149}
.badge-open{background:#0d2d3d;color:#58a6ff}
.footer{margin-top:16px;text-align:center;color:#484f58;font-size:12px}
</style>
</head>
<body>

<!-- Status Bar -->
<div class="status-bar {{ 'status-ok' if status.healthy else ('status-warn' if status.paused else 'status-bad') }}">
    <span>{{ '🟢' if status.healthy else '🟡' if status.paused else '🔴' }}</span>
    <span>{{ status.mode }}{% if status.dry_run %} (DRY RUN){% endif %}</span>
    {% if status.paused %}<span style="margin-left:auto;font-size:14px">⚠️ {{ status.pause_reason }}</span>{% endif %}
    {% if not status.paused %}<span style="margin-left:auto;font-size:14px">All systems operational</span>{% endif %}
</div>

<!-- Stats Grid -->
<div class="grid">
    <!-- Today PnL -->
    <div class="card">
        <h3>📊 Today</h3>
        <div class="stat"><span class="label">Realized P&L</span><span class="value {{ 'positive' if pnl.realized >= 0 else 'negative' }}">${{ "%.2f"|format(pnl.realized) }}</span></div>
        <div class="stat"><span class="label">Trades</span><span class="value">{{ pnl.total_trades }} ({{ "%.0f"|format(pnl.winrate) }}% WR)</span></div>
        <div class="stat"><span class="label">W / L</span><span class="value"><span class="positive">{{ pnl.winning_trades }}</span> / <span class="negative">{{ pnl.losing_trades }}</span></span></div>
    </div>

    <!-- Total PnL -->
    <div class="card">
        <h3>💰 All Time</h3>
        <div class="stat"><span class="label">Total P&L</span><span class="value {{ 'positive' if total.total_realized >= 0 else 'negative' }}">${{ "%.2f"|format(total.total_realized) }}</span></div>
        <div class="stat"><span class="label">Total Trades</span><span class="value">{{ total.total_trades }}</span></div>
        <div class="stat"><span class="label">Win Rate</span><span class="value">{{ "%.1f"|format(total.overall_winrate) }}%</span></div>
    </div>

    <!-- Risk State -->
    <div class="card">
        <h3>🛡️ Risk</h3>
        <div class="stat"><span class="label">Daily Loss</span><span class="value negative">${{ "%.2f"|format(risk.daily_loss) }} / ${{ "%.2f"|format(risk.max_daily_loss) }}</span></div>
        <div class="stat"><span class="label">Streak</span><span class="value">
            {% if risk.consecutive_wins > 0 %}<span class="positive">+{{ risk.consecutive_wins }}W</span>
            {% elif risk.consecutive_losses > 0 %}<span class="negative">-{{ risk.consecutive_losses }}L</span>
            {% else %}<span class="neutral">0</span>{% endif %}
        </span></div>
        <div class="stat"><span class="label">Drawdown</span><span class="value">{{ "%.1f"|format(risk.current_drawdown_pct) }}%</span></div>
        <div class="stat"><span class="label">Sizing Factor</span><span class="value">{{ "%.0f"|format(risk.get('sizing_factor', 1.0) * 100) }}%</span></div>
        <div class="stat"><span class="label">Trades Left</span><span class="value">{{ risk.trades_remaining }}</span></div>
    </div>
</div>

<!-- Active Positions -->
<div class="card" style="margin-bottom:12px">
    <h3>📈 Active Positions ({{ positions|length }})</h3>
    {% if positions %}
    <table>
        <tr><th>Market</th><th>Side</th><th>Size</th><th>Entry</th><th>Current</th><th>P&L</th></tr>
        {% for p in positions %}
        <tr>
            <td>{{ p.market_name[:40] if p.market_name else p.market_id[:20] }}</td>
            <td><span class="badge badge-open">{{ p.side }}</span></td>
            <td>${{ "%.2f"|format(p.size_usd) if p.size_usd else '?' }}</td>
            <td>{{ "%.3f"|format(p.entry_price) if p.entry_price else '?' }}</td>
            <td>{{ "%.3f"|format(p.current_price) if p.current_price else '?' }}</td>
            <td class="{{ 'positive' if (p.unrealized_pnl or 0) >= 0 else 'negative' }}">
                ${{ "%.2f"|format(p.unrealized_pnl) if p.unrealized_pnl else '0.00' }}
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p style="color:#484f58;padding:8px 0">No active positions</p>
    {% endif %}
</div>

<!-- Recent Trades -->
<div class="card">
    <h3>📋 Recent Trades</h3>
    {% if trades %}
    <table>
        <tr><th>Time</th><th>Market</th><th>Side</th><th>Amount</th><th>Result</th></tr>
        {% for t in trades %}
        <tr>
            <td style="white-space:nowrap">{{ t.created_at[:16] if t.created_at else '?' }}</td>
            <td>{{ (t.market_name or t.slug or '')[:35] }}</td>
            <td>{{ t.outcome or t.side or '?' }}</td>
            <td>${{ "%.2f"|format(t.amount) if t.amount else '?' }}</td>
            <td>
                {% if t.profit is not none %}
                <span class="badge {{ 'badge-win' if t.profit >= 0 else 'badge-loss' }}">
                    ${{ "%.2f"|format(t.profit) }}
                </span>
                {% else %}
                <span class="badge badge-open">pending</span>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p style="color:#484f58;padding:8px 0">No trades yet</p>
    {% endif %}
</div>

<div class="footer">PolyBot Dashboard — auto-refreshes every 15s</div>
</body>
</html>"""


def run_dashboard():
    """Start the FastAPI dashboard."""
    import uvicorn
    from fastapi import FastAPI, Request
    from fastapi.responses import HTMLResponse
    from starlette.middleware.cors import CORSMiddleware
    from jinja2 import Environment, BaseLoader

    settings = get_settings()
    init_db()

    app = FastAPI(title="PolyBot Dashboard", version="2.0")
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True,
        allow_methods=["*"], allow_headers=["*"],
    )

    jinja_env = Environment(loader=BaseLoader(), autoescape=True)
    template = jinja_env.from_string(DASHBOARD_HTML)

    @app.get("/", response_class=HTMLResponse)
    async def index():
        with get_db() as conn:
            trades_rows = conn.execute("SELECT * FROM trades ORDER BY id DESC LIMIT 20").fetchall()
            positions_rows = conn.execute("SELECT * FROM positions WHERE status = 'OPEN' ORDER BY id DESC LIMIT 10").fetchall()

        trades = [dict(t) for t in trades_rows]
        positions = [dict(p) for p in positions_rows]

        return template.render(
            status=_get_bot_status(),
            risk=_get_risk_state(),
            pnl=_get_today_pnl(),
            total=_get_total_pnl(),
            trades=trades,
            positions=positions,
        )

    # ── JSON API endpoints ──
    @app.get("/api/status")
    async def api_status():
        return {
            "status": _get_bot_status(),
            "risk": _get_risk_state(),
            "pnl_today": _get_today_pnl(),
            "pnl_total": _get_total_pnl(),
        }

    @app.get("/api/trades")
    async def api_trades():
        with get_db() as conn:
            rows = conn.execute("SELECT * FROM trades ORDER BY id DESC LIMIT 100").fetchall()
        return [dict(r) for r in rows]

    @app.get("/api/positions")
    async def api_positions():
        with get_db() as conn:
            rows = conn.execute("SELECT * FROM positions WHERE status = 'OPEN' ORDER BY id DESC").fetchall()
        return [dict(r) for r in rows]

    @app.get("/api/pnl")
    async def api_pnl():
        with get_db() as conn:
            rows = conn.execute("SELECT * FROM daily_pnl ORDER BY date DESC LIMIT 30").fetchall()
        data = []
        for r in rows:
            d = dict(r)
            total = d.get("total_trades", 0)
            d["winrate"] = (d.get("winning_trades", 0) / total * 100) if total > 0 else 0
            data.append(d)
        return data

    @app.get("/health")
    async def health():
        return {"status": "ok", "mode": settings.mode}

    port = int(settings.port if hasattr(settings, "port") else 8000)
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
