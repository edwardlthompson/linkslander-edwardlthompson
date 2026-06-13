# Runbook

> Operational guide for deploy, rollback, and incident response — LinksLander PWA.

## Health Checks

Static PWA — no backend endpoints. Verify:

| Check | Command / URL | Expected |
|-------|---------------|----------|
| Site loads | `curl -I https://edwardlthompson.com` | `200 OK` |
| Custom domain | `site/CNAME` contains `edwardlthompson.com` | Matches DNS |
| Service worker | DevTools → Application → Service Workers | Registered, no errors |
| Offline mode | DevTools → Network → Offline, reload | Page renders from cache |
| CI site tests | `cd site && npm run test:e2e` | All pass |

## Deploy

1. `[AUTO]` CI green on `main` (includes **Deploy GitHub Pages** workflow)
2. `[AUTO]` Push to `main` triggers `.github/workflows/pages.yml`
3. `[AUTO]` GitHub Actions uploads `site/` artifact and publishes to Pages
4. `[HUMAN]` Verify https://edwardlthompson.com within 2–5 minutes

### First-time Pages migration

1. Repo **Settings → Pages → Build and deployment**
2. Source: **GitHub Actions** (not "Deploy from branch /docs")
3. After first successful deploy, confirm custom domain shows **DNS check valid**

## Rollback

1. `git revert` the offending commit on `main` (or reset to last known-good SHA)
2. Push to `main` — Pages workflow redeploys previous `site/` content
3. Confirm https://edwardlthompson.com loads correctly
4. Log user-impacting incidents in `DECISION_LOG.md`

## Common Failures

| Symptom | Check | Fix |
|---------|-------|-----|
| 404 on edwardlthompson.com | Pages workflow run + Settings source | Switch to GitHub Actions source |
| Missing icons offline | `site/sw.js` ASSETS list vs actual files | Align cache manifest |
| CI failing on lint | Local `pre-commit run --all-files` | Fix and push |
| Lighthouse budget fail | `cd site && npm run lighthouse` | Optimize assets or investigate CDN flake |
| Dependabot alert | `docs/SECURITY_TRIAGE.md` | Merge bump PR |

## Backup & Restore

| Target | RPO | RTO | Procedure |
|--------|-----|-----|-----------|
| Site content | N/A (git) | Immediate | `git clone` + checkout known-good tag |
| Custom domain DNS | External | Provider-dependent | Restore CNAME at DNS registrar |

## SLOs

| Service | SLI | Target |
|---------|-----|--------|
| Site availability | HTTP 200 on `/` | 99.9% |
| Page load (Lighthouse perf) | CI median score | ≥ 0.9 |

## Escalation

1. Check `BUILD_PLAN.md` Ongoing Maintenance
2. Review `docs/SECURITY_TRIAGE.md` for security issues
3. Contact `@edwardlthompson` per `.github/CODEOWNERS`

## Secret Rotation

This static site has no production secrets. If GitHub tokens or repo access is compromised:

1. **`[HUMAN]`** Revoke compromised tokens immediately
2. **`[HUMAN]`** Review branch protection and CODEOWNERS
3. **`[HUMAN]`** Log incident in `DECISION_LOG.md`
