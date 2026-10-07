#!/usr/bin/env python3
"""Download logo marks from each catalog app's GitHub repo into site/img/apps/."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "js" / "apps-catalog.json"
APPS_DIR = ROOT / "img" / "apps"

# Prefer square marks that read well on the black plate.
CANDIDATES = (
    "branding/assets/logo-mark.svg",
    "branding/assets/app-icon-512.svg",
    "branding/assets/logo-mark.png",
    "branding/assets/app-icon-512.png",
    "branding/assets/favicon.svg",
    "branding/assets/logo-mark-mono.svg",
)


def gh_api_file(repo: str, path: str) -> bytes | None:
    try:
        proc = subprocess.run(
            [
                "gh",
                "api",
                f"repos/edwardlthompson/{repo}/contents/{path}",
                "--jq",
                ".download_url",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        print("gh CLI not found", file=sys.stderr)
        return None
    if proc.returncode != 0:
        return None
    url = (proc.stdout or "").strip().strip('"')
    if not url or url == "null":
        return None
    dl = subprocess.run(
        ["gh", "api", url, "--jq", "."],
        capture_output=True,
        check=False,
    )
    # gh api on raw download_url may not work; use curl via gh
    dl = subprocess.run(
        ["gh", "api", f"repos/edwardlthompson/{repo}/contents/{path}", "-H", "Accept: application/vnd.github.raw"],
        capture_output=True,
        check=False,
    )
    if dl.returncode != 0 or not dl.stdout:
        return None
    return dl.stdout


def pick_and_download(repo_id: str) -> str | None:
    for remote in CANDIDATES:
        data = gh_api_file(repo_id, remote)
        if not data:
            continue
        ext = Path(remote).suffix.lower() or ".svg"
        local_name = f"{repo_id}{ext}"
        dest = APPS_DIR / local_name
        dest.write_bytes(data)
        print(f"  {repo_id}: {remote} -> {local_name} ({len(data)} bytes)")
        return f"img/apps/{local_name}"
    print(f"  {repo_id}: no branding logo found (keeping existing)")
    return None


def main() -> int:
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    updated = 0
    for app in catalog.get("apps", []):
        repo_id = app["id"]
        print(f"=== {repo_id}")
        logo = pick_and_download(repo_id)
        if logo:
            app["logo"] = logo
            updated += 1
    CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"updated {updated}/{len(catalog.get('apps', []))} logos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
