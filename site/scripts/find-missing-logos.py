#!/usr/bin/env python3
"""Locate and download real product icons for catalog apps."""
from __future__ import annotations

import io
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "js" / "apps-catalog.json"
APPS_DIR = ROOT / "img" / "apps"
MAX_STORE = 120_000

PATTERN = re.compile(
    r"(icon|logo|brand|ic_launcher|mipmap|favicon|mark|app.?icon)",
    re.I,
)
EXT = re.compile(r"\.(svg|png|webp|jpg)$", re.I)


def tree_paths(repo: str) -> list[str]:
    proc = subprocess.run(
        ["gh", "api", f"repos/edwardlthompson/{repo}/git/trees/HEAD?recursive=1"],
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0 or not proc.stdout:
        return []
    data = json.loads(proc.stdout.decode("utf-8", errors="replace"))
    return [t["path"] for t in data.get("tree", []) if t.get("type") == "blob"]


def score(path: str) -> int:
    p = path.lower()
    s = 0
    if "branding/assets/logo-mark.png" in p:
        s += 120
    if "branding/assets/app-icon-512.png" in p:
        s += 115
    if "branding/assets/logo-mark.svg" in p:
        s += 50  # often a Golden Path stub
    if "branding/assets/app-icon-512.svg" in p:
        s += 45
    if "docs/branding" in p and "icon" in p and p.endswith(".png"):
        s += 110
    if "fastlane" in p and p.endswith("/icon.png"):
        s += 105
    if "metadata" in p and p.endswith("/icon.png"):
        s += 100
    if "ic_launcher.png" in p and "xxxhdpi" in p and "round" not in p and "foreground" not in p:
        s += 95
    if "ic_launcher.webp" in p and "xxxhdpi" in p and "round" not in p and "foreground" not in p:
        s += 94
    if "assets/appicon.png" in p.replace("-", "").replace("_", ""):
        s += 90
    if p.endswith("app-icon.svg") or p.endswith("app-icon.png"):
        s += 85
    if p.endswith(".png"):
        s += 12
    if p.endswith(".webp"):
        s += 10
    if p.endswith(".svg"):
        s += 5
    if "foreground" in p or "round" in p:
        s -= 30
    if "readme" in p or "social" in p or "splash" in p or "hero" in p or "banner" in p:
        s -= 50
    if "coins/" in p or "exchanges/" in p or "generic.svg" in p:
        s -= 80
    if "node_modules" in p or "/test" in p or "fixture" in p:
        s -= 100
    if PATTERN.search(p):
        s += 8
    return s


def download(repo: str, path: str) -> bytes | None:
    dl = subprocess.run(
        [
            "gh",
            "api",
            f"repos/edwardlthompson/{repo}/contents/{path}",
            "-H",
            "Accept: application/vnd.github.raw",
        ],
        capture_output=True,
        check=False,
    )
    if dl.returncode != 0 or not dl.stdout:
        return None
    return dl.stdout


def is_stub(data: bytes, path: str = "") -> bool:
    head = data[:600].decode("utf-8", errors="ignore")
    if "Golden Path" in head:
        return True
    if path.endswith(".svg") and b"<image " in data and b"href=\"logo-mark.png\"" in data:
        return True  # external relative image — useless alone
    if path.endswith(".svg") and len(data) < 280 and b"<path d=\"M128 320" in data:
        return True
    if path.endswith(".svg") and len(data) < 280 and b"<path d=\"M16 40" in data:
        return True
    return False


def shrink_image(data: bytes, ext: str) -> tuple[bytes, str] | None:
    try:
        from PIL import Image
    except ImportError:
        return None
    try:
        img = Image.open(io.BytesIO(data))
        img = img.convert("RGBA")
        img.thumbnail((192, 192), Image.Resampling.LANCZOS)
        out = io.BytesIO()
        img.save(out, format="PNG", optimize=True)
        return out.getvalue(), ".png"
    except Exception:
        return None


def needs_better(app: dict) -> bool:
    logo = ROOT / app["logo"]
    if not logo.exists():
        return True
    data = logo.read_bytes()
    if is_stub(data, str(logo)):
        return True
    if len(data) > MAX_STORE and logo.suffix.lower() in {".png", ".jpg", ".webp"}:
        return True
    # weak generic coin icon etc.
    if "generic.svg" in app["logo"]:
        return True
    return False


def pick_logo(repo: str) -> tuple[str, bytes, str] | None:
    paths = [p for p in tree_paths(repo) if EXT.search(p) and PATTERN.search(p)]
    paths.sort(key=score, reverse=True)
    print(f"=== {repo}")
    for p in paths[:8]:
        print(f"  {score(p):3d}  {p}")
    for path in paths:
        data = download(repo, path)
        if not data:
            continue
        if is_stub(data, path):
            print(f"  skip stub {path}")
            continue
        ext = Path(path).suffix.lower()
        if len(data) > MAX_STORE and ext in {".png", ".jpg", ".webp", ".jpeg"}:
            shrunk = shrink_image(data, ext)
            if shrunk:
                data, ext = shrunk
                print(f"  resized {path} -> {len(data)} bytes")
            else:
                print(f"  skip large {path} ({len(data)} bytes)")
                continue
        if len(data) > MAX_STORE:
            print(f"  skip still large {path} ({len(data)} bytes)")
            continue
        return path, data, ext
    print("  (no suitable logo)")
    return None


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    for app in catalog["apps"]:
        if not needs_better(app):
            print(f"keep {app['id']} -> {app['logo']}")
            continue
        picked = pick_logo(app["id"])
        if not picked:
            continue
        path, data, ext = picked
        local = f"{app['id']}{ext}"
        for old in APPS_DIR.glob(f"{app['id']}.*"):
            old.unlink(missing_ok=True)
        (APPS_DIR / local).write_bytes(data)
        app["logo"] = f"img/apps/{local}"
        print(f"  -> {local} from {path} ({len(data)} bytes)")

    CATALOG.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
