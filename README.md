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
Cython C extensions. Available via [PyPI](https://pypi.org/project/unicorn-binance-suite/) and 
[Anaconda](https://anaconda.org/conda-forge/unicorn-binance-suite).

```
pip install unicorn-binance-suite
```

**2.8 M+ PyPI downloads** | **980+ GitHub stars** | **388+ dependent projects** | Python 3.9 -- 3.14

---

## Why UNICORN Binance Suite — the honest comparison

|                                                                                                                                                                                                  | **UBS** | **python-binance** | **ccxt / ccxt.pro** | **binance-connector-python** |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|---|
| **Binance focus**                                                                                                                                                                                | Specialist. Knows every quirk (Spot, Margin, Futures, COIN-M, Options, US, TR, Testnets) | Binance-only, but shallower | Generalist for 100+ exchanges — Binance is *one of many* | Official, but only a *"simple connector"* (Binance's own words) |
| **WebSocket reconnect**                                                                                                                                                                          | Automatic, unlimited, battle-tested, logged | Hard-coded **max. 5 retries**, then `BinanceUnableToConnect` and you're done | [Silently hangs without exception](https://github.com/ccxt/ccxt/issues/22662) after ~12h, no heartbeat | DIY — build it yourself |
| **DepthCache sync detection**                                                                                                                                                                    | `is_depth_cache_synchronized()` + `DepthCacheOutOfSync` exception + auto re-init in seconds | Returns `None`, instance dead: *"this instance of the DepthCacheManager will not be able to be used again"* | See silent-hang bug above | No DepthCache, no sync |
| **[Orphan level cleanup (>1000)](https://blog.technopathy.club/your-binance-order-book-is-wrong-here-s-why)**                                                                                    | Implemented — strictly follows Binance spec | No — delivers inconsistent books | No | N/A |
| **DepthCache refresh**                                                                                                                                                                           | Event-driven, same asyncio loop as the stream | **REST polling every 30 min** (default) — not truly "live local" | Cache via Pro license | Not available |
| **DepthCache cluster**                                                                                                                                                                           | **UBDCC** — horizontally scalable, load balancing, failover, REST API | — | — | — |
| **Trailing stop loss**                                                                                                                                                                           | **UBTSL** as SDK + CLI, incl. `jump-in-and-trail` | Not included | Not included | Not included |
| **Performance**                                                                                                                                                                                  | Cython C extensions, PyPy wheels, pre-compiled | Pure Python, no C | Pure Python — [reported performance issues](https://github.com/ccxt/ccxt/issues/25152) with many symbols | Pure Python |
| **Multi-arch wheels**                                                                                                                                                                            | x86_64, aarch64, arm64, PyPy | Mostly x86_64 | Pure Python | Pure Python |
| **Python support**                                                                                                                                                                               | 3.9 – 3.14 | 3.8+ | 3.9+ | 3.9+ |
| **[Stream signals](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/%60stream_signals%60)**                                                                            | `CONNECT`, `FIRST_RECEIVED_DATA`, `DISCONNECT`, `STOP`, `STREAM_UNREPAIRABLE` — know the exact state of every stream | No | No | No |
| **Runtime [subscribe/unsubscribe](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api?tab=readme-ov-file#subscribe--unsubscribe-new-markets-and-channels) without disconnect** | Yes | No — stop & restart the stream | Partially | No |
| **Multiple private UserData streams**                                                                                                                                                            | Yes — different API keys in one Manager | One stream per connection | One exchange instance | One stream per connection |
| **UserData stream handling**                                                                                                                                                                     | Automatic, listenKey refresh transparent | Manual | Partially abstracted | Manual |
| **[WebSocket API](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html#module-unicorn_binance_websocket_api.api) (order placement via WS)**   | Yes — Spot and Futures, managed connection | No | Partially | Raw access, no reconnect handling |
| **Asyncio**                                                                                                                                                                                      | Native asyncio under the hood, but **no async boilerplate required** — works out of the box with sync code | Threads + callbacks | Async-first, requires `await` everywhere | Sync and async variants, but separate packages |
| **Package structure**                                                                                                                                                                            | One monolith `unicorn-binance-suite` or modular | One package | One huge package (100+ exchanges) | **Recently split** into `binance-sdk-spot`, `binance-sdk-derivatives-trading-usds-futures`, etc. — migration guide required |
| **License**                                                                                                                                                                                      | MIT | MIT | MIT (ccxt), **ccxt.pro = commercial** | MIT |
| **Maintainer**                                                                                                                                                                                   | Active, reachable by name | Original author abandoned in 2022 — community-maintained fork with sporadic releases | Commercial entity, enterprise-first | Auto-generated SDK, Binance team |

---

### python-binance: reconnect limitations

Original author abandoned the project in 2022. Community fork ships sporadic patches, but the fundamental architecture 
is unchanged: max. 5 reconnect retries, then dead. `DepthCacheManager` permanently unusable after a missed 
reconnect — restart your process, lose your state. Default 30-minute REST polling means you're trading on a stale 
book between refreshes. No Cython, no multi-arch wheels, no cluster story.

### ccxt: silent disconnect on watch_order_book

`watch_order_book` [hangs silently after ~12h](https://github.com/ccxt/ccxt/issues/22662) — no exception, no 
reconnect, your bot just stops. Open since May 2024. Generalist architecture means you pay the abstraction tax for 
100+ exchanges you'll never use. Order book caching requires a commercial ccxt.pro license.

### binance-connector-python: minimal by design

Official ≠ production. No reconnect, no UserDataStream refresh, no DepthCache, no trailing stop. Recently fragmented 
into 5+ packages (`binance-sdk-spot`, `binance-sdk-derivatives-trading-usds-futures`, ...) — existing code needs 
migration.

---

## In short

> **UBS is what comes out when someone trades on Binance daily since 2019 and has eaten every edge case himself — 
> including bugs in Binance's own spec.**

---

## Architecture

```
         ┌────────────────────────────────────────────────┐
         │            Your Trading Application            │
         └──────┬────────────────┬───────────┬────────────┘
                │                │           │
       ┌────────▼───────┐  ┌─────▼───┐  ┌────▼───────────────┐
       │  UBLDC / UBDCC │  │  UBTSL  │  │  Direct UBWA/UBRA  │
       │  (Order Books) │  │  (Stop  │  │  access for custom │
       │                │  │   Loss) │  │  strategies        │
       └───────┬────────┘  └──┬──┬───┘  └──────┬─────────────┘
               │              │  │             │
         ┌─────▼──────────────▼──▼─────────────▼────────────┐
         │                  UnicornFy                       │
         │          (raw data → Python dicts)               │
         └────────────────┬─────────────────┬───────────────┘
                          │                 │
                ┌─────────▼───┐     ┌───────▼───────┐
                │    UBWA     │     │     UBRA      │
                │ (WebSocket) │     │    (REST)     │
                └──────┬──────┘     └───────┬───────┘
                       │                    │
                ┌──────▼────────────────────▼──────┐
                │          Binance API             │
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
way to access current order book depth without exceeding Binance rate limits. Supports Spot, Futures, 
**European Options (Vanilla Options)**, US and TR. Manages multiple depth caches per instance in asyncio coroutines.

**220K+ downloads** | **49 stars**

### [UNICORN Binance DepthCache Cluster](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) (UBDCC)
Production-scale depth cache management with load balancing, automatic failover and self-healing state. 
[Runs locally on a single machine (`pip install ubdcc`)](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#local-setup-without-kubernetes) 
or [scales across a Kubernetes cluster](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#kubernetes-setup). 
[REST API](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#rest-api) 
accessible from any programming language.

### [UNICORN Binance Trailing Stop Loss](https://github.com/oliver-zehentleitner/unicorn-binance-trailing-stop-loss) (UBTSL)
Trailing stop loss engine with smart entry (`jump-in-and-trail`). Available as Python SDK and 
[CLI tool](https://github.com/oliver-zehentleitner/unicorn-binance-trailing-stop-loss/tree/master/cli). 
Supports email notifications.

**101K+ downloads** | **27 stars**

### [UnicornFy](https://github.com/oliver-zehentleitner/unicorn-fy)
Normalization layer that converts raw exchange API payloads into well-formed Python dictionaries. Used internally by 
all suite modules.

**685K+ downloads** | **56 stars**

---

## Common Use Cases

### Stream trades via WebSocket
```python
# use case: receive real-time trade events
# module: unicorn-binance-websocket-api (UBWA)
from unicorn_binance_websocket_api import BinanceWebSocketApiManager

ubwa = BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(channels="trade", markets="btcusdt", process_stream_data=lambda data: print(data))
```
[UBWA docs](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api) — manages reconnect, sequence validation and stream lifecycle automatically.

### Maintain a local order book
```python
# use case: synchronized local depth cache with real-time updates
# module: unicorn-binance-local-depth-cache (UBLDC)
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync

ubldc = BinanceLocalDepthCacheManager(exchange="binance.com")
ubldc.create_depthcache("BTCUSDT")
try:
    asks = ubldc.get_asks("BTCUSDT", limit_count=10)
    bids = ubldc.get_bids("BTCUSDT", limit_count=10)
except DepthCacheOutOfSync:
    pass  # cache is re-syncing automatically
```
[UBLDC docs](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache) — event-driven sync, auto re-init on gaps, orphan level cleanup.

### Place an order via REST
```python
# use case: place a market order on Binance Spot
# module: unicorn-binance-rest-api (UBRA)
from unicorn_binance_rest_api import BinanceRestApiManager

with BinanceRestApiManager(api_key="...", api_secret="...") as ubra:
    order = ubra.create_order(symbol="BTCUSDT", side="BUY", type="MARKET", quoteOrderQty=100)
```
[UBRA docs](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api) — full Binance REST coverage (Spot, Margin, Futures, US, TR).

### Trail a stop loss
```python
# use case: automated trailing stop loss with notification
# module: unicorn-binance-trailing-stop-loss (UBTSL)
from unicorn_binance_trailing_stop_loss import BinanceTrailingStopLossManager

ubtsl = BinanceTrailingStopLossManager(exchange="binance.com", market="BTCUSDT",
                                       stop_loss_limit="1.5%", stop_loss_order_type="LIMIT",
                                       api_key="...", api_secret="...")
```
Also available as a CLI: `ubtsl --profile BTCUSDT_SELL --stoplosslimit 0.5%`

[UBTSL docs](https://oliver-zehentleitner.github.io/unicorn-binance-trailing-stop-loss) — SDK + CLI, smart entry (`jump-in-and-trail`), email notifications.

### Run a DepthCache cluster
```python
# use case: production-scale order books with failover
# module: unicorn-binance-local-depth-cache (UBLDC) + ubdcc
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager

with BinanceLocalDepthCacheManager(exchange="binance.com", ubdcc_address="127.0.0.1") as ubldc:
    ubldc.cluster.create_depthcaches(exchange="binance.com", markets=["BTCUSDT", "ETHUSDT"])
    asks = ubldc.cluster.get_asks(exchange="binance.com", market="BTCUSDT")
```
[Runs locally](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#local-setup-without-kubernetes)
(`pip install ubdcc && ubdcc start`) or on a
[Kubernetes cluster](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#kubernetes-setup).
[REST API](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster?tab=readme-ov-file#rest-api) accessible from any language.

### Canonical example — stream + local order book
```python
# purpose: the most common UBS pattern — stream market data and maintain a local order book
# modules: UBWA (WebSocket) + UBLDC (Depth Cache)
# install: pip install unicorn-binance-suite
from unicorn_binance_local_depth_cache import BinanceLocalDepthCacheManager, DepthCacheOutOfSync
import time

with BinanceLocalDepthCacheManager(exchange="binance.com") as ubldc:
    ubldc.create_depthcache("BTCUSDT")
    while True:
        try:
            best_ask = ubldc.get_asks("BTCUSDT", limit_count=1)
            best_bid = ubldc.get_bids("BTCUSDT", limit_count=1)
            print(f"Best ask: {best_ask}, Best bid: {best_bid}")
        except DepthCacheOutOfSync:
            print("DepthCache is re-syncing...")
        time.sleep(1)
```

### Install everything at once
```
pip install unicorn-binance-suite
```

---

## Installation

Python 3.9+ required. Runs smoothly up to and including Python 3.14.

### pip
```
pip install unicorn-binance-suite
```

### conda
```
conda install -c conda-forge unicorn-binance-suite
```

### Or install individual modules
```
pip install unicorn-binance-websocket-api
pip install unicorn-binance-rest-api
pip install unicorn-binance-local-depth-cache
pip install unicorn-binance-trailing-stop-loss
pip install unicorn-fy
pip install ubdcc
```

PyPy interpreter supported from Python 3.9+.

All packages are built transparently via GitHub Actions and published directly to 
[PyPI](https://pypi.org/project/unicorn-binance-suite/) and 
[conda-forge](https://anaconda.org/conda-forge/unicorn-binance-suite) -- the entire pipeline from source to wheel 
is traceable.

---

## Documentation

| Module | Docs |
|--------|------|
| Suite (this package) | [oliver-zehentleitner.github.io/unicorn-binance-suite](https://oliver-zehentleitner.github.io/unicorn-binance-suite) |
| UBWA (WebSocket) | [oliver-zehentleitner.github.io/unicorn-binance-websocket-api](https://oliver-zehentleitner.github.io/unicorn-binance-websocket-api) |
| UBRA (REST) | [oliver-zehentleitner.github.io/unicorn-binance-rest-api](https://oliver-zehentleitner.github.io/unicorn-binance-rest-api) |
| UBLDC (Depth Cache) | [oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache](https://oliver-zehentleitner.github.io/unicorn-binance-local-depth-cache) |
| UBDCC (Depth Cache Cluster) | [oliver-zehentleitner.github.io/unicorn-binance-depth-cache-cluster](https://oliver-zehentleitner.github.io/unicorn-binance-depth-cache-cluster) |
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

## AI Integration

This project provides [`llms.txt`](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-suite/refs/heads/master/llms.txt) files for AI tools (ChatGPT, Claude, Copilot, etc.). The 
[suite-level llms.txt](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-suite/refs/heads/master/llms.txt) routes use cases to the correct module. Each module also has its own `llms.txt` with 
detailed API reference and code examples.

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
