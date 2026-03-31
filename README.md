# 🤖 PolyBot — Your Friendly Crypto Trading Helper

Hello there, friend! 👋 Welcome to **PolyBot**!

PolyBot is a little helper program (we call it a "bot") that trades on a website called **Polymarket** all by itself. It looks at short 5-minute games where you guess if the price of Bitcoin (BTC), Ethereum (ETH), or Solana (SOL) will go **up** or **down**. The bot tries to be very smart about which games to play, and it collects your winnings for you too!

> **Super Important:** This bot uses **real money**. Please be very, very careful. Read everything below before you turn it on!

> ⚠️ **FORCED EXECUTION v5 Notice:** In this version, the bot's safety circuit breakers (daily loss limit, consecutive loss pauses, drawdown stops) are **disabled** to maximize trade throughput. This means the bot will keep trading even during losing streaks. Please monitor your bot closely and use `REDEEM_ONLY=true` to stop trading if needed!

---

## 📖 Table of Contents

1. [What Does PolyBot Do?](#-what-does-polybot-do)
2. [What You Need Before You Start](#-what-you-need-before-you-start)
3. [How to Set It Up (Step by Step)](#-how-to-set-it-up-step-by-step)
4. [All the Settings You Can Change](#-all-the-settings-you-can-change)
5. [The Volatility Schedule (NEW!)](#-the-volatility-schedule-new)
6. [Sniper Mode](#-sniper-mode)
7. [The Full Redeemer (Collecting Your Winnings)](#-the-full-redeemer-collecting-your-winnings)
8. [The Dashboard (Watching Your Bot)](#-the-dashboard-watching-your-bot)
9. [How the Bot Makes Decisions](#-how-the-bot-makes-decisions)
10. [Safety Features](#-safety-features)
11. [Running It on Your Own Computer (For Testing)](#-running-it-on-your-own-computer-for-testing)
12. [Running Tests](#-running-tests)
13. [All the Web Pages and API Links](#-all-the-web-pages-and-api-links)
14. [Troubleshooting (When Things Go Wrong)](#-troubleshooting-when-things-go-wrong)
15. [Moving to a Fresh Copy](#-moving-to-a-fresh-copy)
16. [Feature List](#-feature-list)
17. [Version History](#-version-history)

---

## 🌟 What Does PolyBot Do?

Okay, imagine this: Every 5 minutes, there is a little game on a website. The game asks: "Will the price of Bitcoin go **up** or **down** in the next 5 minutes?" You can bet a little bit of money on "Up" or "Down."

PolyBot does this for you, automatically! Here is what it does, one step at a time:

1. **It looks at all the games** — There are about 2,395 little games happening. PolyBot looks at all of them.
2. **It picks the best ones** — It only picks games about Bitcoin, Ethereum, or Solana that have enough money in them (at least $200) and enough people playing (at least $100 traded today).
3. **It figures out which way the price will go** — It looks at real prices on Binance (a big crypto exchange) and uses math to guess if the price will go up or down.
4. **It checks if the bet is worth it** — It only bets when it thinks it has a real advantage (we call this "edge"). If the advantage is too small, it says "nah, I'll pass."
5. **It decides how much to bet** — It uses something called "Kelly sizing" which is a smart math formula that says "bet more when you're more sure, bet less when you're not so sure."
6. **It places the bet!** — It actually puts real money on the blockchain and places the trade.
7. **It collects your winnings** — When a game ends and you won, PolyBot collects your money automatically. Even if the bot restarts, it remembers to collect!

**That's it!** It does all of this over and over, every 12 seconds, looking for the next good opportunity.

---

## 📋 What You Need Before You Start

Before you can use PolyBot, you need a few things. Think of these like ingredients for a recipe — you need ALL of them:

### Must-Have Items (You Cannot Skip These!)

| What You Need | Why You Need It | How to Get It |
|---|---|---|
| **A Polygon Wallet** | This is your digital wallet on the Polygon blockchain. PolyBot puts money in and takes money out of this wallet. | Create one at [MetaMask](https://metamask.io) — make sure you pick the "Polygon" network! |
| **Your Private Key** | This is the secret password to your wallet. PolyBot needs it to move your money. | In MetaMask: click the three dots → "Account Details" → "Show Private Key." It starts with `0x` followed by 64 letters and numbers. |
| **Your Wallet Address** | This is like your home address, but for your digital wallet. People can send you money here. | In MetaMask: it's the long address at the top that starts with `0x`. |
| **USDC on Polygon** | USDC is a type of digital dollar. This is the money PolyBot uses to trade. | Buy USDC on an exchange and send it to your Polygon wallet address. You need at least a few dollars to start. |
| **A Railway Account** | Railway is a website that runs your bot in the cloud 24 hours a day, 7 days a week, even when your computer is turned off. | Sign up at [railway.app](https://railway.app). It's free to start! |

### Nice-to-Have Items (Optional, But Helpful!)

| What You Need | Why You Need It | How to Get It |
|---|---|---|
| **An Alchemy API Key** | Alchemy makes the bot talk to the blockchain faster and more reliably. Think of it like giving the bot a faster car! | Sign up at [alchemy.com](https://alchemy.com) — free plan works fine! |
| **A GitHub Account** | To store your copy of the bot's code and connect it to Railway. | Sign up at [github.com](https://github.com). |

> ⚠️ **SUPER DUPER IMPORTANT:** Your **Private Key** is the most secret thing ever. **Never, ever, EVER** share it with anyone. Never put it in a file that other people can see. Never post it online. If someone gets your private key, they can take ALL your money. Keep it safe like a treasure!

---

## 🚀 How to Set It Up (Step by Step)

### Step 1: Get the Code

First, you need to get a copy of PolyBot's code on your computer. Open a terminal (that's the black window where you type commands) and type:

```bash
git clone https://github.com/YOUR_USERNAME/PolyBot.git
```

> **What does this do?** It downloads all of PolyBot's files to your computer, into a new folder called "PolyBot."

Then go into that folder:

```bash
cd PolyBot
```

> **What does this do?** It moves you inside the PolyBot folder, like walking into a room.

### Step 2: Set Up Railway

1. Go to [railway.app](https://railway.app) and sign in.
2. Click **"New Project"**.
3. Click **"Deploy from GitHub Repo"**.
4. Pick the **PolyBot** repo from the list.
5. Railway will start building your bot automatically. Wait for it to finish (it takes about 2 minutes).

### Step 3: Add Your Secret Settings

This is the most important part! You need to tell PolyBot your wallet info and how you want it to behave.

1. In Railway, click on your PolyBot service.
2. Click the **"Variables"** tab.
3. Add these variables **one at a time** by clicking **"New Variable"**:

| Variable Name | What to Type | Why |
|---|---|---|
| `POLYGON_PRIVATE_KEY` | Your private key (starts with `0x`) | So the bot can sign trades with your wallet |
| `WALLET_ADDRESS` | Your wallet address (starts with `0x`) | So the bot knows which wallet to use |
| `DRY_RUN` | `false` | This means "do real trades with real money." Type `true` if you just want to watch without spending money. |
| `AUTO_EXECUTE` | `true` | This means "go ahead and place trades automatically." |
| `ALCHEMY_API_KEY` | Your Alchemy key (optional) | Makes the bot faster. Leave this out if you do not have one. |

> **How to add a variable:** Click "New Variable." In the left box, type the name (like `POLYGON_PRIVATE_KEY`). In the right box, type the value (like `0xabc123...`). Then press Enter.

### Step 4: Redeploy

After you added all your variables, Railway will automatically redeploy. If it does not, click the three dots menu → **"Redeploy"**.

### Step 5: Check If It Is Working

Wait about 1 minute, then open this link in your browser (replace `your-bot` with your actual Railway URL):

```
https://your-bot.railway.app/api/health
```

If you see something like `{"status": "ok"}`, then **congratulations! Your bot is running!** 🎉

You can also visit the dashboard to see what it's doing:

```
https://your-bot.railway.app/dashboard
```

---

## ⚙️ All the Settings You Can Change

These are all the "knobs" you can turn to change how the bot behaves. You set these as **environment variables** on Railway (or in a `.env` file if running locally).

### 🔑 Required Settings (The Bot Won't Work Without These)

| Setting Name | What It Means | Example |
|---|---|---|
| `POLYGON_PRIVATE_KEY` | Your secret wallet key. Starts with `0x` and then 64 characters. **Keep this secret!** | `0xabcdef1234567890...` |
| `WALLET_ADDRESS` | Your public wallet address. Starts with `0x`. | `0x1234abcd5678efgh...` |

### 🎮 Main Settings (The Most Important Knobs)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `DRY_RUN` | `false` | When this is `true`, the bot just pretends to trade. No real money is used. Great for testing! When it is `false`, it uses real money. |
| `AUTO_EXECUTE` | `true` | When this is `true`, the bot places trades all by itself. When it is `false`, it finds good trades but doesn't actually place them. |
| `MODE` | `updown` | What kind of trading the bot does. The main mode is `updown` (5-minute crypto games). Other options: `sniper`, `signal`, `copy`, `arbitrage`. |
| `REDEEM_ONLY` | `false` | Emergency stop! When this is `true`, the bot stops making any new trades and only collects winnings from old trades. Great for safely shutting down. |
| `LOG_LEVEL` | `INFO` | How much detail the bot writes in its diary. Options: `DEBUG` (everything), `INFO` (normal), `WARNING` (only problems), `ERROR` (only big problems). |

### 💰 Money Settings (How Much to Bet)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `KELLY_MULTIPLIER` | `0.5` | Controls bet size. `0.5` means "Half-Kelly" — the bot bets half of what the math says is perfect. This is safer. `1.0` would be full-Kelly (more aggressive). Range: `0.1` to `1.0`. |
| `MAX_POSITION_USD` | `50.0` | The most money the bot will put into one single bet. Even if the math says "bet $100", it will never bet more than this. |
| `MIN_TRADE_USD` | `5.0` | The smallest bet the bot will make. If the math says "bet $3", it won't bother. |
| `MIN_BALANCE_USD` | `0.3` | If your wallet has less than 30 cents, the bot stops trading. |
| `MIN_TRADE_SIZE_USD` | `1.0` | The absolute minimum trade size the Polymarket exchange accepts. |
| `MAX_RISK_PER_TRADE` | `2.0` | The most the bot will risk on one trade, as a percentage of your total balance. |
| `EXECUTION_SLIPPAGE_BPS` | `30` | How much "wiggle room" the bot gives on price. 30 means 0.3%. This helps trades actually go through when prices move fast. |

### 🔍 Market Filter Settings (Which Games to Play)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `MIN_EV` | `0.005` | The minimum "expected value." This is the smallest advantage the bot needs before it will trade. `0.005` means 0.5%. Higher = pickier. Default production value is `0.015` (1.5%). |
| `MIN_EDGE_PERCENT` | `0.85` | Minimum edge percentage to place a trade. |
| `UP_DOWN_ONLY` | `true` | When `true`, the bot ONLY looks at the quick 5-minute Up/Down games. When `false`, it looks at all kinds of markets. |
| `MIN_LIQUIDITY_USD` | `200.0` | The bot only plays games that have at least this much money in them. More liquidity = easier to trade. |
| `MIN_VOLUME_USD` | `100.0` | The bot only plays games where at least this much money was traded in the last 24 hours. |
| `TARGET_SYMBOLS` | `BTC,ETH,SOL` | Which cryptocurrencies to watch. Separate them with commas. Options: `BTC`, `ETH`, `SOL`, `XRP`, `DOGE`. |
| `MIN_CONFIDENCE` | `68` | Minimum signal confidence (0 to 100) before the bot trades. |
| `MIN_CONFIDENCE_FILTER` | `0.65` | Another confidence filter (0.0 to 1.0). |

### 🛡️ Safety Settings (Circuit Breakers — Like Safety Fuses!)

These settings protect you from losing too much money. Think of them like safety fuses in your house — when something goes wrong, they flip off to keep you safe.

| Setting Name | Default Value | What It Means |
|---|---|---|
| `MAX_DAILY_LOSS` | `25.0` | If the bot loses $25 in one day, it stops trading for the rest of the day. |
| `MAX_DAILY_TRADES` | `30` | The bot will make at most 30 trades per day, then it rests. |
| `MAX_POSITION_SIZE_PCT` | `30.0` | No single bet can be more than 30% of your total wallet balance. |
| `MAX_DRAWDOWN_PCT` | `25.0` | If your wallet drops by 25% from its highest point, the bot stops. |
| `MAX_CONCURRENT_POSITIONS` | `3` | The bot will have at most 3 bets running at the same time. |
| `CIRCUIT_BREAKER_CONSECUTIVE_LOSSES` | `4` | If the bot loses 4 times in a row, it takes a timeout break. |
| `MAX_CATEGORY_EXPOSURE` | `50.0` | No more than 50% of your money in one category (like "crypto"). |

### ⏱️ Timing Settings

| Setting Name | Default Value | What It Means |
|---|---|---|
| `SCAN_INTERVAL_SECONDS` | `12` | How often the bot looks for new games (in seconds). Every 12 seconds it checks again. |
| `DAILY_RISK_RESET_HOUR` | `0` | What hour (UTC time) the daily loss counter resets. `0` means midnight UTC. |

### 🔌 Connection Settings (How the Bot Talks to the Blockchain)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `POLYGON_RPC_URL` | `https://polygon-rpc.com` | The "phone number" the bot uses to call the Polygon blockchain. |
| `ALCHEMY_API_KEY` | _(empty)_ | Your Alchemy key for a faster, more reliable connection. Optional but strongly recommended! |
| `FORCE_ALCHEMY` | `true` | When `true`, the bot prefers Alchemy over the free RPC. |
| `AUTO_APPROVE_ENABLED` | `true` | The bot automatically gives Polymarket permission to use your USDC. You want this to be `true`. |
| `MIN_ALLOWANCE_USDC` | `10000.0` | The minimum USDC allowance the bot sets. Don't worry, it only uses what it needs! |

### 🏦 Full Redeemer Settings (Collecting Your Winnings)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `FULL_REDEEM_ENABLED` | `false` | Turn this on (`true`) to automatically collect ALL your winnings, even from before the bot started! |
| `FULL_REDEEM_INTERVAL_SECONDS` | `45` | How often (in seconds) the bot checks for winnings to collect. |
| `MIN_REDEEM_BALANCE` | `0.08` | You need at least 8 cents of USDC to pay for the gas (transaction fee) to collect winnings. |
| `REDEEM_GAS_BUFFER_PERCENT` | `30` | Extra buffer on gas price (30% extra, just to be safe). |
| `STARTUP_REDEEM_ALL` | `true` | When the bot starts up, it immediately checks for any uncollected winnings. |

### 📊 Backtesting Settings (Testing Strategies on Old Data)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `BACKTEST_DAYS` | `30` | How many days of old data to test on. |
| `BACKTEST_MODE` | `edge` | What kind of backtest to run. `edge` uses the EdgeEngine. |
| `BACKTEST_MIN_LIQUIDITY` | `200.0` | Minimum liquidity for backtest markets. |
| `BACKTEST_COMMISSION_BPS` | `20.0` | Simulated trading fees (in basis points). 20 = 0.2%. |
| `BACKTEST_OUTPUT_CSV` | `backtest_results_edge.csv` | Where to save the results. |

### 🧪 Optimization Settings (Finding the Best Settings)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `HYPEROPT_ENABLED` | `false` | Turn on Optuna hyperparameter search (finds the best settings automatically). |
| `OPTUNA_SAMPLER` | `tpe` | The search algorithm. `tpe` is smart Bayesian search. Other options: `cmaes`, `random`, `grid`. |
| `OPTUNA_N_TRIALS` | `50` | How many different settings to try. More trials = better results but takes longer. |
| `OPTUNA_DIRECTION` | `maximize` | Whether to maximize or minimize the target metric. |
| `OPTUNA_VIZ_ENABLED` | `true` | Create pretty charts of the optimization results. |
| `AUTO_APPLY_BEST` | `true` | Automatically use the best settings found. |
| `VIZ_DIR` | `/app/static/optuna_viz` | Where to save the charts. |

### 🌡️ Volatility Schedule Settings (NEW!)

| Setting Name | Default Value | What It Means |
|---|---|---|
| `VOLATILITY_SCHEDULE` | `false` | Turn on the volatility schedule. When `true`, the bot trades bigger during busy market times and smaller during quiet times. |
| `VOLATILITY_MODE` | `adaptive` | How the schedule works. `aggressive` = only trade during busy times. `adaptive` = always trade but adjust size. `passive` = ignore the schedule. |

### 🎯 Sniper Mode Settings

| Setting Name | Default Value | What It Means |
|---|---|---|
| `SNIPER_MODE` | `false` | Turn on sniper mode. The bot waits until the last 30 seconds of a 5-minute game and then places its bet. |

### 📈 Advanced Settings

| Setting Name | Default Value | What It Means |
|---|---|---|
| `POSITION_SCALING_FACTOR` | `1.0` | Scales all position sizes. `2.0` = double all bets, `0.5` = half all bets. Range: `0.1` to `5.0`. |
| `ADAPTIVE_SCALING` | `true` | The bot automatically adjusts bet sizes based on how well it's doing. Winning streak = bigger bets. Losing streak = smaller bets. |

---

## 🕐 The Volatility Schedule (NEW!)

This is a brand new feature! 🎉

### What Is It?

The crypto market is not the same all day long. Sometimes it is very busy and prices move a lot (we call this "volatile"). Sometimes it is very quiet and nothing happens. The **Volatility Schedule** knows when the busy times are, and it tells the bot:

- During **busy times**: "Bet MORE! There are more opportunities!" 🔥
- During **quiet times**: "Bet LESS! There is not much happening." 😴

### When Are the Busy Times?

Here are the times the bot knows about (all times are in UTC):

| Window Name | Time (UTC) | Days | How Much Busier? | Why? |
|---|---|---|---|---|
| 🇺🇸 US Market Open | 14:20 - 15:00 | Mon-Fri | 1.8x bigger bets | When the US stock market opens, crypto prices move A LOT |
| 🇺🇸 US Market Close | 20:50 - 21:10 | Mon-Fri | 1.4x bigger bets | End-of-day scramble |
| 🇬🇧 London Open | 07:50 - 08:20 | Mon-Fri | 1.3x bigger bets | European traders wake up |
| 🇯🇵 Asia Open | 00:00 - 01:00 | Every day | 1.2x bigger bets | Asian traders start their day |
| 💰 Funding Reset 00:00 | 23:55 - 00:10 | Every day | 1.3x bigger bets | Futures funding rates reset, causing liquidations |
| 💰 Funding Reset 08:00 | 07:55 - 08:10 | Every day | 1.3x bigger bets | Same as above |
| 💰 Funding Reset 16:00 | 15:55 - 16:10 | Every day | 1.3x bigger bets | Same as above |
| 📰 Macro Data | 13:25 - 13:45 | Mon-Fri | 1.5x bigger bets | Economic reports come out (CPI, jobs, etc.) |
| 📊 CME Gap | 22:00 - 00:00 | Sunday | 1.4x bigger bets | CME futures reopen after the weekend |

### When Are the Quiet Times?

| Time (UTC) | What Happens |
|---|---|
| 03:00 - 06:00 | Global dead zone. Almost nobody is trading. The bot uses only **60%** of normal bet size. |
| 11:00 - 13:00 | Gap between Asia closing and Europe starting. The bot uses only **60%** of normal bet size. |

### The Three Modes

| Mode | What It Does |
|---|---|
| `adaptive` (default) | The bot always trades, but it bets more during busy times and less during quiet times. |
| `aggressive` | The bot ONLY trades during busy times. During quiet times, it does not trade at all. |
| `passive` | The schedule is ignored. The bot trades the same amount all the time. |

### How to Turn It On

Add these to your Railway variables:

```
VOLATILITY_SCHEDULE=true
VOLATILITY_MODE=adaptive
```

That is all! The bot will now automatically adjust its behavior based on the time of day.

---

## 🎯 Sniper Mode

### What Is Sniper Mode?

Normal mode: The bot scans markets every 12 seconds and trades whenever it finds something good.

Sniper mode is different: The bot **waits** until there are only **30 seconds left** in a 5-minute game, then it quickly analyzes the situation and places a bet. This works because by the time there are only 30 seconds left, the crypto price has usually already moved — so the bot can see which way it went and bet accordingly!

### How Does It Make Decisions?

The sniper uses three sources of information, in this order of priority:

1. **SignalEngine** (best source): Checks Binance for big liquidations, order flow, and price movements. Confidence: 60-82%.
2. **CEX Price Delta**: If the real crypto price moved more than 0.1% during the 5-minute window, the bot bets in that direction.
3. **Market Prices**: If the Polymarket "YES" price is above 0.58, people think it's going up. Below 0.42, people think it's going down.

### How to Turn It On

Set this variable in Railway:

```
SNIPER_MODE=true
```

Or:

```
MODE=sniper
```

> **Note:** Sniper mode now also uses the Volatility Schedule if you have it enabled! During busy market times, the sniper will bet bigger.

---

## 💰 The Full Redeemer (Collecting Your Winnings)

### The Problem It Solves

Imagine you won a bet, but then the bot restarted (maybe Railway updated, maybe the internet hiccupped). The old bot would "forget" about that win and never collect the money! 😱

The **Full Redeemer** fixes this. It looks directly at the blockchain to find ALL your winning positions — even ones from before the bot started running!

### What It Does

1. It asks the Polymarket Data API: "Hey, does this wallet have any winnings to collect?"
2. For each winning position it finds, it sends a transaction to collect the money.
3. It does this every 45 seconds (you can change this).
4. It only needs about $0.08 of USDC for gas fees — way less than the $1.20 you need for trading!

### How to Turn It On

Add this to your Railway variables:

```
FULL_REDEEM_ENABLED=true
```

### How to Manually Collect Winnings

You can also tell the bot to collect winnings right now by opening this URL:

```bash
curl -X POST https://your-bot.railway.app/api/force_full_redeem
```

### How to Check the Status

```bash
curl https://your-bot.railway.app/api/full_redeemer_status
```

---

## 📺 The Dashboard (Watching Your Bot)

PolyBot comes with a web dashboard so you can watch what it's doing! Just open your bot's URL in a browser.

### How to See the Dashboard

Go to:

```
https://your-bot.railway.app/dashboard
```

The dashboard shows you:
- 🟢 **Green dot** = Bot is running and happy
- 🟡 **Yellow dot** = Bot is paused (maybe hit a safety limit)
- 🔴 **Red dot** = Something is wrong
- 💰 **Today's profit/loss** — How much money the bot made or lost today
- 📊 **All-time profit/loss** — How much money the bot made or lost in total
- 🎯 **Win rate** — What percentage of bets the bot won
- 📋 **Recent trades** — The last few trades the bot made
- 📈 **Open positions** — Bets that are still running

The dashboard refreshes automatically every 15 seconds, so you can just leave it open!

---

## 🧠 How the Bot Makes Decisions

Here is the step-by-step thinking process the bot goes through:

### Step 1: Scan Markets (The Scanner)

Every 12 seconds, the scanner wakes up and says:
- "Let me look at all 2,395 markets on Polymarket..."
- "I only care about 5-minute Up/Down crypto games" (if `UP_DOWN_ONLY=true`)
- "This market needs at least $200 of liquidity"
- "This market needs at least $100 of volume in the last 24 hours"
- "I have about 15-30 good candidates to look at!"

### Step 2: Calculate the Edge (The Edge Engine v3)

For each candidate, the Edge Engine asks:
- "What does Polymarket think the probability of UP is?" (This is the market price)
- "What does the real crypto price on Binance say?" (This is reality)
- "Is there a gap between what the market thinks and what reality says?"
- If there IS a gap: "That gap is my edge! I can profit from this!"

The edge engine uses a fancy math model (log-normal probability) with real volatility data:
- Bitcoin (BTC): 45% annual volatility
- Ethereum (ETH): 55% annual volatility
- Solana (SOL): 75% annual volatility

### Step 3: Check Safety Rules (The Risk Manager)

Before placing any bet, the bot checks:
- "Have I lost too much money today?" (Max $25 daily loss)
- "Have I lost too many times in a row?" (Max 4 losses in a row)
- "Have I made too many trades today?" (Max 30 per day)
- "Has my wallet dropped too much?" (Max 25% drawdown)
- "Do I already have 3 bets running?" (Max concurrent positions)

If any of these checks fail, the bot says "Nope, not trading right now!" and waits.

### Step 4: Calculate Bet Size (Kelly Criterion)

The bot uses the **Kelly Criterion** — a famous math formula that tells you the perfect amount to bet based on your edge and the odds. But to be safe, the bot only uses **half-Kelly** (50%), which means it bets half of what the math says is perfect. This is much safer!

Then it also checks:
- Is the bet size at least $5? (Minimum trade)
- Is the bet size at most $50? (Maximum position)
- If the Volatility Schedule is on: multiply the bet by the current intensity (e.g., 1.8x during US Market Open)

### Step 5: Place the Trade (The On-Chain Executor)

The bot:
1. Signs the order with your private key
2. Sends it to the Polymarket exchange
3. Waits for confirmation
4. Records the trade in its database

### Step 6: Monitor and Collect (Auto-Redeem)

Every 30 seconds, the bot checks:
- "Did any of my bets finish?"
- "Did I win? If so, let me collect the winnings!"
- "Am I losing badly on something? Should I cut my losses?"

---

## 🛡️ Safety Features

PolyBot has lots of safety features built in. Here they all are:

### Circuit Breakers (Automatic Pauses)

| Safety Feature | What Triggers It | What Happens |
|---|---|---|
| **Daily Loss Limit** | You lose $25 in one day | Bot stops trading for the rest of the day |
| **Consecutive Loss Streak** | You lose 4 times in a row | Bot takes a timeout (2-30 minutes) |
| **Daily Trade Limit** | You make 30 trades in one day | Bot stops trading for the rest of the day |
| **Drawdown Limit** | Your wallet drops 25% from its highest point | Bot stops trading until you manually reset |

### Smart Sizing (Automatic Adjustment)

The bot adjusts how much it bets based on its recent performance:

| Your Recent Performance | How Much It Bets |
|---|---|
| Won 3 or more in a row | 100% of Kelly size (full confidence!) |
| Won 1-2 in a row | 85% of Kelly size |
| No streak either way | 75% of Kelly size |
| Lost 1-2 in a row | 55% of Kelly size (getting careful) |
| Lost 3 or more in a row | 40% of Kelly size (very careful!) |

### The REDEEM_ONLY Emergency Stop

If something goes wrong and you want to stop ALL trading immediately:

1. Go to Railway → Variables
2. Set `REDEEM_ONLY=true`
3. The bot will:
   - ❌ Stop ALL new trades immediately
   - ✅ Keep collecting winnings from old trades
   - ✅ Keep running the Full Redeemer
   - ✅ Keep the dashboard working

### The DRY_RUN Safety Net

If you set `DRY_RUN=true`:
- The bot does everything it normally does (scanning, analyzing, calculating)
- But it **never actually places any trades**
- It just tells you "I WOULD have placed this trade"
- Great for testing and learning!

---

## 💻 Running It on Your Own Computer (For Testing)

You can run PolyBot on your own computer to test it. Here is how:

### Step 1: Install Everything

Open your terminal and type:

```bash
cd PolyBot
pip install -e ".[dev]"
```

> **What does this do?** It installs PolyBot and all the helper tools it needs (like testing frameworks).

### Step 2: Create Your Settings File

Copy the example settings file:

```bash
cp env.example .env
```

Then open `.env` in a text editor and fill in your values. The most important ones are `POLYGON_PRIVATE_KEY` and `WALLET_ADDRESS`.

### Step 3: Run the Bot

For a safe test run (no real money):

```bash
DRY_RUN=true python -m uvicorn polybot.main_fastapi:app --reload
```

> **What does this do?**
> - `DRY_RUN=true` means no real money
> - `python -m uvicorn polybot.main_fastapi:app` starts the bot
> - `--reload` means if you change any code, the bot restarts automatically

Then open your browser and go to `http://localhost:8000/dashboard` to see the dashboard!

### Using Docker (Alternative)

If you have Docker installed, you can also run:

```bash
docker-compose up
```

> **What does this do?** It starts the bot, a Redis database, and everything else in containers. Docker is like a little virtual computer inside your real computer.

---

## 🧪 Running Tests

Tests make sure everything is working correctly. To run them:

```bash
cd PolyBot
pip install -e ".[dev]"
python -m pytest tests/ -v --timeout=60
```

> **What does this do?**
> - `python -m pytest tests/` runs ALL the tests
> - `-v` means "verbose" — it shows you each test passing or failing
> - `--timeout=60` means "if a test takes more than 60 seconds, something is wrong, stop it"

You should see lots of lines that say `PASSED` in green. If you see `FAILED` in red, something might be wrong!

---

## 🌐 All the Web Pages and API Links

Once your bot is running, you can visit these URLs (replace `your-bot.railway.app` with your actual URL):

### Web Pages (Open in Browser)

| URL | What You See |
|---|---|
| `/dashboard` | The main dashboard with status, P&L, trades, positions |
| `/viz` | Pretty charts from the Optuna optimizer |
| `/monitor` | Real-time PnL chart and trade feed |
| `/logs` | Error log viewer |

### API Links (For Checking Data)

| URL | Method | What You Get |
|---|---|---|
| `/api/health` | GET | Quick "is the bot alive?" check. Returns `{"status": "ok"}` |
| `/api/status` | GET | Full bot status (mode, DRY_RUN, risk state, P&L, next scan countdown) |
| `/api/risk_status` | GET | Circuit breaker status, daily loss, consecutive losses, drawdown |
| `/api/positions` | GET | All currently open bets |
| `/api/pnl` | GET | Profit and loss summary (today and all-time) |
| `/api/trades` | GET | Last 100 trades |
| `/api/rpc-status` | GET | Blockchain connection health |
| `/api/rpc_health` | GET | Detailed RPC statistics |
| `/api/allowance_status` | GET | USDC balance and allowance status |
| `/api/next_scan` | GET | Countdown to next market scan |
| `/api/backtest-report` | GET | Backtest results |
| `/api/strategy-comparison` | GET | Compare different strategies |
| `/api/production-status` | GET | Production readiness checks |
| `/api/production-safety` | GET | Safety checks (wallet, RPC, allowance) |
| `/api/full_redeemer_status` | GET | Full Redeemer status |

### API Actions (Do Something)

| URL | Method | What It Does |
|---|---|---|
| `/api/force_full_redeem` | POST | Immediately collect all winnings |
| `/apply-best-params` | POST | Load the best parameters from optimization |
| `/api/trigger-backup` | POST | Backup optimization data |

---

## 🔧 Troubleshooting (When Things Go Wrong)

### "The bot is not making any trades!"

Check these things one at a time:

1. **Is `DRY_RUN` set to `false`?** If it's `true`, the bot won't place real trades.
2. **Is `AUTO_EXECUTE` set to `true`?** If it's `false`, the bot won't place trades automatically.
3. **Is `REDEEM_ONLY` set to `false`?** If it's `true`, the bot won't make new trades.
4. **Do you have enough USDC?** Check `/api/allowance_status` — you need at least $1 for trading.
5. **Are the circuit breakers triggered?** Check `/api/risk_status` — maybe the bot lost too much today and stopped.
6. **Is the market liquid enough?** The bot needs at least $200 of liquidity and $100 of volume.

### "The bot says 'low balance'!"

Your wallet needs USDC on the Polygon network. Send some USDC to your wallet address. You need at least $0.30 for the bot to start trading, but we recommend at least $20-50 for meaningful results.

### "I see errors about RPC!"

The bot talks to the Polygon blockchain through an "RPC endpoint." If it's having trouble:

1. **Get an Alchemy API key** — It's free and much more reliable.
2. Set `ALCHEMY_API_KEY` in Railway with your key.
3. Set `FORCE_ALCHEMY=true` to prioritize it.

### "How do I stop the bot safely?"

1. Set `REDEEM_ONLY=true` in Railway.
2. Wait for all open positions to finish and get collected.
3. Then you can turn off the service.

### "The bot keeps losing money!"

1. Set `DRY_RUN=true` to stop real trading immediately.
2. Check `/api/backtest-report` to see how the strategy has been performing.
3. Maybe try different `MIN_EV`, `KELLY_MULTIPLIER`, or `TARGET_SYMBOLS` settings.
4. Remember: even the best bot can have losing streaks. The circuit breakers are there to protect you!

---

## 🔄 Moving to a Fresh Copy

If you are having trouble with the git history (the "memory" of all past changes) and want to start fresh:

```bash
# Step 1: Go to your PolyBot folder
cd PolyBot

# Step 2: Run the migration script
./migrate_to_polybot2.sh

# Step 3: Go to the new folder
cd ../polybot2

# Step 4: Upload to GitHub
gh repo create polybot2 --private --source=. --push
```

> **What does this do?** It creates a brand new copy of the bot called "polybot2" with all the latest files but without any of the old history. Your original PolyBot folder stays exactly the same.

---

## ✨ Feature List

Here is everything PolyBot can do:

| Feature | Status | What It Means |
|---------|--------|---------------|
| 5-Minute Market Filter | ✅ Ready | Finds the best 5-minute Up/Down crypto games |
| EdgeEngine v3 | ✅ Ready | Uses math (log-normal model) to find profitable opportunities |
| SignalEngine | ✅ Ready | Watches Binance for order flow, liquidations, and price differences |
| Kelly Position Sizing | ✅ Ready | Smart bet sizing (bets more when more confident) |
| Circuit Breakers | ✅ Ready | Automatic safety stops (daily loss, drawdown, loss streaks) |
| Full Redeemer V89 | ✅ Ready | Collects ALL winnings automatically, even after restart |
| Startup Redeem V90 | ✅ Ready | Checks for uncollected winnings when the bot starts |
| Auto-Redeem Monitor | ✅ Ready | Checks every 30 seconds for new winnings to collect |
| Cut-Loss Monitor | ✅ Ready | Sells losing positions if they drop too much |
| Sniper Mode | ✅ Ready | Trades in the last 30 seconds of 5-minute games |
| Volatility Schedule | ✅ NEW! | Adjusts bet sizes based on time of day (busy vs quiet markets) |
| Backtester | ✅ Ready | Test strategies on historical data |
| Optuna Hyperopt | ✅ Ready | Automatically finds the best settings |
| Web Dashboard | ✅ Ready | Watch your bot in real-time at `/dashboard` |
| Docker Support | ✅ Ready | Run with `docker-compose up` |
| Railway Deployment | ✅ Ready | One-click cloud deployment |
| Adaptive Sizing | ✅ Ready | Automatically adjusts bets based on win/loss streaks |
| Smart RPC Manager | ✅ Ready | Picks the fastest blockchain connection automatically |
| USDC Auto-Approve | ✅ Ready | Handles Polymarket permissions automatically |
| REDEEM_ONLY Mode | ✅ Ready | Emergency stop that only collects winnings |
| DRY_RUN Mode | ✅ Ready | Safe testing without real money |

---

## 📝 Version History

| Version | What Changed |
|---------|-------------|
| **V2.0 + Volatility Schedule** | NEW: Time-aware trading intensity. The bot now bets bigger during US Market Open, London Open, and other busy periods, and bets smaller during quiet hours. Sniper mode also uses the volatility schedule. |
| **V90 Startup Redeem** | On restart, the bot scans your entire wallet for uncollected winnings. |
| **V89 Full Redeemer** | Independent on-chain scanner. Collects ALL winnings even if the bot forgot about them. |
| **V78 Cut-Loss Monitor** | Automatically watches for losing positions and cuts them. Auto-redeem every 30 seconds. |
| **Production Defaults** | `DRY_RUN=false`, `AUTO_EXECUTE=true` — the bot is ready for real trading out of the box. |
| **V3 Execution Fix** | Lowered minimum trade to $1.00 and minimum balance to $0.30. |

---

**Good luck, and happy trading!** 🎉💰

Remember: Start small, use `DRY_RUN=true` first, and never invest more than you can afford to lose! 🤗
