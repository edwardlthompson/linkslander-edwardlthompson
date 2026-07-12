# Completed Tasks

> Archive of finished BUILD_PLAN items.

## LinksLander — Sprint 0 Bootstrap Adoption (2026-06-13)

### Sequential

- [x] [HUMAN] Switch GitHub Pages source to GitHub Actions; enable Dependabot alerts + private vulnerability reporting
- [x] [HUMAN] Branch protection on `main` (ruleset `17641917`: Security Scan, CodeQL, key CI jobs)
- [x] [AGENT] Import template scaffolding v0.2.1; prune non-web stacks
- [x] [AGENT] Move site to `site/`; add `pages.yml` workflow
- [x] [AGENT] Customize memory files, ADR-0002, RUNBOOK, THREAT_MODEL
- [x] [AUTO] `validate-bootstrap.sh`, encoding check, template index check pass
- [x] [HUMAN] Approve Sprint 0 after all workflows green on `main`

### Parallel

- [x] [HUMAN] Set GitHub repo About from `docs/GITHUB_ABOUT.md`
- [x] [HUMAN] Configure `.template-update.json` interval (`weekly`)

---

## LinksLander — Sprint 1 Site Hardening (2026-06-13)

### Sequential

- [x] [AGENT] Fix SW cache manifest + restore missing image assets
- [x] [AGENT] Add `site/` Playwright + Lighthouse CI harness
- [x] [AGENT] Remove dead `.theme-toggle-btn` CSS (cleanup only — no theme feature)
- [x] [AUTO] `site-pwa` + `web` CI jobs green
- [x] [HUMAN] Verify live site at edwardlthompson.com after Pages Actions deploy

### Parallel

- [x] [AGENT] Verify SRI on Bootstrap CDN links (`site/index.html` — superseded by local vendoring in code review remediation)

---

## LinksLander — v2.0.0 Release (2026-06-21)

- [x] [AGENT] Decouple app semver (manifest + `site/package.json`) from `.template-version` (upstream)
- [x] [AGENT] Customize `release.yml`, `release-please.yml`, and version sync scripts for child repo
- [x] [AUTO] GitHub Release `v2.0.0` with SBOM assets via `release.yml`
- [x] [HUMAN] Backlog cleared — project ready to park

---

## LinksLander — Sprint 3 CSS Modularization (2026-06-21)

- [x] [AGENT] Split `site/css/style.css` into six modules under `site/css/modules/`
- [x] [AGENT] Update `index.html` link tags and `sw.js` cache (`matrix-cache-v5`)
- [x] [AUTO] Site e2e 7/7 pass; validate-bootstrap + feature-gate + repo-hygiene green

---

## LinksLander — Sprint 4 Template Parity v0.11.1 (2026-06-13)

### Sequential

- [x] [AGENT] Sync template scaffolding from `agent-project-bootstrap` v0.11.1
- [x] [AGENT] Merge CI for web-only child repo (keep `site-pwa`; add repo-hygiene, feature-gate, upgrade-simulation)
- [x] [AGENT] Restore LinksLander customizations (`site/`, `pages.yml`, RUNBOOK, THREAT_MODEL, THIRD_PARTY_LICENSES)
- [x] [AUTO] `validate-bootstrap.sh`, encoding check, e2e + web tests green
- [ ] [HUMAN] Verify live site after deploy

### Parallel

- [x] [AGENT] Adopt new workflows (weekly-health-check, release-please, scorecard, stale, dependabot-automerge)
- [x] [AGENT] Update `.template-version` to `0.11.1`; prune `TEMPLATE_INDEX.json` for web stack

---

## LinksLander — Sprint 3 Code Review Remediation (2026-06-13)

### Phase 1 — Security, CSS, metadata

- [x] [AGENT] Add `rel="noopener noreferrer"` to all external `target="_blank"` links
- [x] [AGENT] Remove CSS merge stubs; fix Matrix effect comment in `site/css/style.css`
- [x] [AGENT] Fix OG/meta tags, `browserconfig.xml`, `manifest.json` start_url, sitemap lastmod
- [x] [AGENT] Add aria-labels for adventure and payment links; fix tooltip init

### Phase 2 — Offline PWA

- [x] [AGENT] Vendor Bootstrap 5.3.3 under `site/vendor/bootstrap-5.3.3/`
- [x] [AGENT] Expand `site/sw.js` to `matrix-cache-v4` with resilient `Promise.allSettled` install
- [x] [AGENT] Update `THIRD_PARTY_LICENSES.md`, `docs/THREAT_MODEL.md`, `docs/RUNBOOK.md`, KB-007

### Phase 3 — Polish and tests

