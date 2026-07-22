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

**Task format:** `- 🔲 [OWNER] Description` (status: 🔲 open · ✅ done · ❌ blocked)

**Filter by label:**

```bash
grep '\[AGENT\]' BUILD_PLAN.md
grep '\[HUMAN\]' BUILD_PLAN.md
```

**Agent rule:** Execute all `[AGENT]` Sequential items first, then dispatch Parallel agents with isolated file scopes.

---

## Sprint 2 — Ongoing Maintenance (active)

### Human & device (after automation)

- ✅ [HUMAN] Merge Release Please PR [#3](https://github.com/edwardlthompson/linkslander-edwardlthompson/pull/3) (`v2.1.1` published 2026-07-22)
- ✅ [HUMAN] Set repo secret `AUTOMERGE_TOKEN` (2026-07-22; from `gh auth` with repo+workflow scopes) — re-run setup script if `gh auth login` rotates the token
- 🔲 [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md` (recommended: Monday)
- 🔲 [HUMAN] Editorial pass on Language Comparison cognate rows (`site/scripts/gen-roots-table.py`)
- 🔲 [HUMAN] Install pre-commit hooks locally (`pip install pre-commit && pre-commit install`)

### Weekly (recurring)

- 🔲 [AGENT] Apply Dependabot dependency bumps and open PRs as needed

---

## Archived sprints

All feature and audit sprints complete through **v2.1.1**. See [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).

Future app releases are automated via Release Please on push to `main`.
