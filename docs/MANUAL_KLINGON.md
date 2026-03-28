# PolyBot Ferox — tlhIngan Hol ghItlh

<div align="center">

<!-- 🌍 Holmey -->
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

![PolyBot Banner](https://img.shields.io/badge/🤖_PolyBot-mIw_automatlh-blue?style=for-the-badge&labelColor=1a1a2e&color=4a90d9)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Polymarket](https://img.shields.io/badge/Polymarket-mIw-purple?style=for-the-badge)

**🚀 vagh tup Dung/bIng Crypto mIw bot — Polymarket**

*automatlh naQ • Ferox Dashboard SeH*

</div>

---

## 📖 De'wI' tetlh

1. [nuq 'oH PolyBot'e'?](#-nuq-oh-polybote)
2. [nIb poQlu'bogh](#-nib-poqlubogh)
3. [naDev ngevwI' cher](#-nadev-ngevwi-cher)
4. [Railway yotlh cher](#-railway-yotlh-cher)
5. [API Endpoints](#-api-endpoints)
6. [mIw Segh](#-miw-segh)
7. [QIH SeH](#-qih-seh)
8. [Qagh lughmoH](#-qagh-lughmoh)

---

## 🎯 nuq 'oH PolyBot'e'?

PolyBot Ferox — **po'wI' mIw bot** ghaH. vagh tup Dung/bIng Crypto wanI'mey [Polymarket](https://polymarket.com)-Daq mIw ta'.

### nap Dochmey

| Doch | 'oS |
|------|-----|
| 🤖 **vagh tup neH** | Dung pagh bIng wanI'mey (BTC, SOL, XRP, ETH) |
| 📊 **Pyramid Compounding** | 30% ngeH automatlh |
| 📈 **Backtest** | 7 jaj ngaQ neH |
| ⏰ **Hourly Risk Regime** | Berlin rep choH automatlh |
| 🎯 **SimpleTrendFilter** | Slope + StdDev wIv |
| 🌐 **Ferox Dashboard** | naQ SeH De'wI'vo' |

---

## 📋 nIb poQlu'bogh

| poQ | meq | nuqDaq Suq |
|-----|-----|------------|
| 💳 Polygon bIQ'a' | mIw ngoD | MetaMask pagh latlh |
| 🚂 Railway mI' | Backend Hoch jaj Hoch ram | [railway.app](https://railway.app) |
| 🌐 De'wI' | Dashboard 'el | De'wI' chu' |

---

## 🚀 naDev ngevwI' cher

```bash
git clone https://github.com/AleisterMoltley/PolyBot.git && cd PolyBot
pip install -e .
uvicorn polybot.main_fastapi:app --host 0.0.0.0 --port 8000
```

http://localhost:8000 yIpoQ

---

## 🚂 Railway yotlh cher

### mIw 1: ngoH chu' chenmoH

1. [railway.app](https://railway.app) yIghoS
2. **"New Project"** yIchel
3. **"Deploy from GitHub repo"** yIwIv
4. **"PolyBot"** yISam 'ej yIwIv

### mIw 2: yotlh ngutlh

| ngutlh | 'oS | poQlu' |
|--------|-----|--------|
| `POLYGON_PRIVATE_KEY` | Polygon pegh ngutlh | ✅ HIja' |
| `DRY_RUN` | `true` — ngoD neH | chup |

### mIw 3: chov

1. yotlh **SuD** ✅ yIloS
2. Railway URL yIchelmoH
3. Dashboard — Railway URL-Daq tu'lu'!

---

## 🔌 API Endpoints

| Endpoint | mIw | 'oS |
|----------|-----|-----|
| `/health` | GET | DotlhIj yIchov |
| `/api/status` | GET | bot Dotlh |
| `/api/balance` | GET | bIQ'a' Huch |
| `/api/scan` | GET | Soj yISuq |
| `/api/trades` | GET | mIw qun |
| `/api/pnl` | GET | PnL De' |
| `/api/risk` | GET | QIH Dotlh |

---

## 🎯 mIw Segh

### Signal mIw
```bash
MODE=signal
```

### Copy mIw
```bash
MODE=copy
COPY_WALLETS=wallet1,wallet2
```

### Arbitrage mIw
```bash
MODE=arbitrage
```

---

## 🛡️ QIH SeH

| Hub | 'oS |
|-----|-----|
| **jaj vuS** | -5% automatlh mev |
| **Circuit Breaker** | wej luj — yIloS |
| **Kelly Sizing** | nIv mIw 'ab |

---

## 🔧 Qagh lughmoH

| Qagh | lughmoH |
|------|---------|
| bot jang Qo' | Railway logs yIlaD |
| mIw ta' Qo' | `DRY_RUN=false` 'ej bIQ'a' yIchov |
| Huch 0 'ang | Polygon bIQ'a'Daq USDC DaghajnIS |

---

## 📜 chut

MIT

---

**Qapla'! 🚀**
