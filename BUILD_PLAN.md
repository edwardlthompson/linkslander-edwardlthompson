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

## Sprint 2 ù Ongoing Maintenance (active)

### Weekly (recurring)

- [ ] [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md` (recommended: Monday)
- [ ] [AGENT] Apply Dependabot dependency bumps and open PRs as needed

### Optional

- [ ] [HUMAN] Install pre-commit hooks locally (`pip install pre-commit && pre-commit install`)

---

## Sprint 3 ó Backlog

| Task | Owner | Notes |
|------|-------|-------|
| Split `site/css/style.css` into modules | AGENT | Align with AGENTS.md 250-line view limit |
| GitHub Release tag `v2.0.0` | HUMAN | After formal release approval |

Code review remediation (Phases 1ñ3) is complete ó see [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).

---

## Archived sprints

Sprint 0 (Bootstrap Adoption) and Sprint 1 (Site Hardening) are complete. See [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).
