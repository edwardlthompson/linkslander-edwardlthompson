# Knowledge Base

> Repository of stack-specific edge cases, resolved complex bugs, anti-patterns, and reusable project solutions.
> **Do not populate with generic framework definitions.**

## How to use

1. Add entries only after resolving a non-obvious issue specific to this project.
2. Include: symptom, root cause, fix, and prevention.
3. Link to relevant ADRs or PRs when available.

## Entries

### KB-001 — UTF-16 file corruption on Windows

| Field | Detail |
|-------|--------|
| **Symptom** | `check-json` / `npm` / `json.load` fails; git ignore rules stop working; `.gitignore` shows as untracked patterns not applied |
| **Cause** | Cursor `StrReplace` or Windows editor saves text as UTF-16 LE (NUL bytes between ASCII chars) |
| **Fix** | Rewrite affected files with Python `Path.write_text(..., encoding='utf-8')`; re-run `scripts/check-file-encoding.sh` |
| **Prevention** | Bulk edits on Windows via Python/PowerShell UTF-8 write; include root `.gitignore` in encoding scan |

### KB-002 — Invalid `trivy-action@0.28.0` ref

| Field | Detail |
|-------|--------|
| **Symptom** | Security Scan workflow fails at setup: action version not found |
| **Cause** | Bare semver `@0.28.0` is not a valid GitHub Action ref tag |
| **Fix** | Pin to full SHA: `aquasecurity/trivy-action@a9c7b0f06e461e9d4b4d1711f154ee024b8d7ab8 # v0.36.0` |
| **Prevention** | Run `validate-workflow-actions.sh` pre-push; use `check-workflow-action-ref-format.sh` locally |

### KB-003 — `gh api --silent` false CI failures

| Field | Detail |
|-------|--------|
| **Symptom** | `validate-workflow-actions.sh` fails in CI with unknown `gh` flag error |
| **Cause** | `gh api` has no `--silent` flag; stderr not suppressed correctly |
| **Fix** | Redirect to `/dev/null` instead: `gh api ... >/dev/null 2>&1` |
| **Prevention** | Test validation scripts in CI job with `GH_TOKEN`; avoid undocumented `gh` flags |

### KB-004 — Lighthouse performance flake on shared runners

| Field | Detail |
|-------|--------|
| **Symptom** | CI fails with performance 0.88 vs required 0.90 on a single Lighthouse run |
| **Cause** | GitHub-hosted runner CPU variance; single-run assertion is noisy |
| **Fix** | Set `numberOfRuns: 3` in `.lighthouserc.json`; LHCI uses median; keep `minScore: 0.9` |
| **Prevention** | Do not lower performance budget for CI flake; use multi-run median in `modules/web/MODULE.md` |

### KB-005 — Playwright webServer duplicate build

| Field | Detail |
|-------|--------|
| **Symptom** | E2E hangs or serves stale assets; double `vite build` in CI |
| **Cause** | `webServer` runs build while CI already built; wrong host binding |
| **Fix** | Use `vite preview` on `127.0.0.1`; CI runs `npm run build` once before Playwright |
| **Prevention** | Golden Path `examples/web/playwright.config.ts` documents preview-only webServer |

### KB-006 — TypeScript strict null in render handlers

| Field | Detail |
|-------|--------|
| **Symptom** | `tsc` / ESLint error: Object is possibly null inside `render()` callback |
| **Cause** | `strictNullChecks` + `document.getElementById` return type includes null |
| **Fix** | Assign narrowed ref at module scope: `const root = document.getElementById('root')!` or guard once |
| **Prevention** | Module-level `const root = app` pattern in `examples/web/src/main.ts` |

### KB-007 — Vendored Bootstrap + service worker cache list

