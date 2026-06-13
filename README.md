# LinksLander — Edward Lee Thompson Digital Portal

A high-performance, interactive personal landing page and PWA at [edwardlthompson.com](https://edwardlthompson.com). Features a custom Matrix-style physics engine, glassmorphism UI, and offline accessibility.

Bootstrapped with [agent-project-bootstrap](https://github.com/edwardlthompson/agent-project-bootstrap) v0.2.1 for Cursor agent workflows, CI guardrails, and FOSS compliance.

## Features

- **Persistent 3D-Grid Engine:** Custom HTML5 Canvas background with gravitational cursor interaction and click ripples
- **PWA Core:** Installable on iOS/Android with offline caching via Service Workers
- **Retro-Tech Aesthetic:** CRT scanlines, phosphor-green grading, always-dark theme
- **Dual-Contact vCard:** Integrated `.vcf` download with primary and secondary phone lines

## Tech Stack

| Layer | Technology |
|-------|------------|
| Engine | Vanilla JavaScript / HTML5 Canvas |
| UI | Bootstrap 5.3.3 (CDN) + custom CSS |
| PWA | Service Worker + Web App Manifest |
| Hosting | GitHub Pages (Actions deploy from `site/`) |

## Repository Layout

| Path | Purpose |
|------|---------|
| `site/` | Published PWA (GitHub Pages artifact) |
| `docs/` | Agent documentation (`START_HERE.md`, runbooks) |
| `examples/web/` | Golden Path Vite+TS stub (template CI) |
| `scripts/` | Validation, init, update checker |

## Quick Start (Development)

```bash
# Serve production site locally
cd site && npm ci && npm start

# Run e2e + Lighthouse on site/
cd site && npm run test:e2e && npm run lighthouse

# Golden Path web example
cd examples/web && npm ci && npm test && npm run build
```

## Agent Bootstrap

Open Cursor and paste:

```
Read @docs/START_HERE.md and @docs/INITIALIZATION_PROMPT.md.
Follow Section 8 Startup Sequence.
Use BUILD_PLAN.md Sequential lane first; respect AGENT/HUMAN/ADB/AUTO labels.
```

## BUILD_PLAN Labels

| Label | Owner | When to use |
|-------|-------|-------------|
| `AGENT` | Cursor Agent | Code, docs, scaffolding, tests, CI |
| `HUMAN` | Human developer | Approvals, credentials, GitHub settings |
| `AUTO` | CI/scripts | GitHub Actions, Dependabot, pre-commit |

```bash
grep '\[AGENT\]' BUILD_PLAN.md
grep '\[HUMAN\]' BUILD_PLAN.md
```

## Template Update Checker

Configure in [`.template-update.json`](.template-update.json). Manual check:

```powershell
pwsh scripts/check-template-updates.ps1
```

When a new upstream template version is available, see [`docs/UPGRADING_FROM_TEMPLATE.md`](docs/UPGRADING_FROM_TEMPLATE.md).

## GitHub CI Gate

After pushing workflow or dependency changes to `main`:

```powershell
pwsh scripts/check-github-ci.ps1 -WaitSeconds 300
```

Required workflows: **CI**, **Security Scan**, **CodeQL**, **Deploy GitHub Pages**.

## Security

Enable Dependabot alerts: **Settings → Code security and analysis**. Weekly CVE triage: [`docs/SECURITY_TRIAGE.md`](docs/SECURITY_TRIAGE.md). Report vulnerabilities via [`SECURITY.md`](SECURITY.md).

## Customization

- Update contact links: edit `site/index.html` and add icons to `site/img/`
- Matrix background / styling: edit `site/js/matrix.js` and `site/css/style.css`

## License

MIT — see [`LICENSE`](LICENSE). Third-party attribution: [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).

**Maintained by Edward Lee Thompson.**
