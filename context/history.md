# History

## LUCIT branding/licensing removal (April 2026)

**Type:** decision
**Status:** superseded — LUCIT is fully removed as of this cleanup round
**Evidence:** confirmed
**Source:** commits `83cc723`, `af0a4bf`, `c32edb2`, `097de55`, and others across April 2026

The suite previously had a "LUCIT" branding and licensing layer across all repos: a `lucit` conda channel (`meta.yaml`/`environment.yml`), a `lucit-licensing-python` host dependency, LUCIT-branded logos/badges, a `lucit.tech` security-contact form, and Matomo/Freshchat tracking snippets pointing at `lucit.*` domains in the Sphinx theme config.

This was removed suite-wide: conda-forge is now the only conda channel, the licensing dependency is gone, logos and badges were replaced, and `SECURITY.md` now points to GitHub Security Advisories instead of the LUCIT contact form.

**Reason:** LUCIT is no longer part of how this suite is distributed or supported — the packages are self-contained, licensed under plain MIT, and distributed solely through PyPI, conda-forge, and GitHub.

**Leftover, deliberately kept:** the Sphinx theme's `'lucit': True` option in `conf.py` (see `packaging.md`) — it's a theme feature flag, not a brand reference, and removing it would need a theme-level change, not just a repo cleanup.

**Revisit when:** the suite forks its own Sphinx theme (see suite-wide plan) — re-check whether the `'lucit'` flag still applies under the new theme.
