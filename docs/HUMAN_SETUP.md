# Human Setup Checklist

> One-time GitHub and repository settings required after bootstrap adoption.

## Completed

- [x] **GitHub Pages** — source set to **GitHub Actions**; deploy workflow green; https://edwardlthompson.com loads
- [x] **HTTPS for visitors** — enforced via Cloudflare (`http://` → `https://` redirect; GitHub health `enforces_https: true`). GitHub’s **Enforce HTTPS** toggle stays off while the domain is Cloudflare-proxied (`is_https_eligible: false`); see below.
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

### GitHub Pages Enforce HTTPS toggle (Cloudflare)

`edwardlthompson.com` uses **Cloudflare proxy** (orange cloud). GitHub cannot issue a TLS certificate in that mode, so **Settings → Pages → Enforce HTTPS** remains disabled and the API returns *“The certificate does not exist yet”*.

**Current state (2026-06-21):** Visitors are already on HTTPS — Cloudflare redirects HTTP to HTTPS and GitHub’s DNS health reports `enforces_https: true`.

**Option A — keep Cloudflare (recommended):** In Cloudflare → **SSL/TLS → Edge Certificates**, confirm **Always Use HTTPS** is on.

**Option B — GitHub-managed cert:** Grey-cloud the apex/`www` records, point A records to GitHub Pages IPs (`185.199.108.153`–`111.153`), wait for GitHub to provision the cert (up to ~24h), then:

```powershell
bash scripts/enable-pages-https.sh
```

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
