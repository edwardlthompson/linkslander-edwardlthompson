#!/usr/bin/env bash
# Version sync: template upstream vs app release (child repos decouple the two).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ ! -f .release-please-manifest.json ] || [ ! -f .template-version ]; then
  echo "MISSING: version manifest or .template-version"
  exit 1
fi

MANIFEST="$(python3 -c "import json; print(json.load(open('.release-please-manifest.json'))['.'].strip())")"
TEMPLATE_VERSION="$(tr -d '[:space:]' < .template-version)"
IDX="$(python3 -c "import json; print(json.load(open('TEMPLATE_INDEX.json'))['template_version'])")"

if [ "$IDX" != "$TEMPLATE_VERSION" ]; then
  echo "FAIL: TEMPLATE_INDEX template_version ($IDX) != .template-version ($TEMPLATE_VERSION)"
  exit 1
fi

if [ -f site/package.json ]; then
  APP_VERSION="$(python3 -c "import json; print(json.load(open('site/package.json'))['version'].strip())")"
  if [ "$MANIFEST" != "$APP_VERSION" ]; then
    echo "FAIL: release-please manifest ($MANIFEST) != site/package.json ($APP_VERSION)"
    echo "Fix: bash scripts/sync-app-version.sh"
    exit 1
  fi
  echo "Version sync OK (app ${MANIFEST}, template ${TEMPLATE_VERSION})"
else
  if [ "$MANIFEST" != "$TEMPLATE_VERSION" ]; then
    echo "FAIL: .template-version ($TEMPLATE_VERSION) != manifest ($MANIFEST)"
    echo "Fix: bash scripts/sync-template-version.sh"
    exit 1
  fi
  echo "Template version sync OK ($TEMPLATE_VERSION)"
fi
