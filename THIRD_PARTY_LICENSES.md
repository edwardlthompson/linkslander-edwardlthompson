# Third-Party Licenses

> Dependency and CDN attribution for LinksLander.

## Project License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).

## Runtime Dependencies (CDN — not npm locked)

| Dependency | Version | Source | License |
|------------|---------|--------|---------|
| Bootstrap CSS | 5.3.3 | jsDelivr CDN | MIT |
| Bootstrap JS Bundle | 5.3.3 | jsDelivr CDN | MIT |

SRI integrity hashes are set on both CDN `<link>` and `<script>` tags in `site/index.html`.

## Brand Icon Assets

Icons under `site/img/` are official brand assets from their respective platforms, used for link identification only. Not redistributed as standalone products.

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
