#!/usr/bin/env bash
# Count open Critical/High Dependabot alerts (paginated).
# Usage: scripts/count-critical-high-dependabot.sh
# Exit 0 prints count to stdout; exit 1 on API/auth error.
set -euo pipefail

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: gh CLI required" >&2
  exit 1
fi

REPO="${GITHUB_REPO:-$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)}"
if [ -z "$REPO" ]; then
  echo "ERROR: gh auth required" >&2
  exit 1
fi

if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else PY=python3; fi

COUNT="$("$PY" - "$REPO" << 'PY'
import json, subprocess, sys

repo = sys.argv[1]
proc = subprocess.run(
    ["gh", "api", "--paginate", "--slurp",
     f"repos/{repo}/dependabot/alerts?state=open&per_page=100"],
    capture_output=True, text=True,
)
if proc.returncode != 0:
    print("error", file=sys.stderr)
    raise SystemExit(1)
raw = proc.stdout.strip() or "[]"
alerts = json.loads(raw)
if isinstance(alerts, list) and alerts and isinstance(alerts[0], list):
    alerts = [a for page in alerts for a in page]
total = sum(
    1 for a in alerts
    if (a.get("security_vulnerability") or {}).get("severity", "").lower() in ("critical", "high")
)
print(total)
PY
)"

echo "$COUNT"
