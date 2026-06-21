#!/usr/bin/env bash
# Sync site/package.json version from .release-please-manifest.json (child app releases).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [ ! -f .release-please-manifest.json ]; then
  echo "MISSING: .release-please-manifest.json"
  exit 1
fi

if [ ! -f site/package.json ]; then
  echo "SKIP: site/package.json not found"
  exit 0
fi

VERSION="$(python3 -c "import json; print(json.load(open('.release-please-manifest.json'))['.'].strip())")"

if [ -z "$VERSION" ]; then
  echo "FAIL: empty version in manifest"
  exit 1
fi

python3 <<PY
import json
from pathlib import Path

version = "${VERSION}"
path = Path("site/package.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["version"] = version
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
PY

echo "Synced app version to ${VERSION} (site/package.json)"
