# Build Plan

> Prioritized task board with owner labels, Sequential and Parallel lanes per sprint.
> Move completed items to `COMPLETED_TASKS.md`.

## Owner Label Legend

| Label | Owner | When to use |
|-------|-------|-------------|
| `AGENT` | Cursor Agent | Code, docs, scaffolding, tests, CI config |
| `HUMAN` | Human developer | Approvals, credentials, GitHub settings, product decisions |
| `ADB` | Human (Android) | Android SDK, emulator/device testing, F-Droid submission |
| `AUTO` | CI/scripts/bots | GitHub Actions, Dependabot, pre-commit, update checker |

**Task format:** `- [ ] [OWNER] Description`

**Filter by label:**

```bash
grep '\[AGENT\]' BUILD_PLAN.md
grep '\[HUMAN\]' BUILD_PLAN.md
```

**Agent rule:** Execute all `[AGENT]` Sequential items first, then dispatch Parallel agents with isolated file scopes.

---

## Sprint 0 ù Bootstrap Adoption

### Sequential (must complete in order)

1. [x] [HUMAN] Switch GitHub Pages source to GitHub Actions; enable Dependabot alerts + private vulnerability reporting
2. [x] [HUMAN] Branch protection on `main` (CI, Security Scan, CodeQL required)
3. [x] [AGENT] Import template scaffolding; prune non-web stacks
4. [x] [AGENT] Move site to `site/`; add `pages.yml` workflow
5. [x] [AGENT] Customize memory files, ADR-0002, RUNBOOK, THREAT_MODEL
6. [x] [AUTO] `validate-bootstrap.sh`, encoding check, template index check pass
7. [ ] [HUMAN] Approve Sprint 0 after all workflows green on `main`

### Parallel (safe after Sequential step 5)

| Task | Owner | Isolated scope |
|------|-------|----------------|
| Set GitHub repo About from `docs/GITHUB_ABOUT.md` | HUMAN | GitHub Settings |
| Configure `.template-update.json` interval | HUMAN | `.template-update.json` |
| Install pre-commit hooks locally | HUMAN | local dev |

---

## Sprint 1 ù Site Hardening

### Sequential (must complete in order)

1. [x] [AGENT] Fix SW cache manifest + restore missing image assets
2. [x] [AGENT] Add `site/` Playwright + Lighthouse CI harness
3. [x] [AGENT] Remove dead `.theme-toggle-btn` CSS (cleanup only ù no theme feature)
4. [x] [AUTO] `site-pwa` + `web` CI jobs green
5. [x] [HUMAN] Verify live site at edwardlthompson.com after Pages Actions deploy

### Parallel (safe after Sequential step 2)

| Task | Owner | Isolated scope |
|------|-------|----------------|
| Add SRI to remaining CDN links if missing | AGENT | `site/index.html` |
| Split `site/css/style.css` into modules | AGENT | `site/css/**` (future refactor) |

---

## Sprint 2 ù Ongoing Maintenance

### Weekly (recurring)

- [ ] [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md` (recommended: Monday)
- [ ] [AGENT] Apply Dependabot dependency bumps and open PRs as needed
- [ ] [AUTO] Trivy + CodeQL + CI matrix green after merges
- [ ] [AUTO] Template update check (`scripts/check-template-updates.ps1`)

---

## Milestone Gates

- [ ] [AUTO] Regression tests: zero failures
- [ ] [AUTO] Static analysis and vulnerability scans clean
- [ ] [AUTO] Workflow action refs validated (`scripts/validate-workflow-actions.sh`)
- [ ] [AUTO] UTF-8 encoding check clean (`scripts/check-file-encoding.sh`)
- [ ] [AUTO] Lockfiles present and CI uses locked installs (`npm ci`)
- [ ] [AUTO] `TEMPLATE_INDEX.json` complete (`scripts/validate-template-index.sh`)
- [ ] [HUMAN] Weekly CVE triage completed within last 7 days
- [ ] [HUMAN] Zero open Critical/High Dependabot alerts (or documented exception)
- [ ] [HUMAN] CHANGELOG.md updated (Keep a Changelog format)
- [ ] [HUMAN] `THIRD_PARTY_LICENSES.md` reviewed for distribution