- [x] [AGENT] `matrix.js` `updateFontSize()` on resize
- [x] [AGENT] Prune unused root icon assets; align browserconfig tile paths
- [x] [AGENT] Extend e2e tests (noopener, local Bootstrap, offline smoke)
- [x] [AUTO] CI gates: e2e, encoding check

---

## LinksLander — Sprint 2 Maintenance (2026-06-13)

- [x] [AUTO] Template update check (`scripts/check-template-updates.ps1`) — no upstream update
- [x] [AUTO] Trivy + CodeQL + CI matrix green after merges (verified @ `a70776b`)
- [x] [AGENT] Dependabot review — 0 open alerts, 0 open PRs, `npm audit` clean
- [x] [HUMAN] Initial CVE triage pass (2026-06-13: 0 alerts)

---

## LinksLander — Milestone Gates (Sprint 0–1 sign-off, 2026-06-13)

### Automated

- [x] [AUTO] Regression tests: zero failures (CI `site-pwa` + `web` jobs green)
- [x] [AUTO] Static analysis and vulnerability scans clean (Trivy + CodeQL green)
- [x] [AUTO] Workflow action refs validated (`scripts/validate-workflow-actions.sh`)
- [x] [AUTO] UTF-8 encoding check clean (`scripts/check-file-encoding.sh`)
- [x] [AUTO] Lockfiles present and CI uses locked installs (`npm ci`)
- [x] [AUTO] `TEMPLATE_INDEX.json` complete (`scripts/validate-template-index.sh`)

### Human

- [x] [HUMAN] Zero open Critical/High Dependabot alerts (verified 2026-06-13)
- [x] [HUMAN] CHANGELOG.md updated (Keep a Changelog format — v2.0.0 entry)
- [x] [HUMAN] `THIRD_PARTY_LICENSES.md` reviewed for distribution

---

## LinksLander — Audit Sprint AGENT remediation (2026-07-12)

### Sequential (completed)

- ✅ [AGENT] A02 Align Word Connections `og:description` with EN→DE→ES→PT→IT→FR columns
- ✅ [AGENT] A03 Register service worker on `word-connections.html`
- ✅ [AGENT] A04 Fix `gen-roots-table.py` docstring (regen-only workflow)
- ✅ [AGENT] A06 Add English-cell meaning legend (Break / Borrowed / Aligned)
- ✅ [AGENT] A08 Offline + SW Playwright coverage for Language Comparison; SW `clients.claim` + navigate cache fallback; cache `matrix-cache-v8`

Remaining HUMAN items stay on active `BUILD_PLAN.md` (merge Release Please 2.1.0, cognate editorial, cunnilingus decision).

---

## Template Maintainer Archive (upstream bootstrap — not LinksLander scope)

<details>
<summary>agent-project-bootstrap template maintainer history</summary>

### v0.2.1 Full Bootstrap Hardening (2026-06-13)

- [x] [AGENT] Normalize `.gitignore` UTF-16 to UTF-8; extend encoding scan and pre-commit hook
- [x] [AGENT] Sync `PROMPT_LIBRARY.md` entries 4, 6, 8, 9; populate `KNOWLEDGE_BASE.md` (6 entries)
- [x] [AGENT] Document Lighthouse 3-run median in `modules/web/MODULE.md`
- [x] [AGENT] SHA-pin `release.yml` actions; add pin policy to `docs/SECURITY_TRIAGE.md`
- [x] [AGENT] Add `check-workflow-action-ref-format.sh` pre-commit hook
- [x] [AGENT] Init scripts: `validate-workflow-actions` + `check-github-ci` reminder
- [x] [AGENT] Devcontainer: encoding check, gh CLI feature, CI gate tip
- [x] [AGENT] Add `health-check.yml` weekly workflow
- [x] [AGENT] Bootstrap Gradle wrapper; CI `android-build` assembleDebug job
- [x] [AGENT] Bump to v0.2.1; sync `TEMPLATE_INDEX.json`, `CHANGELOG.md`, `README.md`

### v0.2.0 Backlog Fix (2026-06-12)

- [x] [AGENT] Normalize UTF-16 files to UTF-8; add `scripts/check-file-encoding.sh` + CI + pre-commit
- [x] [AGENT] Add `package-lock.json`, `uv.lock`, `.env.example`; expand `validate-bootstrap.sh`
- [x] [AGENT] Sync `TEMPLATE_INDEX.json` with LICENSE, scripts, workflows, rules
- [x] [AGENT] Harden license-compliance CI; web coverage budget; android ops checklist
- [x] [AGENT] Harden INITIALIZATION_PROMPT Sections 2/7/8 with Build Verification Gate
- [x] [AGENT] Update BUILD_PLAN Sprint 0 + Milestone Gates
- [x] [AGENT] Bump `.template-version` to 0.2.0; finalize CHANGELOG

</details>
