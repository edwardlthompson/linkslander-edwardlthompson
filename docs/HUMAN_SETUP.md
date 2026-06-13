# Human Setup Checklist

> One-time GitHub and repository settings required after bootstrap adoption.

## Completed

- [x] **GitHub Pages** — source set to **GitHub Actions**; deploy workflow green; https://edwardlthompson.com loads
- [x] **Dependabot alerts + security updates** — enabled via GitHub API
- [x] **Private vulnerability reporting** — enabled
- [x] **Branch protection** — repository ruleset **main branch protection** (ID `17641917`) active on `refs/heads/main`:
  - Required linear history
  - Block force pushes and branch deletion
  - Required status checks (strict):
    - `Trivy FS Scan` (Security Scan)
    - `Analyze (javascript-typescript)` (CodeQL)
    - `Validate Bootstrap Artifacts` (CI)
    - `Web — Lint, Test, Build` (CI)
    - `Site — PWA E2E and Lighthouse` (CI)
  - Reference config: [`.github/ruleset-main-protection.json`](../.github/ruleset-main-protection.json)

## Dependabot status (2026-06-13)

- **Open security alerts:** 0
- **Open Dependabot PRs:** 0
- **`npm audit` (`site/`, `examples/web/`):** 0 vulnerabilities
- **Version-update PRs:** none yet (weekly schedule; first bumps expected within 7 days)

## Remaining (optional / recommended)

### Repository About

Copy description and topics from [`GITHUB_ABOUT.md`](GITHUB_ABOUT.md) into **Settings → General → About**.

### Local pre-commit (optional)

```powershell
pip install pre-commit
pre-commit install
```

### Weekly maintenance

Run CVE triage per [`SECURITY_TRIAGE.md`](SECURITY_TRIAGE.md) (recommended: Monday):

```powershell
gh api repos/edwardlthompson/linkslander-edwardlthompson/dependabot/alerts?state=open
gh pr list --author "app/dependabot" --state open
pwsh scripts/check-github-ci.ps1 -WaitSeconds 300
```

## Post-Push Verification

After pushing workflow or dependency changes to `main`:

```powershell
pwsh scripts/check-github-ci.ps1 -WaitSeconds 300
```

Required workflows: **CI**, **Security Scan**, **CodeQL**, **Deploy GitHub Pages**.

## Sign-off

When remaining optional items are done, approve Sprint 0 in [`BUILD_PLAN.md`](../BUILD_PLAN.md).
