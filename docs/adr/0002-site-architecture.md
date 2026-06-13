# ADR-0002: Site Architecture and Deployment

- **Status:** Accepted
- **Date:** 2026-06-13

## Context

LinksLander began as a static PWA published from the repository `docs/` folder via GitHub Pages. Adopting `agent-project-bootstrap` requires `docs/` for agent documentation (`START_HERE.md`, `RUNBOOK.md`, etc.), creating a path conflict.

## Decision

1. **Relocate the published site** from `docs/` to `site/`.
2. **Deploy via GitHub Actions** (`.github/workflows/pages.yml`) uploading `site/` as the Pages artifact.
3. **Reserve `docs/`** exclusively for agent and maintainer documentation (not publicly served as the homepage).
4. **Keep always-dark UI** — no light/dark theme toggle; Bootstrap `data-bs-theme="dark"` is fixed.
5. **Load Bootstrap 5.3.3 from jsDelivr CDN** with SRI integrity attributes on CSS and JS bundles.

## Alternatives Considered

| Alternative | Rejected because |
|-------------|------------------|
| Agent docs in `guide/` | Deviates from template; breaks `validate-bootstrap.sh` paths |
| Keep site in `docs/` | Would expose internal agent docs at public URLs |
| Migrate to Vite build for production site | Out of scope for bootstrap parity; deferred |

## Consequences

- `[HUMAN]` must switch GitHub Pages source from branch `/docs` to GitHub Actions.
- `CNAME` remains in `site/` for custom domain `edwardlthompson.com`.
- Template CI still validates `examples/web/` Golden Path stub separately from production `site/`.
- CDN dependency for Bootstrap documented in `docs/THREAT_MODEL.md` and `THIRD_PARTY_LICENSES.md`.

## References

- ADR-0001: `docs/adr/0001-template-baseline.md`
- Runbook: `docs/RUNBOOK.md`
