# TASKS.md — UNICORN Binance Suite

Suite-wide backlog. Per-module tasks live in the respective repo's `TASKS.md`.

---

## Open

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
