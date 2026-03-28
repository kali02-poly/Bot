# PolyBot Ferox — Udrir hen Valyrio

<div align="center">

<!-- 🌍 ENGOS -->
[![English](https://img.shields.io/badge/🇺🇸_English-README-blue?style=flat-square)](../README.md)
[![Español](https://img.shields.io/badge/🇪🇸_Español-Manual-red?style=flat-square)](MANUAL_ES.md)
[![Русский](https://img.shields.io/badge/🇷🇺_Русский-Руководство-blue?style=flat-square)](MANUAL_RU.md)
[![Polski](https://img.shields.io/badge/🇵🇱_Polski-Instrukcja-red?style=flat-square)](MANUAL_PL.md)
[![Français](https://img.shields.io/badge/🇫🇷_Français-Manuel-blue?style=flat-square)](MANUAL_FR.md)
[![العربية](https://img.shields.io/badge/🇸🇦_العربية-الدليل-green?style=flat-square)](MANUAL_AR.md)
[![中文](https://img.shields.io/badge/🇨🇳_中文-手册-red?style=flat-square)](MANUAL_ZH.md)
[![日本語](https://img.shields.io/badge/🇯🇵_日本語-マニュアル-white?style=flat-square)](MANUAL_JA.md)
[![tlhIngan](https://img.shields.io/badge/🖖_tlhIngan-ghItlh-red?style=flat-square)](MANUAL_KLINGON.md)
[![Sindarin](https://img.shields.io/badge/🧝_Sindarin-Teitho-green?style=flat-square)](MANUAL_SINDARIN.md)
[![Valyrian](https://img.shields.io/badge/🐉_Valyrian-Udrir-purple?style=flat-square)](MANUAL_VALYRIAN.md)

---

![PolyBot Banner](https://img.shields.io/badge/🤖_PolyBot-Ōdrikagon_Valyrio-blue?style=for-the-badge&labelColor=1a1a2e&color=4a90d9)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Polymarket](https://img.shields.io/badge/Polymarket-Ōdrikagon-purple?style=for-the-badge)

**🚀 Tōma-lēben Bēvilza/Gūrogon Crypto ōdrikagon bot — Polymarket**

*Ōdrikagon naejot • Ferox Dashboard keligon*

</div>

---

## 📖 Dāerves Ēngos

1. [Skorkydoso PolyBot issa?](#-skorkydoso-polybot-issa)
2. [Ropagon Brōzagon](#-ropagon-brozagon)
3. [Kesīr Prūmāzma](#-kesir-prumazma)
4. [Railway Prūmāzma](#-railway-prumazma)
5. [API Lenton](#-api-lenton)
6. [Ōdrikagon Mōris](#-odrikagon-moris)
7. [Gīmigon Qrinuntys](#-gimigon-qrinuntys)
8. [Rōvēgon Sȳz](#-rovegon-syz)

---

## 🎯 Skorkydoso PolyBot issa?

PolyBot Ferox **ōdrikagon bot sȳrior** issa — tōma-lēben Bēvilza/Gūrogon Crypto hen [Polymarket](https://polymarket.com).

### Nāpāstre Rȳbagon

| Ēngos | Gīmīle |
|-------|--------|
| 🤖 **Tōma-lēben Erinon** | Bēvilza iā Gūrogon (BTC, SOL, XRP, ETH) |
| 📊 **Pyramid Compounding** | 30% ōdrikagon vaoreznon |
| 📈 **Backtest** | 7 tubī gōntan erinon |
| ⏰ **Hourly Risk Regime** | Berlin tubis choH vaoreznon |
| 🎯 **SimpleTrendFilter** | Slope + StdDev daor |
| 🌐 **Ferox Dashboard** | Keligon naejot hen i gāmis |

---

## 📋 Ropagon Brōzagon

| Ropagon | Skoros | Kostilus |
|---------|--------|---------|
| 💳 Polygon kisalbar | Ōdrikagon ngoer | MetaMask iā mēre |
| 🚂 Railway brōzi | Backend arlī tubī | [railway.app](https://railway.app) |
| 🌐 Gāmis | Dashboard keligon | Gāmis ēlī |

---

## 🚀 Kesīr Prūmāzma

```bash
git clone https://github.com/AleisterMoltley/PolyBot.git && cd PolyBot
pip install -e .
uvicorn polybot.main_fastapi:app --host 0.0.0.0 --port 8000
```

Naejot http://localhost:8000 jemagon

---

## 🚂 Railway Prūmāzma

### Tōma 1: Brōzi Ēlī Sōvegon

1. Naejot [railway.app](https://railway.app) jemagon
2. **"New Project"** rȳbagon
3. **"Deploy from GitHub repo"** keligon
4. **"PolyBot"** ūndegon se keligon

### Tōma 2: Ēngos Brōzagon

| Ēngos | Gīmīle | Ropagon |
|-------|--------|---------|
| `POLYGON_PRIVATE_KEY` | Aōha Polygon mīsagon ēngos | ✅ Kessa |
| `DRY_RUN` | `true` — dōrī erinon | Iēdrosa |

### Tōma 3: Keligon

1. Rūsīr prūmāzma **kasta** ✅ gaomagon
2. Railway annon-palan camo
3. Dashboard — Railway annon-palan-iot issa!

---

## 🔌 API Lenton

| Lenton | Mōris | Gīmīle |
|--------|-------|--------|
| `/health` | GET | Gīmigon i-qrinuntys |
| `/api/status` | GET | Bot qrinuntys |
| `/api/balance` | GET | Kisalbar tepagon |
| `/api/scan` | GET | Ōñagon i-mazenka |
| `/api/trades` | GET | Ōdrikagon penrose |
| `/api/pnl` | GET | PnL tolī |
| `/api/risk` | GET | Qrinuntys kostōba |

---

## 🎯 Ōdrikagon Mōris

### Tinnol Ōdrikagon
```bash
MODE=signal
```

### Gūrogon Ōdrikagon
```bash
MODE=copy
COPY_WALLETS=wallet1,wallet2
```

### Athrabed Ōdrikagon
```bash
MODE=arbitrage
```

---

## 🛡️ Gīmigon Qrinuntys

| Dīnilūks | Gīmīle |
|-----------|--------|
| **Tubis Rōvēgon** | Daorun vaoreznon -5% |
| **Circuit Breaker** | Hēnkirī hāre caul |
| **Kelly Sizing** | Sȳrior ōdrikagon mēre |

---

## 🔧 Rōvēgon Sȳz

| Qrinuntys | Sȳrior |
|-----------|--------|
| Bot daor ivestragon | Railway ēngos tirion |
| Ōdrikagon daor | `DRY_RUN=false` se kisalbar keligon |
| Tepagon 0 sagon | USDC hen Polygon kisalbar ropagon |

---

## 📜 Dāerves

MIT

---

**Valar morghulis! Yn kesrio syt iksis! 🐉🚀**
