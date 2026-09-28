# Packaging

## No in-repo conda build

**Id:** 735b6b07-59d0-43a8-95cc-2938b62855a5
**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** commit 83cc723, 2026-04-18

`.github/workflows/build_conda.yml` was removed; conda-forge's own feedstock (`unicorn-binance-suite-feedstock`) is the only conda build path. `meta.yaml` in this repo is kept only as a local dev copy — it's not used by the feedstock and not built in CI.

**Reason:** conda-forge builds and publishes the conda package on its own infrastructure once the feedstock recipe is updated; an in-repo conda build was redundant with that and added a build path the feedstock doesn't consume anyway.

**Rejected alternative:** keeping the in-repo conda build as a pre-publish sanity check. Rejected as part of the same cleanup — the feedstock's own CI already validates the recipe.

## `channels:` doesn't belong in `meta.yaml`

**Id:** 9bc8270c-a534-41be-93b7-6ffaed7827b4
**Type:** constraint
**Status:** active
**Evidence:** confirmed
**Source:** commit 83cc723, 2026-04-18

`meta.yaml` no longer has a `channels:` block. It was removed because conda-build silently ignores `channels:`/`dependencies:` keys there — those are `environment.yml` keys, not valid `meta.yaml` recipe keys. Silently ignored, not erroring, is what let it sit there unnoticed for a while.

**How to apply:** channel configuration (`conda-forge` only, no `defaults`, no pip mixing) belongs in `environment.yml`, never in `meta.yaml`.

## Sphinx theme's `'lucit': True` flag

**Id:** 8724ad7d-0e41-4eb1-a2bb-15b01a941f1f
**Type:** decision
**Status:** active
**Evidence:** confirmed
**Source:** retrospective pass; maintainer, 2026-09-28
**See:** history.md#lucit-brandinglicensing-removal-april-2026 — 2749fc08-cdca-456b-a8bd-fd4b646ff64c — as of 2026-09-28

`dev/sphinx/source/conf.py` sets `'lucit': True` in `html_context`, even though the LUCIT branding/licensing cleanup (see `history.md`) removed LUCIT elsewhere in the repo (badges, channel refs, contact URLs).

**Reason:** this is a boolean feature flag consumed by the custom Sphinx theme (`python_docs_theme_lucit`) to switch on a layout/behavior mode, not a literal LUCIT brand reference — removing it would change how the theme renders, not just cosmetic wording. First derived in a retrospective pass — no commit here explains the flag's meaning inside the theme — and confirmed by the maintainer on 2026-09-28.

**Revisit when:** the suite forks or replaces `python_docs_theme_lucit` (see suite-wide plan to fork it into a UBS-specific theme variant) — at that point this flag's meaning should be re-checked against the new theme's option, not carried over blindly.
