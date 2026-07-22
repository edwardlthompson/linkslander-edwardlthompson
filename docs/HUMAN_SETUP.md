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
    - `Analyze (javascript-typescript) (javascript-typescript)` (CodeQL matrix job name)
    - `Validate Bootstrap Artifacts` (CI)
    - `Web — Lint, Test, Build` (CI)
    - `Site — PWA E2E and Lighthouse` (CI)
  - Reference config: [`.github/ruleset-main-protection.json`](../.github/ruleset-main-protection.json)
- [x] **Allow auto-merge** — enabled (Settings → General → Pull Requests)

## Dependabot status (2026-06-13)

- **Open security alerts:** 0
- **Open Dependabot PRs:** 0
- **`npm audit` (`site/`, `examples/web/`):** 0 vulnerabilities
- **Version-update PRs:** none yet (weekly schedule; first bumps expected within 7 days)

## Remaining (optional / recommended)

### Release Please auto-merge (recommended)

So release PRs merge when checks go green without a human click:

1. Create a classic PAT (`repo` + `workflow`) or fine-grained token (Contents + Pull requests + Workflows) for this repo.
2. Store it as the repo secret `AUTOMERGE_TOKEN`:

```powershell
pwsh scripts/setup-automerge-token.ps1
# or: gh secret set AUTOMERGE_TOKEN
```

3. Workflows already wired:
   - [`.github/workflows/release-please-automerge.yml`](../.github/workflows/release-please-automerge.yml) — queues `gh pr merge --auto` for `release-please--*` PRs
   - [`.github/workflows/release-please.yml`](../.github/workflows/release-please.yml) — uses `AUTOMERGE_TOKEN` when present so PR CI is not stuck in `action_required`

Without the PAT, Release Please PRs from `GITHUB_TOKEN` often need a one-time **Approve and run workflows** click before required checks appear.

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
