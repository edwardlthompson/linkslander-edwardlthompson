# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.3](https://github.com/edwardlthompson/linkslander-edwardlthompson/compare/v2.1.2...v2.1.3) (2026-07-22)


### Fixed

* **deps:** pin brace-expansion and js-yaml overrides for High alerts ([6a12482](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/6a12482ee21e9602154906162136c5422da3edc0))

## [2.1.2](https://github.com/edwardlthompson/linkslander-edwardlthompson/compare/v2.1.1...v2.1.2) (2026-07-22)


### Changed

* **ci:** mark AUTOMERGE_TOKEN set; fix Windows setup script ([20a88ae](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/20a88aee3c75c663aadd29b1b7fa09f4d2ae5e72))

## [2.1.1](https://github.com/edwardlthompson/linkslander-edwardlthompson/compare/v2.1.0...v2.1.1) (2026-07-22)


### Fixed

* **web:** restore Vitest localStorage under Node 25+ ([bc6c091](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/bc6c0916e539896646324ac6922bb134cf7309d3))


### Changed

* **agents:** adopt FOSS Cursor surface from bootstrap 0.15 ([ae7b0fb](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/ae7b0fb019651bb99a6a5017b5df3249ded74a7f))
* **docs:** slim BUILD_PLAN after v2.1.0 audit archive ([53c034a](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/53c034a9016555c2e92311a32db58bcaefe8fe47))


### Documentation

* mark audit A01 and A07 complete after release merge ([7f76dd2](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/7f76dd256ad792acf82ef4691988ea6e69dcb8e7))
* record /push milestone and Release Please HUMAN gate ([94c5964](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/94c596471c507b8a9df1f8606b9c67a44286ac54))

## [Unreleased]

### Fixed

- npm overrides pin `brace-expansion@1.1.16` and `js-yaml@4.3.0` in `site/` and `examples/web/`
- Release Please auto-merge workflow: set `GH_REPO` so `gh pr merge --auto` works without a checkout

## [2.1.0](https://github.com/edwardlthompson/linkslander-edwardlthompson/compare/v2.0.0...v2.1.0) (2026-07-12)


### Added

* **site:** add Language Comparison page and Word Connections link ([8a3dd16](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/8a3dd16399c4aa0b917cb141300d0d0ca9279ef9))


### Fixed

* **site:** audit remediations and remove cunnilingus row ([84e0f45](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/84e0f452c082205d52c15848590d51fc8654ca19))
* **site:** compress word-connections icon below repo size limit ([535888a](https://github.com/edwardlthompson/linkslander-edwardlthompson/commit/535888a50fa7dc35806ed205bb4ac66af31a4291))

## [2.0.0] - 2026-06-21

### Added

- agent-project-bootstrap scaffolding (Cursor rules, CI guardrails, workspace memory, scripts)
- Published PWA in `site/` with GitHub Actions Pages deploy and custom domain
- `site/` Playwright e2e (7 tests) + Lighthouse CI harness (`site-pwa` job)
- Repository ruleset **main branch protection** with required Security Scan, CodeQL, and CI checks
- ADR-0002 documenting `site/` vs `docs/` split and always-dark UI policy
- Vendored Bootstrap 5.3.3 under `site/vendor/` for offline PWA reliability
- Service worker `matrix-cache-v5` with resilient per-asset caching
- Template parity upgrade to `agent-project-bootstrap` v0.11.1 (batch commands, design tokens, repo hygiene)
- CI jobs: repo-hygiene, feature-gate, upgrade-simulation; workflows: release-please, scorecard, stale
- CSS split into six modules under `site/css/modules/` (base, glass, identity, icons, responsive, animations)
- Automated app releases via Release Please + GitHub Release SBOM workflow

### Changed

- `docs/` reserved for agent documentation; live site served from `site/`
- CodeQL limited to `javascript-typescript` (web-only stack)
- Bootstrap loaded from local vendor path (no CDN runtime dependency)
- `.release-please-manifest.json` tracks app semver; `.template-version` tracks upstream template only

### Removed

- Dead `.theme-toggle-btn` CSS and legacy root icon duplicates
- Pruned python/android/lightroom stacks and related CI jobs
- Monolithic `site/css/style.css` (replaced by modules)

### Security

- Dependabot alerts and security updates enabled
- Private vulnerability reporting enabled
- `rel="noopener noreferrer"` on all external `target="_blank"` links

## [0.2.1] - 2026-06-13 (template upstream history)

### Added

- `scripts/check-workflow-action-ref-format.sh` — local pre-commit guard against bare-semver action refs
- `.github/workflows/health-check.yml` — weekly Monday 07:00 UTC poll of CI + Security Scan + CodeQL on main
- CI `android-build` job — `./gradlew assembleDebug` smoke for `examples/android/`
- Gradle wrapper binaries (`gradlew`, `gradlew.bat`, `gradle-wrapper.jar`) in `examples/android/`
- `KNOWLEDGE_BASE.md` — six structured entries from v0.2.0 CI/security fix round
- `PROMPT_LIBRARY.md` entries 8–9 — workflow action validation and post-push GitHub gate
- Devcontainer `github-cli` feature; postStart runs encoding check + CI gate reminder
- README GitHub CI Gate section; init scripts run `validate-workflow-actions` and remind `check-github-ci`

### Changed

- Normalized root `.gitignore` from UTF-16 to UTF-8; added to encoding scan and pre-commit hook
- SHA-pinned `release.yml` actions: `anchore/sbom-action`, `softprops/action-gh-release`, `actions/attest-build-provenance`
- `docs/SECURITY_TRIAGE.md` — GitHub Actions pin policy, health-check in weekly triage table
- `modules/web/MODULE.md` — Lighthouse 3-run median policy documented
- `modules/android/MODULE.md` — CI assembleDebug documented; fixed corrupted path characters
- `docs/INITIALIZATION_PROMPT.md` — root `.gitignore` in encoding extension list
- `PROMPT_LIBRARY.md` entries 4 and 6 — validate-workflow-actions, three-workflow sign-off

### Fixed

- CI: Lighthouse CI uses 3 runs with median assertion to reduce shared-runner flake while keeping 0.9 performance budget
- Security Scan: pin `aquasecurity/trivy-action` to SHA `a9c7b0f` (v0.36.0); invalid `@0.28.0` ref caused workflow setup failure
- Automation: `scripts/validate-workflow-actions.sh` and `scripts/check-github-ci.sh` (+ `.ps1`) to catch bad action refs and poll required GH workflows before sign-off
- CI: Web TS null narrowing in main.ts, MIT license on web package, scoped Android FOSS grep to Gradle files
- Python: ruff format on greet.py
- Index/pre-commit: CONTRIBUTING.md in TEMPLATE_INDEX; encoding hook covers .ts/.tsx/.toml
- License script: --excludePrivatePackages for private stub packages
- Encoding: normalize UTF-16 index.html and style.css; extend encoding scan to .html/.css

[2.0.0]: https://github.com/edwardlthompson/linkslander-edwardlthompson/releases/tag/v2.0.0
