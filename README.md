# 🤖 PolyBot — Automated Polymarket Trading Bot

> **Version 2.0.0** · **Python 3.11+** · **License: MIT**

PolyBot is an automated trading bot that trades on [Polymarket](https://polymarket.com), a prediction market platform built on the Polygon blockchain. It focuses on **5-minute Up/Down crypto markets** (BTC, ETH, SOL), scanning for profitable opportunities and placing real trades with your money.

---

## ⚠️ IMPORTANT WARNING — READ THIS FIRST

- **This bot trades REAL money** when `DRY_RUN=false`. You can lose your funds.
- **Never share or commit your private key.** Anyone with your private key can steal all your crypto.
- **Start with `DRY_RUN=true`** to test without risking real money.
- **This is not financial advice.** Use at your own risk.

---

## 📑 Table of Contents

1. [What Does This Bot Do?](#-what-does-this-bot-do)
2. [How It Works (Simple Explanation)](#-how-it-works-simple-explanation)
3. [Prerequisites — What You Need Before Starting](#-prerequisites--what-you-need-before-starting)
4. [Quick Start — Deploy to Railway (Easiest)](#-quick-start--deploy-to-railway-easiest)
5. [Local Development Setup (For Developers)](#-local-development-setup-for-developers)
6. [Docker Setup](#-docker-setup)
7. [Environment Variables — Complete Reference](#-environment-variables--complete-reference)
8. [Trading Modes](#-trading-modes)
9. [Full Redeemer V89 — Automatic Winnings Collection](#-full-redeemer-v89--automatic-winnings-collection)
10. [API Endpoints — Complete Reference](#-api-endpoints--complete-reference)
11. [CLI Commands](#-cli-commands)
12. [Dashboard & Monitoring](#-dashboard--monitoring)
13. [Backtesting — Test Strategies on Historical Data](#-backtesting--test-strategies-on-historical-data)
14. [Hyperparameter Optimization](#-hyperparameter-optimization)
15. [Architecture Overview](#-architecture-overview)
16. [Project Structure](#-project-structure)
17. [Running Tests](#-running-tests)
18. [CI/CD Pipeline](#-cicd-pipeline)
19. [Migration to a Fresh Repository](#-migration-to-a-fresh-repository)
20. [Troubleshooting & FAQ](#-troubleshooting--faq)
21. [Security Best Practices](#-security-best-practices)
22. [Contributing](#-contributing)
23. [License](#-license)

---

## 🧠 What Does This Bot Do?

In plain English:

1. **Polymarket** is a website where you bet on real-world outcomes (like "Will BTC go up in 5 minutes?"). You buy **YES** or **NO** shares. If you are right, you get paid. If you are wrong, you lose your money.

2. **PolyBot** is a program that **automatically** places these bets for you. It:
   - Scans ~2,395 markets every 12 seconds looking for opportunities
   - Filters down to ~15–30 markets that match its criteria (5-minute crypto Up/Down markets for BTC, ETH, SOL)
   - Calculates if a trade has a mathematical edge (an expected profit)
   - Decides how much money to bet using the Kelly Criterion (a formula that optimizes bet sizing)
   - Places the trade on-chain (on the Polygon blockchain) through Polymarket's API
   - Tracks your profit and loss (P&L) in real time
   - Automatically cashes out (redeems) winning positions

3. **You need:**
   - A Polygon wallet with USDC (a stablecoin worth $1 each)
   - A place to run the bot 24/7 (Railway.app is recommended)
   - An Alchemy API key (free tier works, makes the bot faster)

---

## 🔄 How It Works (Simple Explanation)

Here is the step-by-step process the bot follows every 12 seconds:

```
Step 1: SCAN          → Look at all Polymarket markets
Step 2: FILTER        → Keep only 5-min Up/Down markets for BTC, ETH, SOL
Step 3: CALCULATE     → Determine if there's a mathematical edge (profit potential)
Step 4: CHECK         → Is the edge bigger than our minimum threshold (1.5% by default)?
Step 5: SIZE          → Decide how much money to bet (Half-Kelly formula, max $50)
Step 6: EXECUTE       → Place the trade on the blockchain
Step 7: TRACK         → Record the trade and update P&L
Step 8: REDEEM        → Cash out winning positions automatically
Step 9: REPEAT        → Wait 12 seconds, then do it all again
```

**Key Concepts Explained:**
- **Edge**: The mathematical advantage the bot calculates. If a market is mispriced, there is an edge.
- **Expected Value (EV)**: How much profit you expect on average. The bot only trades when EV > 1.5%.
- **Kelly Criterion**: A formula that tells you the optimal bet size. Half-Kelly (0.5) is used by default because it is safer.
- **USDC**: A stablecoin on the Polygon blockchain. 1 USDC = $1 USD. This is what the bot uses to trade.
- **CLOB**: Central Limit Order Book — Polymarket's order matching system.
- **RPC**: Remote Procedure Call — how the bot communicates with the Polygon blockchain.

---

## 📋 Prerequisites — What You Need Before Starting

Before you do anything, make sure you have the following:

### 1. A Polygon Wallet

You need a crypto wallet that works on the **Polygon network**. The wallet must have:
- **USDC tokens** (this is what the bot trades with)
- **A small amount of MATIC/POL** for transaction fees (gas)

**How to get a wallet:**
- Use [MetaMask](https://metamask.io/) (browser extension)
- Add the Polygon network to MetaMask
- Send USDC to your Polygon wallet address

**You will need two things from your wallet:**
- `POLYGON_PRIVATE_KEY` — Your wallet's private key (a long hex string starting with `0x`)
- `WALLET_ADDRESS` — Your wallet's public address (also starts with `0x`)

> ⚠️ **NEVER share your private key with anyone. NEVER put it in your code. NEVER commit it to Git.**

### 2. An Alchemy API Key (Recommended, Free)

Alchemy gives you fast access to the Polygon blockchain.

1. Go to [alchemy.com](https://www.alchemy.com/)
2. Create a free account
3. Create a new app → Select **Polygon Mainnet**
4. Copy your API key

Without Alchemy, the bot will use slower public RPCs (it will still work, just slower).

### 3. A Place to Run the Bot

The bot needs to run 24/7. You have three options:

| Option | Difficulty | Cost | Best For |
|--------|-----------|------|----------|
| **Railway.app** (recommended) | Easy | ~$5/month | Most users |
| **Docker** on your own server | Medium | Varies | Self-hosters |
| **Local machine** | Easy | Free (electricity) | Testing only |

### 4. Software Requirements (for local development only)

If you want to run the bot on your own computer:
- **Python 3.11 or newer** — [Download here](https://www.python.org/downloads/)
- **Git** — [Download here](https://git-scm.com/downloads)
- **pip** — Comes with Python

---

## 🚀 Quick Start — Deploy to Railway (Easiest)

This is the fastest way to get the bot running. No coding required.

### Step 1: Fork the Repository

1. Go to the GitHub repository page
2. Click the **"Fork"** button in the top-right corner
3. This creates a copy of the code in your own GitHub account

### Step 2: Create a Railway Account

1. Go to [railway.app](https://railway.app/)
2. Sign up with your GitHub account
3. Click **"New Project"**
4. Select **"Deploy from GitHub repo"**
5. Choose your forked PolyBot repository

### Step 3: Set Environment Variables

In the Railway dashboard, go to your project → **Variables** tab. Add these:

**Required (the bot will NOT work without these):**

| Variable | Example Value | What It Is |
|----------|---------------|-----------|
| `POLYGON_PRIVATE_KEY` | `0xabc123...` | Your wallet's private key |
| `WALLET_ADDRESS` | `0xdef456...` | Your wallet's public address |

**Recommended:**

| Variable | Value | What It Is |
|----------|-------|-----------|
| `ALCHEMY_API_KEY` | `your-key-here` | Makes blockchain calls faster |
| `DRY_RUN` | `true` | Start with `true` to test without real money! |
| `AUTO_EXECUTE` | `true` | Let the bot trade automatically |
| `MODE` | `updown` | Trade 5-minute Up/Down crypto markets |

### Step 4: Deploy

Railway will automatically build and deploy your bot. This takes about 2 minutes.

### Step 5: Verify It Works

Open these URLs in your browser (replace `your-bot` with your Railway URL):

```
https://your-bot.railway.app/api/health       → Should show {"status": "ok"}
https://your-bot.railway.app/api/status        → Shows bot status and wallet info
https://your-bot.railway.app/dashboard         → Web dashboard with live data
```

### Step 6: Go Live (When Ready)

When you are confident everything works:

1. Change `DRY_RUN` to `false` in Railway Variables
2. Make sure your wallet has USDC loaded
3. Redeploy the bot
4. **The bot is now trading with REAL money!**

---

## 💻 Local Development Setup (For Developers)

If you want to run the bot on your own computer (for testing or development):

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PolyBot.git
cd PolyBot
```

### Step 2: Install Python Dependencies

```bash
# Install the bot and all development dependencies
pip install -e ".[dev]"
```

This installs:
- The bot itself (as a Python package called `polybot`)
- All runtime dependencies (FastAPI, Web3, etc.)
- Development tools (pytest, pandas, etc.)

### Step 3: Create Your Environment File

```bash
# Copy the example environment file
cp env.example .env
```

Now open `.env` in a text editor and fill in your values:

```bash
# SAFE DEFAULTS for testing — change for production!
MODE=updown
DRY_RUN=true                   # true = simulate only, false = REAL trades
AUTO_EXECUTE=false             # false = don't auto-trade, true = auto-trade

# Your wallet credentials (REQUIRED for live trading)
POLYGON_PRIVATE_KEY=0x...      # Your private key (NEVER commit this!)
WALLET_ADDRESS=0x...           # Your wallet address
ALCHEMY_API_KEY=...            # Alchemy API key (optional but recommended)
```

### Step 4: Run the Bot

```bash
# Run in dry-run mode (no real trades)
DRY_RUN=true uvicorn src.polybot.main_fastapi:app --reload --port 8000
```

Then open [http://localhost:8000/api/health](http://localhost:8000/api/health) in your browser.

### Step 5: Run the Tests

```bash
# Run all tests
pytest tests/ -v

# Run tests with code coverage
pytest tests/ -v --cov=src/polybot

# Run a specific test file
pytest tests/test_scanner.py -v
```

---

## 🐳 Docker Setup

### Option A: Docker Compose (Recommended for Local Docker)

This starts the bot, Redis (for caching), and an optional Next.js frontend:

```bash
# 1. Make sure Docker and Docker Compose are installed

# 2. Create your .env file (see Step 3 above)
cp env.example .env
# Edit .env with your values

# 3. Start everything
docker-compose up

# 4. Stop everything
docker-compose down
```

**Services that start:**
| Service | Port | What It Does |
|---------|------|-------------|
| Backend (FastAPI) | 8000 | The trading bot itself |
| Redis | 6379 | Caching for execution logs |
| Frontend (Next.js) | 3000 | Optional web dashboard |

### Option B: Docker Only (No Compose)

```bash
# Build the Docker image
docker build -t polybot:latest .

# Run the container
docker run -d \
  --name polybot \
  -p 8000:8000 \
  -e DRY_RUN=true \
  -e POLYGON_PRIVATE_KEY=0x... \
  -e WALLET_ADDRESS=0x... \
  -e ALCHEMY_API_KEY=... \
  polybot:latest

# Check if it's running
docker ps

# View logs
docker logs -f polybot

# Stop the container
docker stop polybot
```

### Docker Image Details

- **Base image:** Python 3.11-slim
- **Multi-stage build:** ~200MB smaller than single-stage
- **Runs as non-root user** (UID 1000) for security
- **Health check built in:** Checks `/api/health` every 30 seconds
- **Exposed port:** 8000

---

## ⚙️ Environment Variables — Complete Reference

### Core Trading Settings

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `MODE` | `updown` | No | Trading mode. See [Trading Modes](#-trading-modes). |
| `DRY_RUN` | `false` | **YES** | `true` = simulate only (no real trades). `false` = trade with REAL money. **Always start with `true`!** |
| `AUTO_EXECUTE` | `true` | No | `true` = bot trades automatically. `false` = bot only logs what it would trade. |

### Edge & Threshold Settings

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `MIN_EV` | `0.015` | No | Minimum expected value. `0.015` = 1.5%. The bot ignores trades with less edge than this. Higher = fewer but safer trades. |
| `MIN_EDGE_PERCENT` | `0.85` | No | Minimum edge percentage. Another filter to avoid bad trades. |

### Position Sizing (How Much to Bet)

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `KELLY_MULTIPLIER` | `0.5` | No | `0.5` = Half-Kelly (safer). `1.0` = Full Kelly (riskier). Lower = smaller bets = safer. |
| `MAX_POSITION_USD` | `50` | No | Maximum dollars per trade. The bot will never bet more than this on a single trade. |
| `MIN_TRADE_USD` | `5` | No | Minimum trade size in USD. Trades smaller than this are skipped. |

### Market Filters (What Markets to Trade)

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `MIN_LIQUIDITY_USD` | `200` | No | Minimum market liquidity in USD. Low liquidity = hard to buy/sell = bad. |
| `MIN_VOLUME_USD` | `100` | No | Minimum 24-hour trading volume. Low volume = not enough trading activity. |
| `UP_DOWN_ONLY` | `true` | No | `true` = only trade 5-minute Up/Down markets. `false` = trade all market types. |
| `TARGET_SYMBOLS` | `BTC,ETH,SOL` | No | Which cryptocurrencies to trade. Comma-separated. |

### Scan Interval

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `SCAN_INTERVAL_SECONDS` | `12` | No | How often (in seconds) the bot scans for new opportunities. Range: 5–300. |
| `SMART_SCAN_ENABLED` | `true` | No | Adjusts scan speed near market close for better timing. |
| `HIGH_FREQUENCY_INTERVAL` | `5` | No | Scan interval (seconds) in the final minute before market close. |
| `NORMAL_INTERVAL` | `30` | No | Scan interval (seconds) during normal times. |

### Wallet & Credentials (REQUIRED for Live Trading)

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `POLYGON_PRIVATE_KEY` | — | **YES** | Your Polygon wallet's private key. Starts with `0x`. **NEVER commit this to Git!** |
| `WALLET_ADDRESS` | — | **YES** | Your Polygon wallet's public address. Starts with `0x`. |
| `ALCHEMY_API_KEY` | — | Recommended | Your Alchemy API key for fast Polygon RPC. Free tier works. |
| `FORCE_ALCHEMY` | `true` | No | Force using Alchemy RPC instead of slower public RPCs. |
| `AUTO_APPROVE_ENABLED` | `true` | No | Automatically approve USDC spending on the Polymarket exchange contract. |

### Full Redeemer V89

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `FULL_REDEEM_ENABLED` | `false` | No | Enable automatic position redemption every 45 seconds. |
| `FULL_REDEEM_INTERVAL_SECONDS` | `45` | No | How often (in seconds) to scan for redeemable positions. |
| `MIN_REDEEM_BALANCE` | `0.08` | No | Minimum USDC balance needed to run the redeemer (only needs gas money). |
| `REDEEM_GAS_BUFFER_PERCENT` | `30` | No | Extra gas price buffer percentage for redemption transactions. |

### Logging & Debugging

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `LOG_LEVEL` | `DEBUG` | No | How much detail to show in logs. Options: `DEBUG` (most detail), `INFO`, `WARNING`, `ERROR`. |

### Hyperparameter Optimization (Advanced)

| Variable | Default | Required? | What It Does |
|----------|---------|-----------|-------------|
| `OPTUNA_SAMPLER` | `tpe` | No | Algorithm for hyperparameter optimization. Options: `tpe`, `cmaes`, `random`, `grid`. |
| `OPTUNA_N_TRIALS` | `30` | No | Number of optimization trials to run. |
| `OPTUNA_VIZ_ENABLED` | `true` | No | Generate interactive optimization charts. |
| `AUTO_APPLY_BEST` | `true` | No | Automatically apply the best parameters found by optimization. |
| `VIZ_DIR` | `/app/static/optuna_viz` | No | Directory for optimization visualization files. |

---

## 🎯 Trading Modes

PolyBot supports four trading modes. Set the `MODE` environment variable to switch between them.

### 1. `MODE=updown` (Default — Recommended)

**What it does:** Trades 5-minute crypto Up/Down prediction markets.

**How it works:**
- Scans for markets like "Will BTC go up in the next 5 minutes?"
- Calculates edge based on price deviation from fair value
- Places YES or NO bets depending on predicted direction
- Targets BTC, ETH, and SOL markets

**Best for:** Most users. These markets have the best liquidity and shortest resolution time.

### 2. `MODE=signal`

**What it does:** Uses real-time data from centralized exchanges (like Binance) to detect trading signals.

**Signal types detected:**
- **Order Flow Imbalance (OFI):** Detects hidden buying or selling pressure before price moves
- **Liquidation Cascades:** Detects forced liquidations that cause large price moves (80%+ directional probability)
- **Latency Arbitrage:** Detects when the CEX price has moved but Polymarket hasn't updated yet (15–90 second edge window)

**Best for:** Advanced users who want to exploit information advantages.

### 3. `MODE=copy`

**What it does:** Copies trades from other successful Polymarket traders.

**How it works:**
- Monitors specified wallet addresses on Polymarket
- When they place a trade, the bot copies it
- Mirrors their position sizing (proportionally)

**Best for:** Users who want to follow proven traders.

### 4. `MODE=arbitrage`

**What it does:** Looks for risk-free arbitrage opportunities.

**How it works:**
- In a binary market, YES + NO should always equal $1.00
- Sometimes YES + NO < $1.00 due to market inefficiency
- The bot buys both YES and NO, guaranteeing a profit regardless of outcome

**Best for:** Users who want lower risk. Opportunities are rare but profitable when they appear.

---

## 🔄 Full Redeemer V89 — Automatic Winnings Collection

When you win a trade on Polymarket, your winning shares need to be **redeemed** (converted back to USDC). The Full Redeemer does this automatically.

### Why Is This Needed?

- The old auto-redeem only tracked positions the bot created during the current session
- If the bot restarted, it would "forget" about older winning positions
- The Full Redeemer V89 scans the blockchain directly, so it finds ALL your positions, even ones from before the bot started

### How It Works

1. Every 45 seconds, the redeemer scans the CTF (Conditional Token Framework) smart contract on Polygon
2. It finds all ERC-1155 token balances in your wallet
3. It queries Polymarket's Data API to check which positions are resolved (market ended, outcome decided)
4. It batches and redeems all resolved positions, converting them back to USDC

### How to Enable It

**Option 1: Automatic (recommended for production)**

Set this environment variable:
```
FULL_REDEEM_ENABLED=true
```

**Option 2: Manual trigger via API**

```bash
# Trigger a manual redemption scan
curl -X POST https://your-bot.railway.app/api/force_full_redeem

# Check the status of the redeemer
curl https://your-bot.railway.app/api/full_redeemer_status
```

### Full Redeemer Settings

| Variable | Default | What It Does |
|----------|---------|-------------|
| `FULL_REDEEM_ENABLED` | `false` | `true` = scan for redeemable positions automatically |
| `FULL_REDEEM_INTERVAL_SECONDS` | `45` | How often to scan (in seconds) |
| `MIN_REDEEM_BALANCE` | `0.08` | Minimum USDC needed (just for gas fees, much lower than the $1.2+ needed for trading) |
| `REDEEM_GAS_BUFFER_PERCENT` | `30` | Extra gas price buffer (to make sure transactions go through) |

---

## 🌐 API Endpoints — Complete Reference

The bot runs a FastAPI web server on port 8000. Here are all available endpoints:

### Health & Status

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/health` | Basic health check. Returns `{"status": "ok"}` if the bot is running. |
| GET | `/api/status` | Comprehensive bot status: wallet balance, RPC health, scan cycle info, and more. |
| GET | `/api/production-status` | Production readiness checklist — shows if everything is properly configured. |

### Trading & Positions

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/positions` | Lists all open positions (market name, buy price, current price, unrealized P&L). |
| GET | `/api/pnl` | Profit & Loss summary (realized P&L, unrealized P&L, total fees paid). |

### RPC & Infrastructure

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/rpc-status` | Shows all RPC providers ranked by latency (response time). |
| GET | `/api/rpc_health` | Detailed RPC health statistics. |
| GET | `/api/allowance_status` | Shows USDC spending allowance status on the exchange contract. |

### Risk Management

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/risk_status` | Circuit breaker and risk limit status (daily loss, consecutive losses, etc.). |

### Scanning

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/next_scan` | Shows when the next scan will happen and smart scan timing info. |

### Full Redeemer V89

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| POST | `/api/force_full_redeem` | Manually trigger a full redemption scan right now. |
| GET | `/api/full_redeemer_status` | Shows the redeemer's last scan time, positions found, and redemption results. |

### Backtesting & Optimization

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/api/backtest-report` | Shows backtest results (win rate, Sharpe ratio, profit factor, max drawdown). |
| GET | `/api/strategy-comparison` | Compares the top Optuna optimization trials side by side. |

### Dashboard

| Method | Endpoint | What It Does |
|--------|----------|-------------|
| GET | `/dashboard` | Full HTML dashboard with charts, trades, and live data. |

---

## 🖥️ CLI Commands

PolyBot includes a command-line interface (CLI) built with Typer:

```bash
# Start the FastAPI server (default command)
polybot

# Start the API server explicitly
polybot api

# Run the trading loop
polybot run

# Run the legacy dashboard
polybot dashboard
```

> **Note:** The `polybot` command is available after installing with `pip install -e ".[dev]"`. If it does not work, you can always use `uvicorn` directly:
> ```bash
> uvicorn src.polybot.main_fastapi:app --host 0.0.0.0 --port 8000
> ```

---

## 📊 Dashboard & Monitoring

PolyBot includes a built-in web dashboard:

- **`/dashboard`** — Main HTML dashboard with live data, built with Jinja2 templates
- **`/api/status`** — JSON status endpoint for programmatic access

### What the Dashboard Shows

- **Bot status:** Running, scanning, trading mode, dry-run status
- **Wallet info:** USDC balance, wallet address
- **Open positions:** Current trades with unrealized P&L
- **Trade history:** Past trades with outcomes
- **P&L chart:** Profit and loss over time
- **RPC status:** Which blockchain providers are active and their latency

---

## 📈 Backtesting — Test Strategies on Historical Data

Backtesting lets you test how the bot's strategy would have performed on past markets — without risking real money.

### What the Backtester Does

1. Fetches resolved (completed) markets from Polymarket's Gamma API
2. Simulates trades the bot would have made using your current settings
3. Calculates performance metrics:

| Metric | What It Means |
|--------|-------------|
| **Win Rate** | Percentage of trades that were profitable |
| **Sharpe Ratio** | Risk-adjusted return (higher = better, >1 is good) |
| **Profit Factor** | Gross wins ÷ gross losses (>1 means profitable) |
| **Max Drawdown** | Largest peak-to-trough loss (how bad it got at its worst) |
| **Equity Curve** | Chart showing your balance over time |

### How to Run a Backtest

```bash
# Run backtester tests
pytest tests/test_backtester.py -v

# Access backtest report via API (when bot is running)
curl http://localhost:8000/api/backtest-report
```

---

## 🔧 Hyperparameter Optimization

PolyBot uses [Optuna](https://optuna.org/) to automatically find the best trading parameters.

### What It Optimizes

| Parameter | Range | What It Controls |
|-----------|-------|-----------------|
| `MIN_EV` | 0.01 → 0.05 | Minimum expected value threshold |
| `KELLY_MULTIPLIER` | 0.3 → 1.0 | Bet sizing aggressiveness |
| `MAX_POSITION_USD` | 10 → 100 | Maximum bet size per trade |

### Optimization Algorithms

| Algorithm | Environment Variable | Description |
|-----------|---------------------|-------------|
| **TPE** (default) | `OPTUNA_SAMPLER=tpe` | Bayesian optimization — smart, learns from previous trials |
| **CMA-ES** | `OPTUNA_SAMPLER=cmaes` | Evolutionary strategy — good for continuous parameters |
| **Random** | `OPTUNA_SAMPLER=random` | Random search — good baseline for comparison |
| **Grid** | `OPTUNA_SAMPLER=grid` | Exhaustive search — tests every combination |

### How It Works

1. Optuna runs multiple "trials," each with different parameter values
2. Each trial runs a backtest with those parameters
3. Walk-forward validation prevents overfitting (tests on unseen data)
4. The best parameters are saved and can be auto-applied

### Configuration

```bash
OPTUNA_SAMPLER=tpe          # Which algorithm to use
OPTUNA_N_TRIALS=30          # How many trials to run (more = better but slower)
OPTUNA_VIZ_ENABLED=true     # Generate interactive charts
AUTO_APPLY_BEST=true        # Automatically use the best parameters found
```

---

## 🏗️ Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     FastAPI Web Server                        │
│                    (Port 8000, async)                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌── Continuous Scanner (every 12s) ────────────────────┐  │
│   │                                                      │  │
│   │  1. MaxProfitScanner → Fetch markets from Gamma API  │  │
│   │  2. Filter → 5min Up/Down, BTC/ETH/SOL, liquidity   │  │
│   │  3. EdgeEngine → Calculate trading edge              │  │
│   │  4. EV Check → Edge > MIN_EV?                        │  │
│   │  5. Kelly Sizing → How much to bet                   │  │
│   │  6. Executor → Place order via CLOB API              │  │
│   │  7. PnL Tracker → Record result                      │  │
│   │                                                      │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                              │
│   ┌── Full Redeemer V89 (every 45s) ────────────────────┐  │
│   │  Scan blockchain → Find resolved positions → Redeem  │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                              │
│   ┌── Cut-Loss Monitor (every 30s) ─────────────────────┐  │
│   │  Check prices → Stop-loss losers → Auto-redeem wins  │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                              │
│   ┌── API Endpoints ────────────────────────────────────┐  │
│   │  /api/health, /api/status, /api/pnl, /dashboard...  │  │
│   └──────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────┬──────────────┬────────────────────────────┘
                   │              │
          ┌────────▼──────┐  ┌───▼──────────────────┐
          │  Polygon RPC  │  │  Polymarket APIs     │
          │  (Alchemy or  │  │  - Gamma (markets)   │
          │   public)     │  │  - CLOB (orders)     │
          │               │  │  - Data (positions)  │
          └───────┬───────┘  └──────────────────────┘
                  │
          ┌───────▼───────────────────────┐
          │    Polygon Blockchain          │
          │    - USDC (ERC-20)            │
          │    - CTF Exchange             │
          │    - Conditional Tokens       │
          │      (ERC-1155)               │
          └───────────────────────────────┘
```

### External Services Used

| Service | URL | What For |
|---------|-----|----------|
| **Polymarket Gamma API** | `https://gamma-api.polymarket.com` | Market data, prices, liquidity |
| **Polymarket CLOB API** | `https://clob.polymarket.com` | Order placement and execution |
| **Polymarket Data API** | `https://data.polymarket.com` | Position data for redemption |
| **Alchemy RPC** | `https://polygon-mainnet.g.alchemy.com` | Fast Polygon blockchain access |
| **Polygon Public RPCs** | Various | Fallback blockchain access |
| **Binance WebSocket** | `wss://stream.binance.com` | Real-time CEX data (signal mode) |

### Smart Contracts (On Polygon)

| Contract | Address | What It Does |
|----------|---------|-------------|
| **USDC** | `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` | Stablecoin used for trading |
| **CTF Exchange** | `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` | Polymarket's trading exchange |
| **Conditional Tokens** | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` | ERC-1155 tokens representing positions |

---

## 📂 Project Structure

```
PolyBot/
├── src/polybot/                    # Main source code (Python)
│   ├── __init__.py                 # Package initialization
│   ├── __main__.py                 # Entry point for `python -m polybot`
│   ├── main_fastapi.py             # FastAPI app, scanner loop, API endpoints
│   ├── config.py                   # All configuration (environment variables)
│   ├── cli.py                      # Command-line interface (Typer)
│   │
│   ├── scanner.py                  # MaxProfitScanner — finds trading opportunities
│   ├── scanner_updown.py           # 5-minute Up/Down market scanner
│   ├── edge_engine.py              # Calculates trading edge (deviation-based)
│   ├── signal_engine.py            # CEX-based signals (OFI, liquidations)
│   ├── signals.py                  # Signal routing and timing
│   │
│   ├── executor.py                 # Trade execution with Kelly sizing
│   ├── onchain_executor.py         # On-chain order execution via CLOB
│   ├── full_redeemer.py            # V89: Automatic position redemption
│   ├── redeem_all.py               # Bulk redemption utility
│   ├── redeem_stuck_positions.py   # Recovery for stuck positions
│   ├── approve_usdc.py             # USDC spending approval
│   │
│   ├── risk_manager.py             # Circuit breaker and risk limits
│   ├── risk.py                     # Risk calculations
│   ├── portfolio_manager.py        # Position sizing and tracking
│   ├── pnl_tracker.py              # Profit & Loss tracking
│   │
│   ├── backtester.py               # Historical backtest engine
│   ├── backtest.py                 # Backtest CLI command
│   ├── optimizer.py                # Hyperparameter optimization (Optuna)
│   │
│   ├── indicators.py               # Technical indicators (MA, RSI, MACD)
│   ├── simple_trend_filter.py      # Trend detection
│   ├── hourly_risk_regime.py       # Hourly volatility detection
│   ├── volatility_regime.py        # Volatility state tracking
│   │
│   ├── rpc_manager.py              # Polygon RPC management + Alchemy
│   ├── proxy.py                    # Proxy rotation
│   ├── retries.py                  # Exponential backoff retry logic
│   ├── credentials_manager.py      # L2 API credential derivation
│   ├── check_wallet.py             # Wallet balance verification
│   ├── startup_checks.py           # Pre-flight validation
│   │
│   ├── database.py                 # SQLite initialization
│   ├── models.py                   # ORM models (SQLModel)
│   ├── api.py                      # API helpers
│   ├── logging_setup.py            # Structured logging
│   │
│   ├── dashboard.py                # HTML dashboard routes
│   ├── templates/                  # Jinja2 HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── pnl.html
│   │   ├── positions.html
│   │   └── trades.html
│   │
│   ├── arbitrage.py                # YES+NO < $1 arbitrage detection
│   ├── copy_trading.py             # Copy-trader tracking
│   ├── compounding.py              # Profit reinvestment
│   ├── funding.py                  # NegRisk funding calculations
│   ├── whale_tracker.py            # Large order tracking
│   ├── solana_bridge.py            # Solana bridge (optional)
│   └── ...                         # Other utility modules
│
├── tests/                          # Test suite (24 test files)
│   ├── test_scanner.py
│   ├── test_onchain_executor.py
│   ├── test_full_redeemer.py
│   ├── test_risk_manager.py
│   ├── test_signal_engine.py
│   ├── test_backtester.py
│   ├── test_optimizer.py
│   ├── test_pnl_tracker.py
│   └── ...                         # 16 more test files
│
├── docs/                           # Documentation in 10 languages
│   ├── MANUAL_AR.md                # Arabic
│   ├── MANUAL_ES.md                # Spanish
│   ├── MANUAL_FR.md                # French
│   ├── MANUAL_JA.md                # Japanese
│   ├── MANUAL_KLINGON.md           # Klingon (Star Trek)
│   ├── MANUAL_PL.md                # Polish
│   ├── MANUAL_RU.md                # Russian
│   ├── MANUAL_SINDARIN.md          # Sindarin (Lord of the Rings)
│   ├── MANUAL_VALYRIAN.md          # High Valyrian (Game of Thrones)
│   ├── MANUAL_ZH.md                # Chinese
│   └── images/                     # Documentation images
│
├── static/                         # Static web assets
│   └── dashboard.html              # Standalone dashboard
│
├── .github/workflows/ci.yml       # GitHub Actions CI/CD pipeline
├── Dockerfile                      # Multi-stage Docker build
├── docker-compose.yml              # Local dev with Docker Compose
├── railway.toml                    # Railway build configuration
├── railway.json                    # Railway deployment settings
├── nixpacks.toml                   # Nix package manager config
├── pyproject.toml                  # Python package configuration
├── requirements.txt                # Python dependencies
├── env.example                     # Example environment variables
├── .pre-commit-config.yaml         # Pre-commit hooks (code formatting)
├── .gitignore                      # Git ignore rules
├── migrate_to_polybot2.sh          # Migration script for fresh repos
├── redeem_all.py                   # Standalone redemption script
└── LICENSE                         # MIT License
```

---

## 🧪 Running Tests

PolyBot has 24 test files with comprehensive coverage.

### Run All Tests

```bash
pytest tests/ -v
```

### Run Tests with Coverage Report

```bash
pytest tests/ -v --cov=src/polybot
```

### Run a Specific Test File

```bash
pytest tests/test_scanner.py -v
pytest tests/test_onchain_executor.py -v
pytest tests/test_full_redeemer.py -v
```

### Run Tests Matching a Keyword

```bash
pytest tests/ -k "scanner" -v     # Runs all tests with "scanner" in the name
pytest tests/ -k "edge" -v        # Runs all tests with "edge" in the name
```

### Linting (Code Style Checks)

```bash
# Check for code style issues
ruff check src/ tests/

# Check code formatting
ruff format --check src/ tests/

# Auto-fix formatting
ruff format src/ tests/
```

---

## 🔁 CI/CD Pipeline

Every push and pull request triggers a GitHub Actions pipeline (`.github/workflows/ci.yml`):

| Job | What It Does | Runs On |
|-----|-------------|---------|
| **Lint** | Checks code style with Ruff | Every push/PR |
| **Test** | Runs pytest on all test files | Every push/PR |
| **Backtest Validation** | Tests that key modules can be imported correctly | After lint + test pass |
| **Docker Build** | Builds the Docker image to make sure it works | After lint + test pass |

### Branches Watched

- `main` — Production branch
- `develop` — Development branch

### Running CI Locally

You can run the same checks that CI runs:

```bash
# Lint
ruff check src/ tests/
ruff format --check src/ tests/

# Test
pytest tests/ -v --tb=short

# Validate imports (same as backtest job)
python -c "from polybot.backtester import Backtester, BacktestResult; print('OK')"
python -c "from polybot.portfolio_manager import PortfolioManager; print('OK')"
python -c "from polybot.volatility_regime import VolatilityRegimeDetector; print('OK')"
python -c "from polybot.execution_logger import ExecutionLogger; print('OK')"
```

---

## 🔀 Migration to a Fresh Repository

If your Git history is too large or corrupted, you can create a fresh copy:

```bash
# From inside the PolyBot directory:
./migrate_to_polybot2.sh            # Creates ../polybot2 with clean history

# Push to a new GitHub repo:
cd ../polybot2
gh repo create polybot2 --private --source=. --push
```

The original PolyBot directory stays untouched.

---

## ❓ Troubleshooting & FAQ

### "The bot is running but not making any trades"

**Possible causes:**
1. `DRY_RUN=true` — The bot is in simulation mode. Set `DRY_RUN=false` for real trades.
2. `AUTO_EXECUTE=false` — The bot won't auto-trade. Set `AUTO_EXECUTE=true`.
3. No USDC in wallet — Check your wallet balance at `/api/status`.
4. No markets meet criteria — The bot only trades when it finds an edge > `MIN_EV`. This is normal.
5. Low liquidity — Markets might not have enough liquidity during quiet periods.

### "I see errors about RPC or Web3"

**Possible causes:**
1. No `ALCHEMY_API_KEY` set — The bot is using slow public RPCs that can have rate limits. Add your Alchemy key.
2. Public RPCs are down — This happens occasionally. The bot has fallback logic and will retry.
3. Network congestion — Polygon can be slow during high-traffic periods.

### "My positions aren't being redeemed"

1. Enable the Full Redeemer: Set `FULL_REDEEM_ENABLED=true`.
2. Or trigger manually: `curl -X POST https://your-bot.railway.app/api/force_full_redeem`.
3. Make sure you have enough USDC for gas (at least $0.08).

### "How much money do I need to start?"

- **Minimum:** About $10 USDC (enough for a couple of trades at $5 each)
- **Recommended:** $50–$100 USDC (gives the bot room to diversify)
- **Plus:** A tiny amount of MATIC/POL for gas fees (~$0.01 per transaction)

### "Is this bot profitable?"

That depends on market conditions, parameters, and timing. The bot uses mathematical edge detection and Kelly Criterion sizing, but **there are no guarantees**. Always start with `DRY_RUN=true` and backtest before using real money.

### "Can I run multiple instances?"

The bot is designed for single-instance deployment. Running multiple instances with the same wallet could cause conflicts (double-spending, conflicting positions).

### "How do I update the bot?"

```bash
# If deployed on Railway:
# Just push to your GitHub repo — Railway auto-deploys

# If running locally:
git pull origin main
pip install -e ".[dev]"
```

---

## 🔒 Security Best Practices

1. **NEVER commit your private key to Git.** Use environment variables (Railway Variables, `.env` file).
2. **The `.env` file is in `.gitignore`** — but double-check before committing.
3. **Use a dedicated trading wallet.** Don't use your main wallet. Create a separate wallet just for the bot.
4. **Start with small amounts.** Test with $10–$20 before scaling up.
5. **Monitor the bot.** Check `/api/status` and `/api/pnl` regularly.
6. **Keep your Alchemy API key private.** Don't share it publicly.
7. **The Docker image runs as a non-root user** (UID 1000) for container security.
8. **Use `DRY_RUN=true` first.** Always test before going live.

---

## 🤝 Contributing

Contributions are welcome! Here is how to contribute:

1. **Fork** the repository
2. **Create a branch** for your feature: `git checkout -b feature/my-feature`
3. **Make your changes** and write tests
4. **Run linting and tests:**
   ```bash
   ruff check src/ tests/
   ruff format --check src/ tests/
   pytest tests/ -v
   ```
5. **Commit** your changes: `git commit -m "Add my feature"`
6. **Push** to your fork: `git push origin feature/my-feature`
7. **Open a Pull Request** against the `main` branch

### Code Style

- Code is formatted with **Ruff** (Python linter and formatter)
- Pre-commit hooks are configured in `.pre-commit-config.yaml`
- All new code should have tests in the `tests/` directory

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software. See the full license text for details.

---

## 📚 Additional Documentation

Documentation is available in 10 languages in the `docs/` folder:

| Language | File |
|----------|------|
| Arabic | [docs/MANUAL_AR.md](docs/MANUAL_AR.md) |
| Chinese | [docs/MANUAL_ZH.md](docs/MANUAL_ZH.md) |
| French | [docs/MANUAL_FR.md](docs/MANUAL_FR.md) |
| High Valyrian (Game of Thrones) | [docs/MANUAL_VALYRIAN.md](docs/MANUAL_VALYRIAN.md) |
| Japanese | [docs/MANUAL_JA.md](docs/MANUAL_JA.md) |
| Klingon (Star Trek) | [docs/MANUAL_KLINGON.md](docs/MANUAL_KLINGON.md) |
| Polish | [docs/MANUAL_PL.md](docs/MANUAL_PL.md) |
| Russian | [docs/MANUAL_RU.md](docs/MANUAL_RU.md) |
| Sindarin (Lord of the Rings) | [docs/MANUAL_SINDARIN.md](docs/MANUAL_SINDARIN.md) |
| Spanish | [docs/MANUAL_ES.md](docs/MANUAL_ES.md) |

---

## 📊 Feature Summary

| Feature | Status | Description |
|---------|--------|-------------|
| 5-Minute Market Scanner | ✅ | Scans ~2,395 markets, filters to ~15–30 opportunities |
| Edge Engine v2 | ✅ | Deviation-based edge calculation |
| Kelly Criterion Sizing | ✅ | Half-Kelly position sizing (safer) |
| Auto-Execute Trading | ✅ | Real trades when `DRY_RUN=false` |
| Full Redeemer V89 | ✅ | On-chain position scanning and automatic redemption |
| Backtester | ✅ | Test strategies on historical data |
| Optuna Hyperparameter Optimization | ✅ | TPE, CMA-ES, Random, Grid search algorithms |
| Web Dashboard | ✅ | Live HTML dashboard at `/dashboard` |
| REST API | ✅ | 15+ endpoints for monitoring and control |
| Signal Engine | ✅ | CEX-based OFI, liquidation, and latency signals |
| Arbitrage Detection | ✅ | YES+NO < $1 risk-free opportunities |
| Copy Trading | ✅ | Mirror trades from other wallets |
| Risk Management | ✅ | Circuit breaker, loss limits, drawdown protection |
| Docker Support | ✅ | Multi-stage build, non-root user, health checks |
| Railway Deployment | ✅ | One-click deploy from GitHub |
| CI/CD Pipeline | ✅ | Automated lint, test, backtest, Docker build |
| Multi-Language Docs | ✅ | Documentation in 7 languages |
| Graceful Shutdown | ✅ | Backs up state on exit |
| Smart Scan Timing | ✅ | Faster scanning near market close |
| RPC Resilience | ✅ | Automatic fallback between RPC providers |

---

**Happy trading! Remember: always start with `DRY_RUN=true` and test before risking real money.** 🚀
