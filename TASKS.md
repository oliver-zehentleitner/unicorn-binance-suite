# TASKS.md — UNICORN Binance Suite

Suite-wide backlog. Per-module tasks live in the respective repo's `TASKS.md`.

---

## Open

### [ ] conda-forge: finish the python 3.14 rollout
UBRA, UBWA, UBLDC and UBTSL feedstocks do not have py3.14 variants yet — the python314 migrator bot never opened a PR for them because they were `noarch: python` at the time of the first migrator run. Open rerun-bot issues waiting for the autotick-bot:
- UBRA: conda-forge/unicorn-binance-rest-api-feedstock#27
- UBWA: conda-forge/unicorn-binance-websocket-api-feedstock#36
- UBLDC: conda-forge/unicorn-binance-local-depth-cache-feedstock#17
- UBTSL: conda-forge/unicorn-binance-trailing-stop-loss-feedstock#21

Once all four feedstocks have `migrations/python314.yaml` + py3.14 variants built, drop the `python <3.14` cap on the UBS-Meta feedstock (`recipe/meta.yaml` lines pinning `python >=3.10,<3.14` — just remove the `<3.14` part).

### [ ] README: add "Start here / Choose the right module" block at the very top
Before the competitor comparison table, add a short decision block so a first-time visitor instantly knows which sub-package they need. Template available in `llms.txt` (`## Use Case → Module Routing` table — one-liner per module). Suggested placement: directly after the install snippet, before the "Why UBS" comparison.

### [ ] File headers: add conda-forge URL in all modules
The standard per-file header block (`Project website`, `Github`, `Documentation`, `PyPI`) is missing a line for the conda-forge package. Add a consistent
`# Conda-Forge: https://anaconda.org/conda-forge/<package-name>` line right below the `PyPI` line in every `.py` file across all suite modules (UBWA, UBRA, UBLDC, UBTSL, UBDCC packages, UBS-Meta, UnicornFy).

### [ ] Check for Python 3.15 support (November 2026)
CPython 3.15 is scheduled for release in October 2026 ([PEP 790](https://peps.python.org/pep-0790/)).
conda-forge typically adds a new Python version to the global pinning 1–2 months after the CPython release,
once core packages (numpy, etc.) have uploaded 3.15 wheels.

**What to do when 3.15 lands:**
- Add `"Programming Language :: Python :: 3.15"` classifier in every `setup.py`
- Bump the supported range `3.9 – 3.14` → `3.9 – 3.15` in:
  - all READMEs
  - all `llms.txt` Version lines
  - `build_wheels.yml` `CIBW_BUILD` / `CIBW_PYTHON`
  - `unit-tests.yml` matrix
- Rerender each conda-forge feedstock so the 3.15 variants are generated
- Bump minimum deps where necessary

**When:** check ~November 2026.

---

## Done

(empty — this file was just created)
