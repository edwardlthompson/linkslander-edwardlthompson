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

## Sprint Audit — 2026-07-12 (active)

> Findings: `CODE_REVIEW.md` (gitignored). AGENT remediation archived in [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).

### Sequential (remaining)

- 🔲 [HUMAN] A01 Merge Release Please PR #2 — `chore(main): release 2.1.0` (F-001)
- 🔲 [HUMAN] A05 Editorial pass on cognate rows in `site/scripts/gen-roots-table.py` (F-005)
- ✅ [HUMAN] A07 Remove `cunnilingus` etymology row (F-007)

### Parallel

- 🔲 [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md`
- 🔲 [AGENT] Apply Dependabot dependency bumps and open PRs as needed (0 open alerts as of 2026-07-12)
- 🔲 [HUMAN] Install pre-commit hooks locally (`pip install pre-commit && pre-commit install`)

### Deferred

- F-009 Local feature-gate WSL1 `npx` path — use native npm / WSL2
- F-010 CSP headers — Cloudflare/Pages preference
- F-011 Externalize cognate data + CI regen check

---

## Archived sprints

All feature sprints complete including **v2.0.0** release and Language Comparison (Word Connections) on `main`. See [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).

Future app releases are automated via Release Please on push to `main` (open: PR #2 → **v2.1.0**).
