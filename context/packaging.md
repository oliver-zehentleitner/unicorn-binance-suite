# Packaging

## No in-repo conda build

**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** commit 83cc723, 2026-04-18

`.github/workflows/build_conda.yml` was removed; conda-forge's own feedstock (`unicorn-binance-suite-feedstock`) is the only conda build path. `meta.yaml` in this repo is kept only as a local dev copy — it's not used by the feedstock and not built in CI.

**Reason:** conda-forge builds and publishes the conda package on its own infrastructure once the feedstock recipe is updated; an in-repo conda build was redundant with that and added a build path the feedstock doesn't consume anyway.

**Rejected alternative:** keeping the in-repo conda build as a pre-publish sanity check. Rejected as part of the same cleanup — the feedstock's own CI already validates the recipe.

## `channels:` doesn't belong in `meta.yaml`

**Type:** constraint
**Status:** active
**Evidence:** confirmed
**Source:** commit 83cc723, 2026-04-18

`meta.yaml` no longer has a `channels:` block. It was removed because conda-build silently ignores `channels:`/`dependencies:` keys there — those are `environment.yml` keys, not valid `meta.yaml` recipe keys. Silently ignored, not erroring, is what let it sit there unnoticed for a while.

**How to apply:** channel configuration (`conda-forge` only, no `defaults`, no pip mixing) belongs in `environment.yml`, never in `meta.yaml`.

## Sphinx theme's `'lucit': True` flag

**Type:** decision
**Status:** active
**Evidence:** inferred

`dev/sphinx/source/conf.py` sets `'lucit': True` in `html_context`, even though the LUCIT branding/licensing cleanup (see `history.md`) removed LUCIT elsewhere in the repo (badges, channel refs, contact URLs).

**Reason (inferred):** this is a boolean feature flag consumed by the custom Sphinx theme (`python_docs_theme_lucit`) to switch on a layout/behavior mode, not a literal LUCIT brand reference — removing it would change how the theme renders, not just cosmetic wording. No commit was found explaining the flag's internal meaning inside the theme itself; kept as inferred since that would require reading the theme package's source, not just this repo's history.

**Revisit when:** the suite forks or replaces `python_docs_theme_lucit` (see suite-wide plan to fork it into a UBS-specific theme variant) — at that point this flag's meaning should be re-checked against the new theme's option, not carried over blindly.
