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

### Feature — Contacts gate + icon labels + static avatar

- ✅ [AGENT] Show one-word labels under icons; lock private Direct Contact / Social / card behind `#MyContacts` AES-GCM gate; static aspect-locked avatar (`img/p.jpg`); Pages artifact strip + SW/docs/e2e updates
- ✅ [AGENT] Portal UI polish: force-visible labels, Snapchat/TikTok/YouTube PNGs, SW `matrix-cache-v11` (#14)

### Feature — Personal app store

- ✅ [AGENT] Other → Apps page with purpose groups/categories, detail modal, Releases CTAs, monogram logos, SW `matrix-cache-v38`, sitemap + e2e


### Human & device (after automation)

- ✅ [HUMAN] Merge Release Please PR [#3](https://github.com/edwardlthompson/linkslander-edwardlthompson/pull/3) (`v2.1.1` published 2026-07-22)
- ✅ [HUMAN] Set repo secret `AUTOMERGE_TOKEN` (2026-07-22; from `gh auth` with repo+workflow scopes) — re-run setup script if `gh auth login` rotates the token
- 🔲 [HUMAN] Run weekly CVE triage pass per `docs/SECURITY_TRIAGE.md` (recommended: Monday)
- 🔲 [HUMAN] Editorial pass on Language Comparison cognate rows (`site/scripts/gen-roots-table.py`)
- 🔲 [HUMAN] Install pre-commit hooks locally (`pip install pre-commit && pre-commit install`)

### Weekly (recurring)

- ❌ [AGENT] Clear Dependabot Critical/High alerts (`proxy-addr`, `compression`, `source-map-js` in site + examples/web) — blocked post-v2.3.0; PRs #19–#21 open for proxy-addr/source-map-js; compression still needs bumps
- 🔲 [AGENT] Apply Dependabot dependency bumps and open PRs as needed (merge #19–#21; open/merge compression bumps)
- ✅ [AUTO] Release Please published v2.3.0 (PR #18); SBOM assets on release; Pages deploy + CI/CodeQL/Security Scan green on `337dc4a`
- ✅ [AUTO] Template Upgrade Simulation passed on v2.3.0 merge

---

## Archived sprints

All feature and audit sprints complete through **v2.1.3**. See [`COMPLETED_TASKS.md`](COMPLETED_TASKS.md).

Future app releases are automated via Release Please on push to `main` (auto-merge + `AUTOMERGE_TOKEN`).
