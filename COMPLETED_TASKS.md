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
- [ ] [HUMAN] Install pre-commit hooks locally (optional)

---

## LinksLander — Sprint 1 Site Hardening (2026-06-13)

### Sequential

- [x] [AGENT] Fix SW cache manifest + restore missing image assets
- [x] [AGENT] Add `site/` Playwright + Lighthouse CI harness
- [x] [AGENT] Remove dead `.theme-toggle-btn` CSS (cleanup only — no theme feature)
- [x] [AUTO] `site-pwa` + `web` CI jobs green
- [x] [HUMAN] Verify live site at edwardlthompson.com after Pages Actions deploy

### Parallel

- [x] [AGENT] Verify SRI on Bootstrap CDN links (`site/index.html` — CSS + JS already pinned)
- [ ] [AGENT] Split `site/css/style.css` into modules (deferred — future refactor)

---

## LinksLander — Sprint 2 Maintenance (2026-06-13, partial)

- [x] [AUTO] Template update check (`scripts/check-template-updates.ps1`) — no upstream update
- [x] [AUTO] Trivy + CodeQL + CI green on `main` @ `a70776b`
- [x] [AGENT] Dependabot review — 0 open alerts, 0 open PRs, `npm audit` clean

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
