# Third-Party Licenses

> Dependency attribution for LinksLander.

## Project License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).

## Runtime Dependencies (vendored in `site/`)

| Dependency | Version | Location | License |
|------------|---------|----------|---------|
| Bootstrap CSS | 5.3.3 | `site/vendor/bootstrap-5.3.3/css/bootstrap.min.css` | MIT |
| Bootstrap JS Bundle | 5.3.3 | `site/vendor/bootstrap-5.3.3/js/bootstrap.bundle.min.js` | MIT |

Bootstrap is vendored locally (not loaded from CDN) for offline PWA reliability. Update via Dependabot/manual review; bump `site/sw.js` cache version when upgrading.

## Brand Icon Assets

| Asset | Location | License |
|-------|----------|---------|
| Simple Icons brand glyphs | `site/img/brands/*.svg` | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) ([simple-icons](https://simpleicons.org)) |
| Custom / site-specific marks | `site/img/{GV,IWWYV,heart_transparent,word-connections}.*` | Site assets |

Simple Icons glyphs are vendored locally (not CDN) for offline PWA use. Brand names remain trademarks of their owners; marks identify outbound links only.

## Dev Dependencies (npm)

Run license audits:

```bash
# Golden Path web example
cd examples/web && npx license-checker --production --summary

# Production site test harness
cd site && npx license-checker --production --summary
```

`[AUTO]` CI runs `scripts/check-license-compliance.sh web` on each push.

## Attribution

When bundling dependencies in releases, include this file in the distribution artifact.

## Incompatible Licenses

`[HUMAN]` must approve any dependency with copyleft licenses (GPL, AGPL). Document exceptions in `DECISION_LOG.md`.
