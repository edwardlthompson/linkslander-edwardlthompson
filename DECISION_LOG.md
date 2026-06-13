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

- **Status:** Accepted
- **Context:** GitHub Pages published from `docs/` conflicted with template agent documentation path.
- **Decision:** Move published PWA to `site/`; deploy via GitHub Actions; reserve `docs/` for agent docs.
- **Alternatives considered:** Agent docs in `guide/` — rejected (template path deviation).
- **Consequences:** See ADR-0002 at `docs/adr/0002-site-architecture.md`.
