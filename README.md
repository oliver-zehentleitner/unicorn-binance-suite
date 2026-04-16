[![GitHub Release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-binance-suite.svg?label=github)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/oliver-zehentleitner/unicorn-binance-suite/total?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-suite?color=blue)](https://pypi.org/project/unicorn-binance-suite/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-suite)](https://pepy.tech/project/unicorn-binance-suite)
[![License](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-binance-suite.svg?color=blue)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/blob/master/LICENSE)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_suite.svg)](https://www.python.org/downloads/)
[![Unit Tests](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/actions/workflows/build_wheels.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://oliver-zehentleitner.github.io/unicorn-binance-suite/)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)

# UNICORN Binance Suite

**The production-grade Python toolkit for Binance.** WebSocket streams, REST API, local order books, trailing stop 
losses and cluster-scale depth caches -- all coordinated, fully documented, MIT-licensed and delivered as optimized 
Cython C extensions.

```
pip install unicorn-binance-suite
```

**2.8 M+ PyPI downloads** | **980+ GitHub stars** | **388+ dependent projects** | Python 3.9 -- 3.14

---

## Why UNICORN Binance Suite?

| | UBS | Typical alternative |
|---|---|---|
| **Reconnect handling** | Automatic, battle-tested, logged | DIY or best-effort |
| **Multi-arch wheels** | x86_64, aarch64, arm64 + PyPy | Often x86_64 only |
| **Cython optimized** | Yes, transparent GH Actions build | Rarely |
| **Cluster solution** | UBDCC (Kubernetes-native) | No equivalent |
| **Test suite** | Comprehensive, CI on 3.9-3.14 | Often minimal |
| **Maintainer** | Active, responsive, named | Varies |

> *"You could write this yourself. We already did, battle-tested it with 2.8M+ downloads, and fixed bugs 
> in Binance's own specification along the way."*

---

## Architecture

```
                           ┌─────────────────────────────────────────────────┐
                           │            Your Trading Application             │
                           └──────┬──────────┬───────────┬──────────────────┘
                                  │          │           │
                    ┌─────────────▼──┐  ┌────▼────┐  ┌──▼──────────────────┐
                    │  UBLDC / UBDCC │  │  UBTSL  │  │  Direct UBWA/UBRA  │
                    │  (Order Books) │  │  (Stop  │  │  access for custom │
                    │                │  │   Loss) │  │  strategies        │
                    └───────┬────────┘  └──┬──┬───┘  └──────┬─────────────┘
                            │              │  │             │
                   ┌────────▼──────────────▼──▼─────────────▼──────────┐
                   │                  UnicornFy                        │
                   │          (raw data → Python dicts)                │
                   └────────────────┬─────────────────┬───────────────┘
                                    │                 │
                          ┌─────────▼───┐     ┌───────▼───────┐
                          │    UBWA     │     │     UBRA      │
                          │ (WebSocket) │     │    (REST)     │
                          └──────┬──────┘     └───────┬───────┘
                                 │                    │
                          ┌──────▼────────────────────▼──────┐
                          │          Binance API              │
                          └──────────────────────────────────┘
```

---

## Modules

### [UNICORN Binance WebSocket API](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api) (UBWA)
Real-time market data and user data streams with automatic reconnect, sequence validation, native asyncio queues and 
runtime subscribe/unsubscribe without disconnecting. Supports all Binance endpoints including Spot, Margin, Futures, 
Coin-Futures, US and TR.

**1.1M+ downloads** | **727 stars**

### [UNICORN Binance REST API](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) (UBRA)
Full coverage of Binance REST endpoints for account management, order placement and market data queries. Spot, Margin, 
Isolated Margin, Futures, US and TR -- all with testnet support.

**663K+ downloads** | **67 stars**

### [UNICORN Binance Local Depth Cache](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) (UBLDC)
Synchronized local order books with real-time WebSocket updates and automatic re-initialization on gaps. The fastest 
way to access current order book depth without exceeding Binance rate limits. Manages multiple depth caches per 
instance in asyncio coroutines.

**220K+ downloads** | **49 stars**

### [UNICORN Binance DepthCache Cluster](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) (UBDCC)
Kubernetes-native cluster for production-scale depth cache management. Load balancing, automatic failover and 
self-healing state. Runs locally on a single machine or scales across a K8s cluster. REST API accessible from any 
programming language.

### [UNICORN Binance Trailing Stop Loss](https://github.com/oliver-zehentleitner/unicorn-binance-trailing-stop-loss) (UBTSL)
Trailing stop loss engine with smart entry (`jump-in-and-trail`). Available as Python SDK and 
[CLI tool](https://github.com/oliver-zehentleitner/unicorn-binance-trailing-stop-loss/tree/master/cli). 
Supports email and Telegram notifications.

**101K+ downloads** | **27 stars**

### [UnicornFy](https://github.com/oliver-zehentleitner/unicorn-fy)
Normalization layer that converts raw exchange API payloads into well-formed Python dictionaries. Used internally by 
all suite modules.

**685K+ downloads** | **56 stars**

---

## Quick Start

### WebSocket stream in 4 lines
```python
from unicorn_binance_websocket_api import BinanceWebSocketApiManager

ubwa = BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(channels="trade", markets="btcusdt", process_stream_data=lambda data: print(data))
```

### Local order book in 3 lines
```python
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager

ubldc = BinanceLocalDepthCacheManager(exchange="binance.com")
ubldc.create_depthcache("BTCUSDT")
```

### Trailing stop loss via CLI
```sh
$ pip install unicorn-binance-trailing-stop-loss
$ ubtsl --profile BTCUSDT_SELL --stoplosslimit 0.5%
```

### Install everything at once
```
pip install unicorn-binance-suite
```

---

## Installation

Python 3.9+ required. Runs smoothly up to and including Python 3.14.

```
pip install unicorn-binance-suite
```

Or install individual modules:
```
pip install unicorn-binance-websocket-api
pip install unicorn-binance-rest-api
pip install unicorn-binance-local-depth-cache
pip install unicorn-binance-trailing-stop-loss
pip install unicorn-fy
```

PyPy interpreter supported from Python 3.9+.

All packages are built transparently via GitHub Actions and published directly to 
[PyPI](https://pypi.org/project/unicorn-binance-suite/) -- the entire pipeline from source to wheel is traceable.

---

## Documentation

| Module | Docs |
|--------|------|
| Suite (this package) | [oliver-zehentleitner.github.io/unicorn-binance-suite](https://oliver-zehentleitner.github.io/unicorn-binance-suite) |
| UBWA (WebSocket) | [oliver-zehentleitner.github.io/unicorn-binance-websocket-api](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api) |
| UBRA (REST) | [oliver-zehentleitner.github.io/unicorn-binance-rest-api](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api) |
| UBLDC (Depth Cache) | [oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache) |
| UBTSL (Trailing Stop) | [oliver-zehentleitner.github.io/unicorn-binance-trailing-stop-loss](https://oliver-zehentleitner.github.io/unicorn-binance-trailing-stop-loss) |
| UnicornFy | [oliver-zehentleitner.github.io/unicorn-fy](https://oliver-zehentleitner.github.io/unicorn-fy) |

---

## Community

- [Telegram](https://t.me/unicorndevs) -- questions, announcements, chat
- [GitHub Discussions](https://github.com/oliver-zehentleitner/unicorn-binance-suite/discussions) -- longer-form Q&A
- [Issue Tracker](https://github.com/oliver-zehentleitner/unicorn-binance-suite/issues) -- bugs and feature requests

Binance API news:
[Announcements](https://t.me/binance_api_announcements) |
[English](https://t.me/binance_api_english) |
[Binance US](https://t.me/Binance_USA)

---

## Contributing

Contributions are welcome -- from documentation fixes to new features. Each module has its own repository; 
check the [CONTRIBUTING.md](https://github.com/oliver-zehentleitner/unicorn-binance-suite/blob/master/CONTRIBUTING.md) 
for guidelines.

[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-suite)](https://github.com/oliver-zehentleitner/unicorn-binance-suite/graphs/contributors)

---

## Disclaimer

This project is for informational purposes only. Nothing contained herein constitutes financial advice or a 
solicitation to buy or sell securities.

**If you intend to use real money, use it at your own risk.**

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or 
liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

### SOCKS5 Proxy / Geoblocking
US citizens are exclusively authorized to trade on Binance.US -- this restriction must not be circumvented.
SOCKS5 proxy support exists for non-US citizens accessing US services (e.g. CI runners blocked by Binance.com) and 
for legitimate market data analysis.
