#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS = ROOT / "img" / "apps"
CATALOG = ROOT / "js" / "apps-catalog.json"
SW = ROOT / "sw.js"
REMOTE = "docs/brand/logo-official.png"


def main() -> None:
    dl = subprocess.run(
        [
            "gh",
            "api",
            f"repos/edwardlthompson/continuum-calendar/contents/{REMOTE}",
            "-H",
            "Accept: application/vnd.github.raw",
        ],
        capture_output=True,
        check=False,
    )
    if dl.returncode != 0 or not dl.stdout:
        raise SystemExit(f"download failed: {dl.stderr!r}")

    for p in APPS.glob("continuum-calendar.*"):
        p.unlink(missing_ok=True)
    dest = APPS / "continuum-calendar.png"
    dest.write_bytes(dl.stdout)

    cat = json.loads(CATALOG.read_text(encoding="utf-8"))
    for app in cat["apps"]:
        if app["id"] == "continuum-calendar":
            app["logo"] = "img/apps/continuum-calendar.png"
    CATALOG.write_text(json.dumps(cat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    text = SW.read_text(encoding="utf-8")
    for old in ("matrix-cache-v39", "matrix-cache-v40"):
        text = text.replace(old, "matrix-cache-v41")
    logos = sorted(
        f"  'img/apps/{p.name}',"
        for p in APPS.iterdir()
        if p.suffix.lower() in {".svg", ".png", ".webp", ".jpg", ".jpeg"}
    )
    out: list[str] = []
    skip = False
    for line in text.splitlines():
        if "'img/apps/" in line:
            if not skip:
                out.extend(logos)
                skip = True
            continue
        out.append(line)
    SW.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"installed {dest} ({dest.stat().st_size} bytes) from {REMOTE}")


if __name__ == "__main__":
    main()
