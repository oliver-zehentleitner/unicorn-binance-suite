# Dependency management

## Deps are declared in 5 files, kept in sync manually

**Id:** e4ecf155-46ab-432e-9403-25ad694f453c
**Type:** constraint
**Status:** active
**Evidence:** confirmed
**Source:** retrospective pass; maintainer, 2026-09-28

`requirements.txt`, `setup.py`, `pyproject.toml`, `environment.yml`, and `meta.yaml` (local dev copy) all declare the suite's module dependencies independently. `setup.py` is the source of truth; the other four are updated by hand whenever it changes.

**Reason:** the five files belong to four different packaging ecosystems (pip sdist, PEP 621/pyproject, conda env spec, conda recipe) that don't share a common dependency-declaration format this project generates from. A single generated source was never proposed; this is the default state of a multi-ecosystem Python package, not a considered-and-rejected alternative — derived from the history in a retrospective pass, confirmed by the maintainer on 2026-09-28.

## Never pin to a version that isn't released on PyPI yet

**Id:** 14654d8a-59b4-47ba-b047-da435520fc08
**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** maintainer
**See:** release-workflow.md#wait-for-conda-forge-indexing-not-just-for-the-merge — a5227f38-928b-4573-9f9a-eeae5a3b336b — as of 2026-09-28

When bumping a suite-module constraint (e.g. `unicorn-binance-websocket-api >= 2.15.0`), the new floor must already be published on PyPI before the commit lands here.

**Reason:** pip's resolver doesn't error on an unsatisfiable floor — it silently falls back to the newest version that *is* available, which is the previous one. The bump then looks like it landed but has no actual effect, and the mismatch isn't visible until something that depends on the new floor's behavior breaks downstream.

**Rejected alternative:** bumping constraints as soon as the corresponding upstream PR merges (i.e. tracking source instead of tracking releases). Rejected for the reason above — a merged PR isn't a resolvable version yet.

**How to apply:** bump suite pins only after the corresponding module's PyPI release is confirmed live, and after conda-forge indexing if the conda-side pin is also being bumped (see `release-workflow.md`).
