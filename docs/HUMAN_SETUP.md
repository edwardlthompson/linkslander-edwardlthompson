# Human Setup Checklist

> One-time GitHub and repository settings required after bootstrap adoption.
> These steps cannot be fully automated by the agent.

## GitHub Pages (required)

1. Open **Settings → Pages → Build and deployment**
2. Set **Source** to **GitHub Actions** (not "Deploy from branch /docs")
3. After first push to `main`, confirm **Deploy GitHub Pages** workflow succeeds
4. Verify https://edwardlthompson.com loads and custom domain shows **DNS check valid**

## Security (required)

1. **Settings → Code security and analysis**
   - Enable **Dependabot alerts**
   - Enable **Dependabot security updates**
   - Enable **Private vulnerability reporting**
2. Run weekly CVE triage per [`SECURITY_TRIAGE.md`](SECURITY_TRIAGE.md) (recommended: Monday)

## Branch Protection (required)

**Settings → Branches → Add rule for `main`:**

- Require status checks before merging:
  - `CI` (or all CI jobs)
  - `Security Scan`
  - `CodeQL`
- Require linear history
- Do not allow force pushes

## Repository About (recommended)

Copy description and topics from [`GITHUB_ABOUT.md`](GITHUB_ABOUT.md) into **Settings → General → About**.

## Local Development (optional)

```powershell
pip install pre-commit
pre-commit install
```

## Post-Push Verification

After pushing workflow changes to `main`:

```powershell
pwsh scripts/check-github-ci.ps1 -WaitSeconds 300
```

Confirm all required workflows are green: **CI**, **Security Scan**, **CodeQL**, **Deploy GitHub Pages**.

## Sign-off

When complete, check off Sprint 0 human tasks in [`BUILD_PLAN.md`](../BUILD_PLAN.md) and approve Sprint 0.
