# AGENTS.md — UNICORN Binance Suite

> **End-user cheatsheet for AI-assisted consumption:** [`llms.txt`](llms.txt) — use that one if you're writing code *against* the suite.
> **This file** is for AI agents working *on* the suite repos themselves.

## Planning & Backlog

Suite-wide tasks and decisions are tracked in **[TASKS.md](TASKS.md)**. Per-module tasks live in the respective module repo's `TASKS.md`.

---

## Project Overview

`unicorn-binance-suite` is the **meta-package** (pure-Python, noarch) that pulls in the entire UNICORN Binance Suite as a single install. It has no source code of its own — it just pins and composes the six suite modules.

**Current Version:** 2.1.0
**Python Compatibility:** 3.9 – 3.14
**Author:** Oliver Zehentleitner
**PyPI:** `unicorn-binance-suite`
**conda-forge:** `unicorn-binance-suite`
**License:** MIT

---

## Suite modules (installed transitively)

| Module | Purpose | Repo | Abbrev. |
|---|---|---|---|
| [unicorn-fy](https://github.com/oliver-zehentleitner/unicorn-fy) | Normalize raw Binance JSON into typed Python dicts | `unicorn-fy` | UnicornFy |
| [unicorn-binance-rest-api](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) | Full-coverage Python SDK for all Binance REST endpoints | `unicorn-binance-rest-api` | UBRA |
| [unicorn-binance-websocket-api](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api) | Real-time market + user data streams with auto-reconnect | `unicorn-binance-websocket-api` | UBWA |
| [unicorn-binance-local-depth-cache](https://github.com/oliver-zehentleitner/unicorn-binance-local-depth-cache) | Synchronized local order books | `unicorn-binance-local-depth-cache` | UBLDC |
| [unicorn-binance-trailing-stop-loss](https://github.com/oliver-zehentleitner/unicorn-binance-trailing-stop-loss) | Trailing stop loss engine (SDK + CLI) | `unicorn-binance-trailing-stop-loss` | UBTSL |
| [unicorn-binance-depth-cache-cluster](https://github.com/oliver-zehentleitner/unicorn-binance-depth-cache-cluster) | Distributed depth cache cluster (K8s/local) | `ubdcc` | UBDCC |

---

## Directory Structure

```
unicorn_binance_suite/    # Stub package (no real code — just the meta install shim)
unittest_binance_suite.py # Smoke tests: verify all modules import after install
images/                   # Suite-wide banner, logos
tools/                    # get_versions_of_unicorn_packages.py etc.
docs/                     # Sphinx HTML output
dev/sphinx/               # Sphinx source
```

---

## Dependencies

Managed in `requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml` and `meta.yaml` — **all five must be kept in sync manually**, with `setup.py` as source of truth.

Current pins (see [CHANGELOG.md](CHANGELOG.md) for the history):

- `unicorn-fy >= 0.17.2`
- `unicorn-binance-rest-api >= 2.11.0`
- `unicorn-binance-websocket-api >= 2.12.2`
- `unicorn-binance-local-depth-cache >= 2.12.2`
- `unicorn-binance-trailing-stop-loss >= 1.3.1`
- `ubdcc >= 0.5.0`

**Rule:** Never pin to a version that isn't released on PyPI yet — pip-resolver will silently fall through to the previous suite version. Bump constraints *after* upstream modules have been published.

---

## Running Tests

```bash
# Smoke test: verify every suite module imports cleanly
python -m unittest unittest_binance_suite.py
```

CI runs the same across the full Python matrix.

---

## Build & Packaging

- **PyPI:** `.github/workflows/build_wheels.yml` builds the sdist + noarch wheel and publishes via trusted publisher on release.
- **conda-forge:** the [unicorn-binance-suite-feedstock](https://github.com/conda-forge/unicorn-binance-suite-feedstock) picks up the new PyPI release automatically. `meta.yaml` in this repo is the local dev copy, not used by the feedstock.
- **No in-repo conda build.** `build_conda.yml` was removed during the LUCIT cleanup round — conda-forge is the single conda source.

**Version bump** — `dev/set_version.py` (run by Oliver only). Version string lives in:
1. `setup.py` — `version=`
2. `pyproject.toml` — `version =`

---

## Code Conventions

- **File header:** Full MIT license block with author/copyright (Oliver Zehentleitner)
- **Encoding:** UTF-8, UNIX line endings
- **Language:** Chat in German with the maintainer; code + docs in English.

---

## Release Flow

A release cycle across the suite typically runs in dependency order:

1. `unicorn-fy` (standalone) — PyPI → conda-forge feedstock bump
2. `unicorn-binance-rest-api` (standalone) — PyPI → feedstock bump
3. `unicorn-binance-websocket-api` (depends on unicorn-fy + UBRA) — PyPI → feedstock bump
4. `unicorn-binance-local-depth-cache` (depends on UBWA + UBRA) — PyPI → feedstock bump
5. `unicorn-binance-trailing-stop-loss` (depends on UBWA + UBRA) — PyPI → feedstock bump
6. `ubdcc` (depends on UBLDC) — PyPI only (no conda-forge by design)
7. **This repo** — bump pins to the new module versions, PyPI + feedstock bump

Conda-forge channel indexing takes ~10–30 min per feedstock, so running downstream feedstock bumps too early will fail with unsatisfiable deps — wait for the upstream package to land in the channel.

---

## Notes & Gotchas

- Meta-package has no source code; any "bug" is really in one of the six modules.
- The `meta.yaml` in this repo is for **local dev builds only**. Conda-forge uses its own feedstock recipe.
- Don't add a `channels:` block to `meta.yaml` — it's not a valid key there; it belongs in `environment.yml` (`conda-forge` only, no `defaults`, no pip mixing).
- `dev/sphinx/source/conf.py` has a legacy `'lucit': True` theme option — keep it (theme-specific).
