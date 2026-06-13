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

## Sprint 0 ù Bootstrap Adoption ? COMPLETE

> Archived 2026-06-13. See `COMPLETED_TASKS.md` ? LinksLander Sprint 0.

---

## Sprint 1 ù Site Hardening ? COMPLETE

> Archived 2026-06-13. See `COMPLETED_TASKS.md` ? LinksLander Sprint 1.
>
> **Deferred:** Split `site/css/style.css` into modules (future refactor sprint).

---

## Sprint 2 ù Ongoing Maintenance (active)

### Weekly (recurring)

- [ ] [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md` (recommended: Monday)
- [ ] [AGENT] Apply Dependabot dependency bumps and open PRs as needed (none pending as of 2026-06-13)
- [x] [AUTO] Trivy + CodeQL + CI matrix green after merges (verified @ `a70776b`)
- [x] [AUTO] Template update check (`scripts/check-template-updates.ps1`) ù no upstream update

### Optional

- [ ] [HUMAN] Install pre-commit hooks locally (`pip install pre-commit && pre-commit install`)

---

## Milestone Gates

### Automated (Sprint 0ù1 sign-off)

- [x] [AUTO] Regression tests: zero failures (CI `site-pwa` + `web` jobs green)
- [x] [AUTO] Static analysis and vulnerability scans clean (Trivy + CodeQL green)
- [x] [AUTO] Workflow action refs validated (`scripts/validate-workflow-actions.sh`)
- [x] [AUTO] UTF-8 encoding check clean (`scripts/check-file-encoding.sh`)
- [x] [AUTO] Lockfiles present and CI uses locked installs (`npm ci`)
- [x] [AUTO] `TEMPLATE_INDEX.json` complete (`scripts/validate-template-index.sh`)

### Human (release / ongoing)

- [x] Weekly CVE triage completed within last 7 days (initial pass 2026-06-13: 0 alerts)
- [x] [HUMAN] Zero open Critical/High Dependabot alerts (verified 2026-06-13)
- [x] [HUMAN] CHANGELOG.md updated (Keep a Changelog format)
- [x] [HUMAN] `THIRD_PARTY_LICENSES.md` reviewed for distribution

---

## Future ù Sprint 3 (backlog)

| Task | Owner | Notes |
|------|-------|-------|
| Split `site/css/style.css` into modules | AGENT | Align with AGENTS.md 250-line view limit |
| GitHub Release tag `v2.0.0` | HUMAN | After formal release approval |
