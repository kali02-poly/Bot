# PolyBot Ferox — Teitho en-Edhellen

<div align="center">

<!-- 🌍 LAMMATH -->
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

![PolyBot Banner](https://img.shields.io/badge/🤖_PolyBot-Maenas_Autorín-blue?style=for-the-badge&labelColor=1a1a2e&color=4a90d9)
![Python](https://img.shields.io/badge/Python-3.11+-green?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Polymarket](https://img.shields.io/badge/Polymarket-Maenas-purple?style=for-the-badge)

**🚀 Leven-lheben Amrûn/Annûn Crypto maenas bot — Polymarket**

*Autorín naeg • Ferox Dashboard tíriel*

</div>

---

## 📖 Têw Gonodrim

1. [Man PolyBot?](#-man-polybot)
2. [I Sennas Erui](#-i-sennas-erui)
3. [Estolad Sí](#-estolad-si)
4. [Railway Estolad](#-railway-estolad)
5. [API Annon-ethir](#-api-annon-ethir)
6. [Maenas Herth](#-maenas-herth)
7. [Gostadh Baugladh](#-gostadh-baugladh)
8. [Athradad Angol](#-athradad-angol)

---

## 🎯 Man PolyBot?

PolyBot Ferox na **maenas bot harn** an leven-lheben Amrûn/Annûn Crypto gwanûr mi [Polymarket](https://polymarket.com).

### Niphredil i-Naergon

| Dôr | Pediad |
|-----|--------|
| 🤖 **Leven-lheben Eraid** | Amrûn egor Annûn gwanûr (BTC, SOL, XRP, ETH) |
| 📊 **Pyramid Compounding** | 30% ath-nod autorín |
| 📈 **Backtest** | 7 aur goenol eraid |
| ⏰ **Hourly Risk Regime** | Estolad autorín ned aur Berlin |
| 🎯 **SimpleTrendFilter** | Slope + StdDev peniad |
| 🌐 **Ferox Dashboard** | Tíriad naeg o i-gammad |

---

## 📋 I Sennas Erui

| Sennas | Aníra | Mas |
|--------|-------|-----|
| 💳 Polygon solch | An maenas ngoer | MetaMask egor lain |
| 🚂 Railway herth | Backend ilaurui | [railway.app](https://railway.app) |
| 🌐 Gammad | Dashboard tiriad | Gammad eden |

---

## 🚀 Estolad Sí

```bash
git clone https://github.com/AleisterMoltley/PolyBot.git && cd PolyBot
pip install -e .
uvicorn polybot.main_fastapi:app --host 0.0.0.0 --port 8000
```

Pado na http://localhost:8000

---

## 🚂 Railway Estolad

### Tâd 1: Herth Eden Crear

1. Meno na [railway.app](https://railway.app)
2. Tego **"New Project"**
3. Ciro **"Deploy from GitHub repo"**
4. Celio a ciro **"PolyBot"**

### Tâd 2: Cirth Estolad

| Cirth | Pediad | Sennas |
|-------|--------|--------|
| `POLYGON_PRIVATE_KEY` | I thinnas pen-lín Polygon | ✅ Mae |
| `DRY_RUN` | `true` an ceredir | Anglennol |

### Tâd 3: Tiriad

1. Dartha an i estolad na **calen** ✅
2. Camo i Railway annon-palan
3. I Dashboard na sí ned Railway annon-palan!

---

## 🔌 API Annon-ethir

| Annon-ethir | Herth | Pediad |
|-------------|-------|--------|
| `/health` | GET | Tiriad i-lhaw |
| `/api/status` | GET | Bot lhaw |
| `/api/balance` | GET | Solch mirian |
| `/api/scan` | GET | Cened i-vachad |
| `/api/trades` | GET | Maenas pennas |
| `/api/pnl` | GET | PnL gwaith |
| `/api/risk` | GET | Baugladh lhaw |

---

## 🎯 Maenas Herth

### Tinnol Maenas
```bash
MODE=signal
```

### Aphad Maenas
```bash
MODE=copy
COPY_WALLETS=wallet1,wallet2
```

### Athrabed Maenas
```bash
MODE=arbitrage
```

---

## 🛡️ Gostadh Baugladh

| Dínen | Pediad |
|-------|--------|
| **Aur Lanc** | Daro autorín ned -5% |
| **Circuit Breaker** | Pautha ui neled caul |
| **Kelly Sizing** | And-veren maenas |

---

## 🔧 Athradad Angol

| Angol | Athradad |
|-------|----------|
| Bot ú-bêd | Tiriad Railway cirth |
| Maenas ú-car | Tiriad `DRY_RUN=false` a solch |
| Mirian 0 tíra | USDC ned Polygon solch boe |

---

## 📜 Gonad

MIT

---

**Na 'lass lín! 🚀**
