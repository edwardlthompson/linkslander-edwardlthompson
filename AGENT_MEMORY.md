# Agent Memory

> Centralized index of tech stack, threat models, persistent context, and retrospectives.
> Update only at session startups, milestone boundaries, or major architectural pivots.

## Tech Stack

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Frontend | Vanilla JavaScript + HTML5 Canvas | — | Custom Matrix physics engine |
| UI | Bootstrap 5 (CDN) + custom CSS | 5.3.3 | Glassmorphism, always-dark theme |
| PWA | Service Worker + Web Manifest | — | Cache-first offline strategy |
| Audio | Web Audio API | — | Click ripple feedback |
| Hosting | GitHub Pages (Actions) | — | Deploy artifact from `site/` |
| License | MIT | — | Pure FOSS |
| Distribution | GitHub Pages | — | https://edwardlthompson.com |

## Active Modules

- [x] Web / PWA (`modules/web/MODULE.md`)
- [ ] Android / F-Droid — not applicable
- [ ] Python — not applicable
- [ ] Lightroom Classic — not applicable

## Repository Layout

| Path | Purpose |
|------|---------|
| `site/` | Published PWA (GitHub Pages artifact) |
| `docs/` | Agent documentation (not publicly served) |
| `examples/web/` | Golden Path Vite+TS stub for template CI |

## Threat Model Checklist

- [x] `docs/THREAT_MODEL.md` drafted (STRIDE, trust boundaries, top abuse cases)
- [x] No proprietary closed-source SDKs in production path
- [x] Opt-in only telemetry (none collected); see `docs/PRIVACY.md`
- [x] Secrets excluded from VCS (Gitleaks pre-commit)
- [x] Dependency vulnerability scanning enabled (CodeQL + Trivy + Dependabot)
- [x] Input validation at all data boundaries (static site; no user input)
- [x] `SECURITY.md` and private vulnerability reporting enabled

## Persistent Context

### Project Purpose

High-performance interactive personal landing page and PWA featuring a custom Matrix-style canvas background, glassmorphism UI, dual-contact vCard download, and offline installability on iOS/Android.

### Key Constraints

- Always-dark UI (no theme toggle); documented in `DECISION_LOG.md`
- Max 250 lines per view file, 150 lines per logic file (future refactor target for `site/css/style.css`)
- Trunk-based development with Conventional Commits
- Bootstrap loaded via CDN with SRI integrity hashes

## Session Retrospectives

| Date | Milestone | What worked | What to improve |
|------|-----------|-------------|-----------------|
| 2026-06-13 | Bootstrap adoption | Template scaffold + site/ split | Split large CSS file in future sprint |

## Template Provenance

- **Source template:** `edwardlthompson/agent-project-bootstrap`
- **Template version:** `0.2.1` (see `.template-version`)
- **Last update check:** See `.template-update.json`
