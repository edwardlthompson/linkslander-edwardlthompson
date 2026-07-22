# Agent Memory

> Centralized index of tech stack, threat models, persistent context, and retrospectives.
> Update only at session startups, milestone boundaries, or major architectural pivots.

## Tech Stack

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Frontend | Vanilla JavaScript + HTML5 Canvas | — | Custom Matrix physics engine |
| UI | Bootstrap 5 (vendored) + custom CSS | 5.3.3 | `site/vendor/`; glassmorphism, always-dark theme |
| PWA | Service Worker + Web Manifest | — | Cache-first offline (`matrix-cache-v8`) |
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
- Max 300 lines static data / 150 lines pure logic (`docs/FILE_SIZE_GUIDE.md`; future refactor target for `site/css/style.css`)
- Trunk-based development with Conventional Commits
- Bootstrap vendored under `site/vendor/` for offline PWA (see KB-007)

## Session Retrospectives

| Date | Milestone | What worked | What to improve |
|------|-----------|-------------|-----------------|
| 2026-06-13 | Sprint 0–1 complete | Bootstrap + CI/site hardening; ruleset protection | CSS module split deferred to Sprint 3 |
| 2026-07-12 | Audit sprint AGENT remediations | Meta/SW/legend/offline e2e; 17 site tests green | Merge Release Please PR #2 (v2.1.0) still [HUMAN] |
| 2026-06-28 | Language Comparison page | 7-column table + gen script; site e2e 14 tests green | Feature gate web-lint fails under WSL1 bash — use `npm run lint` directly on Windows |
| 2026-07-21 | FOSS Cursor surface (partial 0.15) | Hooks/skills/agents/worktrees + agent docs; gates green | Full `.template-version` bump + automerge still deferred |
## Template Provenance

- **Source template:** `edwardlthompson/agent-project-bootstrap`
- **Template version:** `0.11.1` (see `.template-version`) — FOSS Cursor surface (hooks/skills/agents/worktrees) cherry-picked from `v0.15.0` on 2026-07-21; full version bump deferred
- **Last update check:** See `.template-update.json`
- **Alignment record:** `docs/BOOTSTRAP_ALIGNMENT.md`