| Field | Detail |
|-------|--------|
| **Symptom** | Offline reload shows unstyled page or missing icons; Bootstrap 404 in Network tab |
| **Cause** | Bootstrap was CDN-only; `sw.js` ASSETS list incomplete or `cache.addAll()` failed silently on one bad path |
| **Fix** | Vendor Bootstrap under `site/vendor/bootstrap-5.3.3/`; list all runtime assets in `sw.js`; use `Promise.allSettled` on install; bump `CACHE_NAME` when asset set changes |
| **Prevention** | After adding images or vendor files, grep `site/index.html` for `src=` / `href=` and sync `ASSETS`; run offline smoke in `site/e2e/site.spec.ts` |

## KB — /ship blocked on PR permissions (2026-09-05)

- **Symptom:** Cloud agent cannot `gh pr create` / REST create PR (`403 Resource not accessible by integration`). Direct `git push origin main` rejected: linear history + 5 required status checks.
- **Workaround:** Human opens PR from `cursor/labels-gate-avatar-2c87` → `main`, waits for CI, merges (squash/rebase). Then re-run `/ship` or Release Please path.
- **Local gates:** feature-gate (web/multi after npm ci), license, readme, bootstrap --quick, contacts unit tests — green on the feature branch.

### KB-008 — Under-icon labels invisible despite `.label` markup

| Field | Detail |
|-------|--------|
| **Symptom** | Live portal shows logos only; hover tooltips work; `<span class="label">` present in HTML |
| **Cause** | `.icons li a` started at `opacity: 0` for fade-in; `.section { overflow: hidden }` clipped labels; tiny `.ico` favicons looked undersized vs PNG peers |
| **Fix** | Force `opacity: 1` / `display: block` on `.label`; `overflow: visible` on sections; use full PNG assets for Snapchat/TikTok/YouTube; bump `matrix-cache-v11` (#14) |
| **Prevention** | After label CSS changes, hard-refresh or unregister SW; keep e2e asserts on `.icons .label` text |

### KB-009 — Duplicate CHANGELOG Unreleased blocks Release Please

| Field | Detail |
|-------|--------|
| **Symptom** | Release Please / changelog CI fails or stalls after `feat` on `main`; two `## [Unreleased]` headings |
| **Cause** | Manual Unreleased notes left above the Release Please-managed Unreleased section |
| **Fix** | Keep a single `## [Unreleased]` block; fold notes into it before push (`7c40c2d`) |
| **Prevention** | Grep CHANGELOG for duplicate Unreleased before `/ship` push |

### KB-010 — WSL1 breaks local Node-based gates on Windows

| Field | Detail |
|-------|--------|
| **Symptom** | `feature-gate.sh` / `check-license-compliance.sh` via WSL fail: WSL 1 not supported / cannot find Node |
| **Cause** | Repo scripts expect WSL2 + Node; Windows host may still run native `npm` gates successfully |
| **Fix** | Prefer native PowerShell/`npm` under `site/` and `examples/web/` for local verify; rely on GitHub Actions Feature Gate for authoritative stack gate |
| **Prevention** | Do not treat WSL1 script failure as product regression when CI Feature Gate is green |

### KB-011 — Continuum Calendar logo source

| Field | Detail |
|-------|--------|
| **Symptom** | Apps store Continuum tile showed a generic Fastlane calendar glyph |
| **Cause** | Logo scrape preferred Fastlane metadata art over brand mark |
| **Fix** | Copy `docs/brand/logo-official.png` from continuum-calendar to `site/img/apps/continuum-calendar.png`; bump SW cache |
| **Prevention** | Prefer `docs/brand/` / official logo paths in `scripts/fetch-app-logos.py` before Fastlane icons |

## KB — /ship v2.3.0 regress notes (2026-10-07)

- Release Please PR #18 merged; tag `v2.3.0` published; SBOM + winget stub uploaded to release assets.
- Post-merge Release Please job may fail at "Sync app version on release PR" when no open release PR remains (noise; release already created).
- Template Upgrade Simulation job green on merge commit `337dc4a`.
- Remaining open Critical/High Dependabot: `proxy-addr` (#71 site, #63 examples/web), `compression` (#70 site, #62 examples/web), `source-map-js` (#64 examples/web). Open PRs #19–#21 cover proxy-addr + source-map-js; compression bumps still pending.

