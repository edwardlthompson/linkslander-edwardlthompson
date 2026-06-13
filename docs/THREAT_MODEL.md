# Threat Model

> Static PWA threat model for LinksLander. Link security tasks in `BUILD_PLAN.md`.

## Scope

| Item | Value |
|------|-------|
| Project | LinksLander — Edward Lee Thompson Digital Portal |
| Stack | Vanilla JS static PWA, vendored Bootstrap 5.3.3, GitHub Pages |
| Methodology | STRIDE (OWASP ASVS adapted for static client-only site) |

## Trust Boundaries

```text
[Visitor Browser] --> [GitHub Pages CDN] --> [Static files in site/]
        |                      |
   Service Worker cache    Vendored Bootstrap (site/vendor/)
        |
   External link targets (Telegram, PayPal, etc.)
```

No backend, API, database, or user authentication.

## STRIDE Summary

| Threat | Example | Mitigation | Owner |
|--------|---------|------------|-------|
| Spoofing | DNS hijack of edwardlthompson.com | CNAME + HTTPS via GitHub Pages | HUMAN |
| Tampering | Compromised GitHub repo push | Branch protection, CODEOWNERS, required CI | HUMAN |
| Repudiation | N/A (no server-side actions) | — | — |
| Information disclosure | PII in public repo | Contact info is intentionally public; no secrets in VCS | AGENT |
| Denial of service | GitHub Pages outage | Monitor health-check workflow | AUTO |
| Elevation of privilege | Malicious workflow injection | PR review for `.github/`, pinned action SHAs | HUMAN |

## Top Abuse Cases

1. **Vendored dependency drift** — Bootstrap copied under `site/vendor/`; mitigated by Dependabot/manual review cadence and pinning version in `THIRD_PARTY_LICENSES.md`
2. **Secret leakage** — `.env` or tokens committed; mitigated by Gitleaks pre-commit + `.gitignore`
3. **Malicious dependency in dev tooling** — npm devDeps for Playwright/Lighthouse; mitigated by Dependabot + lockfiles + CI scans
4. **Open redirect via external links** — All outbound links are hardcoded `https://` to known platforms; no user-controlled redirects
5. **Service worker cache poisoning** — SW only caches same-origin static assets; no dynamic injection

## Out of Scope

- User accounts, forms, or server-side input
- Theme preference tracking (no telemetry)
- Payment processing (links redirect to PayPal/Venmo/Crypto platforms)

## Security Tasks

- `[HUMAN]` Enable Dependabot alerts + private vulnerability reporting
- `[AUTO]` Trivy FS scan + CodeQL on every push
- `[HUMAN]` Weekly CVE triage per `docs/SECURITY_TRIAGE.md`

## Review Cadence

- `[HUMAN]` Review at each milestone boundary
- `[AGENT]` Update when architecture or data flows change (append ADR reference)
