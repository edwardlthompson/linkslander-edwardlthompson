# Bootstrap Alignment — Gap Analysis

> **Phase 0 deliverable** for aligning this live child repo with upstream
> [`edwardlthompson/agent-project-bootstrap`](https://github.com/edwardlthompson/agent-project-bootstrap).
>
> **Date:** 2026-07-21  
> **Local template version:** `0.11.1` (`.template-version`)  
> **Upstream latest:** `v0.15.0` (published 2026-07-22)  
> **Mode:** Migration / upgrade — not a fresh bootstrap.

---

## 1. Repo identity & recommended stack

| Fact | Value |
|------|-------|
| Product | LinksLander — personal landing PWA (`edwardlthompson.com`) |
| Published artifact | `site/` (vanilla JS + Canvas + Bootstrap 5 + SW) |
| Golden Path stub | `examples/web/` (Vite+TS; template CI) |
| Stack selection | `.cursor/stack-selection.json` → **`web` only** (pruned) |
| Active module | `modules/web/MODULE.md` |
| License | MIT (compatible) |
| App version | `site/package.json` → `2.1.0` |

**Recommended stack selection:** keep **web-only**. Do not reintroduce android/python/go/rust/lightroom modules or examples.

---

## 2. What already matches the template

Core agent surface is present and largely current for a 0.11.x child:

| Area | Status |
|------|--------|
| `AGENTS.md` router | Present; `.cursorrules` absent (correct) |
| `docs/START_HERE.md`, `CURSOR_MODES.md`, `FOR_AGENTS.md`, `INITIALIZATION_PROMPT.md` | Present |
| `BUILD_PLAN.md` labels + emoji status | Present (Sprint 2 maintenance active) |
| Memory: `AGENT_MEMORY.md`, `DECISION_LOG.md`, `KNOWLEDGE_BASE.md` | Present + project-filled |
| `COMPLETED_TASKS.md`, `PROMPT_LIBRARY.md`, `SECURITY.md`, triage/threat/privacy docs | Present |
| Batch commands (20 atomic + 5 super) | Present under `.cursor/commands/` + registry |
| `.cursor/rules/*.mdc` (13 rules) | Present except newer upstream rules |
| Scripts: validate/hygiene/gates/encoding/template-update/feature-gate | Present (~70 scripts) |
| CI: ci, security, CodeQL, dependency-review, scorecard, pages, release-please, stale, weekly-health | Present |
| Dependabot, pre-commit, `.env.example`, `.editorconfig`, `.cursorignore`, session-state example | Present |
| Template tracking: `.template-version`, `.template-update.json` | Present (last check 2026-06-13) |
| Design tokens, `docs/FEATURE_MODULES.md`, `docs/WEB_PROJECT_LAYOUT.md` | Present |

**Verdict:** This is not an unaligned legacy repo. It is a **template child lagging 0.11.1 → 0.15.0**.

---

## 3. What is missing (upstream delta)

### 3.1 High value for this web child (recommend adopt)

| Item | Upstream since | Notes |
|------|----------------|-------|
| `.cursor/hooks.json` + `.cursor/hooks/*` | 0.12 / 0.14 | FOSS hooks: encoding after edit, shell guard, session context |
| `.cursor/skills/*` | 0.12 | Agent skills (gates, hygiene, parallel-scope, etc.) |
| `.cursor/agents/*` | 0.12 | explorer / gate-fixer / verifier stubs |
| `.cursor/worktrees.json`, setup-worktree scripts | 0.12+ | Parallel agent worktrees |
| `.cursor/permissions.json`, `sandbox.json.example`, `cursor-features.json` | 0.12–0.15 | Cursor integrations surface |
| `.cursor/rules/local-compute.mdc` | 0.15 | Local-first compute guidance |
| `.cursor/commands/cleanup.md` | 0.12 | Archive BUILD_PLAN rows after `/build` |
| `docs/FILE_SIZE_GUIDE.md` | 0.12 | 300L static / 150L logic taxonomy |
| Cursor integration docs (`CURSOR_CLI.md`, `CURSOR_INTEGRATIONS.md`, `CURSOR_FEATURE_RADAR.md`, registry JSON, help/CURSOR_FEATURES.md) | 0.12–0.15 | Documentation + radar |
| Scripts: `agent-run.py`, `sync-cursor-features.py`, `check-cursor-hooks.sh`, `check-cursor-integrations.sh`, `plan-parallel-dispatch.sh`, `setup-agent-worktrees.sh`, `build-backlog.sh`, `build-sprint-status.sh`, `check-build-plan-parallel.sh`, `attempt-build-plan-row.sh`, `scripts/lib/` | 0.12–0.14 | Parallel/autonomous `/build` + quiet agent shell |
| `HUMAN_BACKLOG.md` (+ `.example`) | — | Seed from example; move non-automatable HUMAN items |
| Content refresh: `docs/CURSOR_MODES.md`, `docs/FOR_AGENTS.md`, `AGENTS.md`, `docs/BATCH_COMMANDS.md`, `TEMPLATE_INDEX.json`, batch-commands rule | 0.12–0.15 | Local files smaller / drifted vs upstream |
| Bump `.template-version` → `0.15.0`; refresh `.template-update.json` | — | After successful merge of adopted surface |
| README template version string | — | Still says `v0.2.1`; should say `0.11.1` → then `0.15.0` |

### 3.2 Optional / confirm before adopt

| Item | Risk | Recommendation |
|------|------|----------------|
| `.github/workflows/release-please-automerge.yml` + `scripts/setup-automerge-token.*` + `merge-release-please-pr.sh` | Needs PAT/secret; changes release automation | **[HUMAN]** decide — adopt only if automerge is desired |
| Commercial Cursor docs / `commercial-compliance.mdc` / `.cursor/*.commercial.example` | FOSS project; commercial surfaces | **Skip** unless you want reference copies |
| `action.yml`, `packaging/`, `.cursor-plugin/` | Template-maintainer packaging | **Skip** for child product repo |
| Inactive modules (`android`, `python`, …) | Stack bloat | **Skip** — already pruned |
| Blind overwrite of `docs/INITIALIZATION_PROMPT.md` | May erase child nuances | **Merge carefully** / human review |

### 3.3 Project-specific — preserve (do not overwrite)

- `site/**` application code, assets, Playwright/Lighthouse harness
- `AGENT_MEMORY.md`, `DECISION_LOG.md`, `KNOWLEDGE_BASE.md` project entries
- `BUILD_PLAN.md` / `COMPLETED_TASKS.md` LinksLander history (emoji markers already correct)
- ADRs under `docs/adr/`, `docs/RUNBOOK.md`, product README sections
- Always-dark UI decision and related CSS
- `examples/web/` may stay as CI Golden Path; do not replace with inactive stacks

---

## 4. Conflicts & careful migrations

| Conflict | Handling |
|----------|----------|
| README claims bootstrap `v0.2.1` vs `.template-version` `0.11.1` | Fix docs to match reality, then bump after upgrade |
| `COMPLETED_TASKS.md` still uses GitHub `- [x]` checkboxes | Template prefers emoji status in *active* BUILD_PLAN; archive may keep historical format or normalize gradually — **low priority** |
| CI dual-path: `examples/web` + `site/` | Keep both; do not collapse to template-only `examples/web` |
| `examples/web/{node_modules,coverage,dist}` present locally | Ensure gitignored (already); do not commit |
| Parallel-first BUILD_PLAN (upstream 0.12) vs this repo’s sequential-first maintenance board | Adopt tooling/docs; **do not** force parallel sprints onto a quiet maintenance board |
| FOSS hooks may alter agent shell behavior | Adopt with dry-run validation (`check-cursor-hooks.sh`) after copy |
| Release Please already in use | Do not break `release-please.yml` / manifest when adding automerge |

---

## 5. Risk areas

| Risk | Severity | Mitigation |
|------|----------|------------|
| Workflow / required-check churn | High | Diff CI workflows; no disable of branch protection without `[HUMAN]` |
| Release-please automerge secrets | High | Optional; requires human token setup |
| Hook shell denylist blocking legitimate commands | Medium | Review `shell-denylist.txt`; validate with check script |
| Overwriting project memory / INIT prompt | Medium | Merge-only; never blind copy |
| TEMPLATE_INDEX / validate-bootstrap failures after copy | Medium | Run `validate-bootstrap.sh` + autofix loops |
| Secrets / `.env` | Low | Never touch real `.env`; merge `.env.example` only |
| License | Low | Already MIT |

---

## 6. Prioritized alignment plan (Sequential)

### Sprint A — Agent infrastructure (0.12–0.15 FOSS surface) `[AGENT]`

1. Write this gap analysis ✅ (this file)
2. Copy FOSS Cursor integrations: hooks, skills, agents, worktrees helpers, permissions/sandbox/features JSON (skip `*.commercial*`)
3. Add `local-compute.mdc`; refresh drifted rules (`batch-commands`, etc.) from upstream where non-conflicting
4. Add `/cleanup` command; refresh `docs/BATCH_COMMANDS.md` + `docs/help/BATCH_COMMANDS.md`
5. Add `docs/FILE_SIZE_GUIDE.md` + Cursor integration docs (FOSS only)
6. Seed `HUMAN_BACKLOG.md` from example; migrate open HUMAN items from BUILD_PLAN as appropriate
7. Refresh `AGENTS.md`, `docs/CURSOR_MODES.md`, `docs/FOR_AGENTS.md` from upstream **with** LinksLander stack notes preserved
8. Bring missing scripts listed in §3.1; update `TEMPLATE_INDEX.json` via upstream merge + validate
9. Fix README template version; bump `.template-version` → `0.15.0` after gates pass
10. Run `scripts/validate-bootstrap.sh` (+ encoding/hygiene); fix failures in scope

### Sprint B — CI / release optional `[HUMAN` gate then `AGENT]`

1. `[HUMAN]` Approve or decline `release-please-automerge.yml` + automerge token setup
2. If approved: add workflow + scripts; document secret in RUNBOOK / HUMAN_BACKLOG
3. Diff `ci.yml` / `weekly-health-check.yml` / CodeQL pins vs upstream; adopt **safe** fixes only (no Android/Python matrix reintroduction)
4. Refresh Dependabot / scorecard only if upstream has non-breaking improvements

### Sprint C — Process hygiene `[AGENT]`

1. Add short “How agents should work in this repo” to README (pointer to START_HERE)
2. Append decision entry for this upgrade in `DECISION_LOG.md`
3. Update `AGENT_MEMORY.md` Template Provenance at milestone end
4. Refresh `.template-update.json` `last_checked`
5. Leave product backlog (Language Comparison editorial, CSS split) as HUMAN items — out of scope for alignment

---

## 7. High-risk items — human decisions

| # | Item | Decision | Status |
|---|------|----------|--------|
| 1 | FOSS Cursor hooks + skills + agents + worktrees | **Approved** (2026-07-21) | ✅ Adopted |
| 2 | Release Please automerge + PAT | Not approved (default no) | 🔲 Deferred |
| 3 | Commercial Cursor docs/rules | Not approved (skip) | ✅ Skipped |
| 4 | Template packaging (`action.yml`, plugin, `packaging/`) | Not approved (skip) | ✅ Skipped |
| 5 | Refresh drifted docs + LinksLander notes | **Approved** (2026-07-21) | ✅ Done |

---

## 8. Migration notes

### Done in this pass (items 1 + 5)

- FOSS Cursor surface from upstream `v0.15.0`: `.cursor/hooks*`, `skills/`, `agents/`, `worktrees.json`, setup-worktree scripts, `permissions.json`, `sandbox.json.example`, `mcp.foss.example`, `cursor-features.json`, `local-compute.mdc`
- Supporting scripts: `agent-run.py`, cursor hook/integration checkers, parallel/worktree helpers, `scripts/lib/*` used by those tools
- Docs: refreshed `AGENTS.md`, `docs/CURSOR_MODES.md`, `docs/FOR_AGENTS.md` (+ LinksLander appendices); FOSS Cursor integration docs; `FILE_SIZE_GUIDE.md`; `/cleanup` + 26-command registry
- `HUMAN_BACKLOG.md` seeded; `distribution_tier: foss` in stack-selection
- Validated: `check-cursor-hooks --smoke`, `check-cursor-integrations --tier foss`, `validate-bootstrap --quick`

### Still deferred / manual

- `.template-version` remains `0.11.1` (partial adopt — not a full 0.15.0 bump)
- Release Please automerge + PAT (item 2)
- Commercial Cursor surfaces (item 3) and template packaging (item 4)
- Weekly CVE triage and local pre-commit install remain `[HUMAN]`
- Product code under `site/` unchanged

### Critique

- **Null/empty:** Hooks may no-op if Cursor version lacks a hook event — keep FOSS examples that degrade gracefully.
- **Timeouts:** CI poll scripts already exist; do not lengthen waits blindly.
- **Races:** Do not enable automerge and manual Release Please merge simultaneously without a single owner.
- **Exceptions:** validate-bootstrap may fail on TEMPLATE_INDEX path drift — fix index before marking Sprint A done.
- **UTF-8:** On Windows, copy via Python UTF-8 writes; run `scripts/check-file-encoding.py` after bulk import.

---

## 9. Status

| Phase | Status |
|-------|--------|
| Phase 0 — Orient + gap analysis | ✅ Written |
| Phase 1 — Core agent infrastructure | ✅ Partial — items 1 + 5 only |
| Phase 2 — Tooling / CI / security | 🔲 Deferred (automerge / full CI diff) |
| Phase 3 — Stack modules | ✅ Web-only already pruned |
| Phase 4 — Process & memory | ✅ Alignment + decision logged |
