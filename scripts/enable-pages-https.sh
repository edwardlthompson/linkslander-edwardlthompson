#!/usr/bin/env bash
# Enable GitHub Pages "Enforce HTTPS" when the custom domain is HTTPS-eligible.
# With Cloudflare proxy (orange cloud), GitHub cannot issue a cert — use Cloudflare
# "Always Use HTTPS" instead (health check enforces_https still reports true).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if ! command -v gh >/dev/null 2>&1; then
  echo "FAIL: gh CLI required"
  exit 1
fi

REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
PAGES="$(gh api "repos/${REPO}/pages")"
ENFORCED="$(python3 -c "import json,sys; print(json.load(sys.stdin).get('https_enforced', False))" <<<"$PAGES")"

if [ "$ENFORCED" = "True" ] || [ "$ENFORCED" = "true" ]; then
  echo "OK: GitHub Pages Enforce HTTPS already enabled"
  exit 0
fi

HEALTH=""
for _ in 1 2 3 4 5; do
  HEALTH="$(gh api "repos/${REPO}/pages/health" 2>/dev/null || true)"
  if [ -n "$HEALTH" ] && [ "$HEALTH" != "{}" ]; then
    break
  fi
  sleep 2
done

if [ -z "$HEALTH" ] || [ "$HEALTH" = "{}" ]; then
  echo "WARN: Pages health check unavailable (no custom domain or pending)"
  exit 1
fi

ACTION="$(python3 -c "
import json, sys
health = json.loads(sys.argv[1])
domain = health.get('domain') or {}
eligible = domain.get('is_https_eligible')
enforces = domain.get('enforces_https')
proxied = domain.get('is_proxied')
host = domain.get('host', 'custom domain')

if enforces and not eligible:
    print('cdn_ok')
    print(f'OK: HTTPS enforced for visitors ({host}) via CDN/proxy, not GitHub toggle.')
    print('NOTE: Enable Cloudflare Always Use HTTPS if not already on.')
elif proxied:
    print('blocked_proxy')
    print(f'BLOCKED: {host} is Cloudflare-proxied; GitHub cannot provision a TLS cert.')
    print('Fix: Cloudflare SSL/TLS Edge Certificates -> Always Use HTTPS')
    print('  OR grey-cloud DNS, point A records to GitHub Pages IPs, wait for cert, re-run.')
elif not eligible:
    print('blocked_pending')
    print(f'BLOCKED: {host} not HTTPS-eligible yet (cert pending or DNS misconfigured).')
    print('Wait for GitHub to issue a certificate, then re-run.')
else:
    print('enable')
" "$HEALTH")"

case "$(echo "$ACTION" | head -1)" in
  cdn_ok)
    echo "$ACTION" | tail -n +2
    exit 0
    ;;
  blocked_proxy|blocked_pending)
    echo "$ACTION" | tail -n +2
    exit 1
    ;;
  enable)
    CNAME="$(python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('cname') or '')" <<<"$PAGES")"
    BUILD_TYPE="$(python3 -c "import json,sys; print(json.load(sys.stdin).get('build_type') or 'workflow')" <<<"$PAGES")"
    python3 -c "
import json
print(json.dumps({'build_type': '${BUILD_TYPE}', 'cname': '${CNAME}' or None, 'https_enforced': True}))
" | gh api "repos/${REPO}/pages" -X PUT --input -
    echo "OK: GitHub Pages Enforce HTTPS enabled"
    ;;
esac
