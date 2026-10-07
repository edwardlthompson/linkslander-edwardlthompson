#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "img" / "apps"
CATALOG = ROOT / "js" / "apps-catalog.json"
SW = ROOT / "sw.js"

LETTERS = {
    "agent-project-bootstrap": "AB",
    "hover-icons": "HI",
    "JanusBoot": "JB",
}


def monogram(letters: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-hidden="true">
  <circle cx="32" cy="32" r="28" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
  <text x="32" y="38" text-anchor="middle" font-family="Courier New, Courier, monospace" font-size="20" font-weight="700" fill="#2CFF3B">{letters}</text>
</svg>
"""


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    for app_id, let in LETTERS.items():
        for old in APPS_DIR.glob(f"{app_id}.*"):
            old.unlink(missing_ok=True)
        (APPS_DIR / f"{app_id}.svg").write_text(monogram(let), encoding="utf-8")
        for app in catalog["apps"]:
            if app["id"] == app_id:
                app["logo"] = f"img/apps/{app_id}.svg"
                print("restored", app_id)

    CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    logos = sorted(
        f"  'img/apps/{p.name}',"
        for p in APPS_DIR.iterdir()
        if p.suffix.lower() in {".svg", ".png", ".webp", ".jpg", ".jpeg"}
    )
    text = SW.read_text(encoding="utf-8")
    # Replace existing img/apps/* lines in ASSETS
    new_assets = []
    skip_apps = False
    for line in text.splitlines():
        if "'img/apps/" in line:
            if not skip_apps:
                new_assets.extend(logos)
                skip_apps = True
            continue
        new_assets.append(line)
    SW.write_text("\n".join(new_assets) + "\n", encoding="utf-8")
    print(f"sw.js logos: {len(logos)}")


if __name__ == "__main__":
    main()
