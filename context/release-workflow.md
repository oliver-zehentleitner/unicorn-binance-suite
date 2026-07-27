# Release workflow

## Fixed release order across the suite

**Status:** active
**Evidence:** confirmed
**Source:** maintainer
**Revisit when:** a new module is added to the suite, or a module's dependency graph changes

Releases across the suite always go in this order:

`unicorn-fy` → UBRA → UBWA → `UBLDC` + `UBTSL` (parallel) → `ubdcc` → `unicorn-binance-suite` (this repo, last)

**Reason:** this is the dependency order (each module pins the ones before it), validated empirically during the April 2026 LUCIT-cleanup release round (see `history.md`) where releasing out of order produced unsatisfiable-dependency failures on conda-forge.

**Rejected alternative:** releasing modules independently of this order (e.g. whenever a fix lands) was the implicit approach before that round. Rejected because a downstream module's conda-forge build fails outright if the upstream package hasn't finished indexing yet — not a soft warning, a hard build failure.

## Wait for conda-forge indexing, not just for the merge

**Status:** active
**Evidence:** confirmed
**Source:** maintainer

After a feedstock PR is merged, there's a ~15–30 minute gap before the package is actually indexed in the conda-forge channel. The next downstream module's feedstock bump must wait for indexing, not just for the merge to land.

**Reason:** merging the feedstock PR triggers the build, but the resulting package isn't queryable by conda-forge's resolver until channel indexing finishes. Bumping a downstream feedstock's pin before that window closes fails with unsatisfiable dependencies, even though the upstream PR is already merged.

## Bot-driven pin bumps vs. manual PRs

**Status:** active
**Evidence:** confirmed
**Source:** maintainer

The conda-forge autotick bot opens pin-bump PRs in downstream feedstocks automatically once an upstream package updates. For simple pin bumps, these bot PRs are left for the maintainer to merge as needed — no manual PR is opened to chase them.

**Reason:** manually duplicating what the bot already does is redundant. A manual PR is only opened when more than a pin bump is needed: a multi-layer cleanup round touching several modules at once, or an actual feature change in the downstream module itself.

## Recurring pitfalls (not bugs, expected friction)

- **CDN-cache race:** a feedstock PR's own CI goes green, but the subsequent main-branch build goes red on the same `meta.yaml` roughly a minute later. Not a real regression — the fix is a new build-number bump and retry. Most likely right after suite deps were just freshly published, before the CDN has caught up.
- **Parallel pin-PR conflicts:** two bump PRs open at once both touch the same `CHANGELOG.md` `X.X.dev` block; merging one requires rebasing the other.
- **Partial Azure builds:** if Azure (Windows/Mac) fails with transient git-fetch errors while Linux is green, the package can land incomplete in the channel. Fix: a new PR bumping `build.number` plus an explicit `@conda-forge-admin, please rerender` comment (the rerender request must be a comment, not text in the PR body — it isn't executed there).
- **Python 3.14 migration silently reverts:** once a feedstock has been converted from `noarch: python` to a compiled build (Cython), a plain rerender can *delete* the existing `.ci_support/*python3.14*` files instead of regenerating them, because conda-smithy falls back to global pinning defaults without an active migration file. Fix: ensure `.ci_support/migrations/python314.yaml` exists in the feedstock (copy from conda-forge's `conda-forge-pinning-feedstock` migrations, or from `unicorn-binance-websocket-api-feedstock` which already has it), commit it, then rerender. Check for this file on every UBS feedstock bump — it's easy to lose 3.14 support silently on a routine rerender otherwise.
- **Autotick bot opens a redundant version-bump PR in parallel** with a manual one — just close it (requires maintainer, the AIgent account has no close rights on those repos).

**Evidence:** all of the above validated during the April 2026 (2026-04-18/19) suite-wide cleanup release round.
