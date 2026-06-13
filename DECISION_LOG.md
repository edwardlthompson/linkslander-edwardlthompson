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

### 2026-06-13 — Site vs docs directory split
- **Status:** Accepted
- **Context:** GitHub Pages published from `docs/` conflicted with template agent documentation path.
- **Decision:** Move published PWA to `site/`; deploy via GitHub Actions; reserve `docs/` for agent docs.
- **Alternatives considered:** Agent docs in `guide/` — rejected (template path deviation).
- **Consequences:** See ADR-0002 at `docs/adr/0002-site-architecture.md`.
