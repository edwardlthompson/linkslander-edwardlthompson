# Decision Log

> Chronological register of major technical trade-offs, accepted architectures, and rejected alternatives.
> **Treat past entries as immutable history; append only.**

## Format

```markdown
### YYYY-MM-DD — [Title]
- **Status:** Accepted | Rejected | Superseded
- **Context:** ...
- **Decision:** ...
- **Alternatives considered:** ...
- **Consequences:** ...
```

## Entries

### 2026-07-21 — Partial bootstrap FOSS Cursor surface (0.15.0)
- **Status:** Accepted
- **Context:** Child repo was on template `0.11.1`; upstream `agent-project-bootstrap` at `v0.15.0`. Full upgrade deferred; human approved only FOSS Cursor integrations and drifted agent-doc refresh.
- **Decision:** Adopt FOSS hooks/skills/agents/worktrees/`local-compute` + refresh `AGENTS.md` / `CURSOR_MODES.md` / `FOR_AGENTS.md` with LinksLander notes. Skip commercial Cursor docs, plugin packaging, and Release Please automerge. Keep `.template-version` at `0.11.1` until a fuller upgrade pass.
- **Alternatives considered:** Full 0.11.1→0.15.0 cherry-pick in one PR — rejected (scope/risk); skip hooks entirely — rejected (human approved item 1).
- **Consequences:** Agents gain FOSS Cursor surface; `validate-bootstrap --quick` and cursor integration checks green; product `site/` untouched. See `docs/BOOTSTRAP_ALIGNMENT.md`.

### 2026-06-13 — Always-dark UI (no theme toggle)
- **Status:** Accepted
- **Context:** Site previously had a light/dark theme toggle; it was removed for visual consistency with the Matrix aesthetic.
- **Decision:** Keep a fixed always-dark theme. Do not implement `prefers-color-scheme` switching or restore theme toggle UI.
- **Alternatives considered:** System preference theming; manual toggle — both rejected per maintainer preference.
- **Consequences:** Simpler CSS; dead `.theme-toggle-btn` rules removed as cleanup only.

### 2026-06-13 — Sprint 0–1 sign-off
- **Status:** Accepted
- **Context:** Bootstrap adoption and site hardening milestones completed; all required CI workflows green.
- **Decision:** Archive Sprint 0 and Sprint 1 to `COMPLETED_TASKS.md`; activate Sprint 2 ongoing maintenance.
- **Alternatives considered:** Keep sprints open in BUILD_PLAN — rejected (clutters active board).
- **Consequences:** Sprint 3 backlog holds CSS refactor and optional `v2.0.0` release tag.

### 2026-06-13 — Site vs docs directory split
- **Status:** Accepted
- **Context:** GitHub Pages published from `docs/` conflicted with template agent documentation path.- **Decision:** Move published PWA to `site/`; deploy via GitHub Actions; reserve `docs/` for agent docs.
- **Alternatives considered:** Agent docs in `guide/` — rejected (template path deviation).
- **Consequences:** See ADR-0002 at `docs/adr/0002-site-architecture.md`.

### 2026-06-28 — Language Comparison page (Word Connections)
- **Status:** Accepted
- **Context:** Tourists benefit from a side-by-side view of Romance word families vs English/German everyday words; off-topic but frequently shared.
- **Decision:** Add `site/word-connections.html` with 7-column parallel table (Category, EN, DE, ES, PT, IT, FR), sticky headers, and portal link in **Other**; maintain data via `site/scripts/gen-roots-table.py`.
- **Alternatives considered:** External hosted page; 4-column Romance-only layout — rejected (on-site PWA offline + German comparison valued).
- **Consequences:** Service worker `matrix-cache-v7`; 14 site Playwright tests; Release Please minor bump expected.

