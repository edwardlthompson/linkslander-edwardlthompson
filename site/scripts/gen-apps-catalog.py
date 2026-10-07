#!/usr/bin/env python3
"""Generate apps-catalog.json, monogram SVGs, and portal apps brand glyph."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "img" / "apps"


def monogram(path: Path, letters: str) -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-hidden="true">
  <circle cx="32" cy="32" r="28" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
  <text x="32" y="38" text-anchor="middle" font-family="Courier New, Courier, monospace" font-size="20" font-weight="700" fill="#2CFF3B">{letters}</text>
</svg>
"""
    path.write_text(svg, encoding="utf-8")


APPS = [
    {
        "id": "agent-project-bootstrap",
        "name": "Agent Project Bootstrap",
        "group": "Build",
        "category": "Agents",
        "letters": "AB",
        "tagline": "Cursor agent bootstrap for FOSS projects.",
        "description": "GitHub template for bootstrapping FOSS projects with Cursor agents: labeled BUILD_PLAN sprints, CI guardrails, Dependabot triage, and Golden Path stubs for Web, Python, and Android.",
        "platforms": ["Template"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "HermesLauncher",
        "name": "Hermes Launcher",
        "group": "Daily",
        "category": "Inbox",
        "letters": "HL",
        "tagline": "Home-screen inbox for notifications, news, and podcasts.",
        "description": "FOSS Android home-screen inbox. Cards for notifications, news, and podcasts dismiss only via X. Local vault, MIT licensed.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "continuum-calendar",
        "name": "Continuum Calendar",
        "group": "Daily",
        "category": "Calendar",
        "letters": "CC",
        "tagline": "Rolling-week calendar with Google sync.",
        "description": "FOSS cross-platform calendar: Tauri desktop plus Android, rolling week view, Continuum brand, optional Google sync.",
        "platforms": ["Desktop", "Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "AstroAlarm",
        "name": "AstroAlarm",
        "group": "Daily",
        "category": "Alarms",
        "letters": "AA",
        "tagline": "Alarm clock driven by solar and lunar events.",
        "description": "FOSS Android astronomical alarm clock with on-device NOAA/Meeus ephemeris, custom clock wheels, lockscreen math unlock, and a day/night widget.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "OpenShouter",
        "name": "OpenShouter",
        "group": "Daily",
        "category": "Speech",
        "letters": "OS",
        "tagline": "Speaks the alerts you choose so you can look away.",
        "description": "FOSS Android TTS that speaks chosen alerts. Built for people who cannot see or read a screen, and for anyone silencing the phone to check it less. No Play Services.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "MultiAppShare-",
        "name": "Multi App Share",
        "group": "Daily",
        "category": "Sharing",
        "letters": "MS",
        "tagline": "Share one item to many apps in sequence.",
        "description": "Android utility that shares photos, videos, or text across custom app groups in a guided sequential workflow instead of repeating the share sheet.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "SyncMark",
        "name": "SyncMark",
        "group": "Knowledge",
        "category": "Bookmarks",
        "letters": "SM",
        "tagline": "Unify bookmarks across browsers; find dead links.",
        "description": "Local-first cross-browser bookmark unifier with dead-link checking and category suggestions.",
        "platforms": ["Desktop"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "selfchronicle",
        "name": "SelfChronicle",
        "group": "Knowledge",
        "category": "Memory",
        "letters": "SC",
        "tagline": "Local-first personal memory and living biography.",
        "description": "Privacy-first personal memory vault that turns exports and notes into a living biography, key facts, and an auditable timeline you own. PWA plus optional Android wrapper.",
        "platforms": ["PWA", "Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "vault-organizer",
        "name": "Vault Organizer",
        "group": "Knowledge",
        "category": "Notes",
        "letters": "VO",
        "tagline": "Offline Obsidian plugin that auto-tags and files notes.",
        "description": "Offline Obsidian plugin using local FOSS embeddings to auto-tag, categorize, and folder notes without cloud AI.",
        "platforms": ["Obsidian"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "aetherfeed",
        "name": "AetherFeed",
        "group": "Knowledge",
        "category": "Feeds",
        "letters": "AF",
        "tagline": "Encrypted local-first news, podcasts, and booru.",
        "description": "Local-first encrypted news, podcast, and booru client. Read offline, keep stars and playback private, optionally sync opaque backups. No account, no telemetry.",
        "platforms": ["Desktop", "Android"],
        "releaseStatus": "none",
        "forkOf": None,
    },
    {
        "id": "point-and-shoot",
        "name": "Point and Shoot",
        "group": "Create",
        "category": "Camera",
        "letters": "PS",
        "tagline": "FOSS pro camera for Camera2 devices.",
        "description": "FOSS professional camera app with HUD controls, LUT workflows, bracketing, and advanced capture pipelines for capable Android Camera2 devices.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "QuickMediaIngest",
        "name": "Quick Media Ingest",
        "group": "Create",
        "category": "Ingest",
        "letters": "QI",
        "tagline": "Fast media import into dated shoot folders.",
        "description": "FOSS .NET 8 WPF media importer for photographers. Ingest from SD cards, local drives, and FTP into dated shoot folders.",
        "platforms": ["Windows"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "noclip-auto",
        "name": "NoClip Auto",
        "group": "Create",
        "category": "Editing",
        "letters": "NC",
        "tagline": "Auto-fix highlight and shadow clipping in Lightroom.",
        "description": "Lightroom Classic plugin that auto-fixes highlight and shadow clipping. FOSS, local-only, Windows and macOS.",
        "platforms": ["Lightroom"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "hover-icons",
        "name": "Hover Icons",
        "group": "Create",
        "category": "Icons",
        "letters": "HI",
        "tagline": "Photorealistic 3D icon pack from a YAML catalog.",
        "description": "FOSS photorealistic 3D icon pack generated from a locked YAML catalog. Same outline in 2D and 3D; tame or neon from one source. MIT code, CC0 assets.",
        "platforms": ["Assets"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "QRaft",
        "name": "QRaft",
        "group": "Create",
        "category": "Codes",
        "letters": "QR",
        "tagline": "Custom QR codes for widgets and wallpapers.",
        "description": "Craft custom QR codes for widgets, lock-screen glance panels, and full-screen wallpapers. Offline F-Droid-friendly Android app.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "DevPulse",
        "name": "DevPulse",
        "group": "Health",
        "category": "Audit",
        "letters": "DP",
        "tagline": "See which installed apps still have a heartbeat.",
        "description": "Local-only Android scanner that checks Play, F-Droid repos, and public forges so you can find stale software, replacements, or repos worth forking.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "screen-wakelock-detector",
        "name": "Screen Wakelock Detector",
        "group": "Health",
        "category": "Battery",
        "letters": "SW",
        "tagline": "Find what wakes your screen; mute it locally.",
        "description": "See the app and channel that wakes your screen, then mute it in one tap. All local, no cloud.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "OBDForge",
        "name": "OBDForge",
        "group": "Vehicle",
        "category": "Diagnostics",
        "letters": "OF",
        "tagline": "Multi-transport OBD-II live data and diagnostics.",
        "description": "FOSS Android OBD-II diagnostics with BT/USB/WiFi/Ethernet, OBDLink STN support, live data, and local AI assists. F-Droid friendly.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "ExpeditionGauge",
        "name": "Expedition Gauge",
        "group": "Vehicle",
        "category": "HUD",
        "letters": "EG",
        "tagline": "Offline-first automotive HUD with record and playback.",
        "description": "Offline-first automotive HUD with recording, playback, and optional live telemetry. FOSS MIT.",
        "platforms": ["Android"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "chromaflow",
        "name": "ChromaFlow",
        "group": "System",
        "category": "Hardware",
        "letters": "CF",
        "tagline": "Fans, pumps, and lighting in one Linux Mint app.",
        "description": "Control PC fans, pumps, and lighting from a single Linux Mint desktop app.",
        "platforms": ["Linux"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "JanusBoot",
        "name": "JanusBoot",
        "group": "System",
        "category": "Boot",
        "letters": "JB",
        "tagline": "UEFI-first graphical boot manager.",
        "description": "UEFI-first graphical boot manager built around Limine, ESP settings, and janusbootctl.",
        "platforms": ["UEFI"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "3d-game-optimizer",
        "name": "3D Game Optimizer",
        "group": "Play",
        "category": "Gaming",
        "letters": "3D",
        "tagline": "One-click glasses-free 3D PC gaming hub.",
        "description": "Hub that streamlines glasses-free 3D PC gaming setup and optimization in one click.",
        "platforms": ["Windows"],
        "releaseStatus": "available",
        "forkOf": None,
    },
    {
        "id": "starrupture-city-planner",
        "name": "StarRupture City Planner",
        "group": "Play",
        "category": "Planning",
        "letters": "SR",
        "tagline": "Offline PWA to plan StarRupture city layouts.",
        "description": "Offline PWA to plan West-to-East StarRupture city layouts from an unlock checklist. FOSS MIT.",
        "platforms": ["PWA"],
        "releaseStatus": "none",
        "forkOf": None,
    },
    {
        "id": "Google-Messages-For-Desktop",
        "name": "Google Messages for Desktop",
        "group": "Connect",
        "category": "Messaging",
        "letters": "GM",
        "tagline": "Native desktop window for Google Messages.",
        "description": "FOSS Electron app for Google Messages for web on Windows, macOS, and Linux. Native window, tray unread badge, OS toasts, and sms/tel/im compose.",
        "platforms": ["Desktop"],
        "releaseStatus": "available",
        "forkOf": "https://github.com/Google-Messages-For-Desktop/Google-Messages-For-Desktop",
    },
    {
        "id": "takein-sms",
        "name": "TakeIn SMS",
        "group": "Connect",
        "category": "Messaging",
        "letters": "TS",
        "tagline": "Google Voice Takeout to Android SMS.",
        "description": "Windows GUI plus ADB tool that imports Google Voice Takeout archives onto Android as SMS messages.",
        "platforms": ["Windows", "Android"],
        "releaseStatus": "none",
        "forkOf": None,
    },
    {
        "id": "linear-trend-spotter",
        "name": "Linear Trend Spotter",
        "group": "Markets",
        "category": "Trading",
        "letters": "LT",
        "tagline": "Crypto scanner with momentum gates and dashboard.",
        "description": "Python scanner for liquid exchange-listed coins: volume and momentum gates, uniformity scoring, strategy backtests, and a public JSON dashboard.",
        "platforms": ["Python", "PWA"],
        "releaseStatus": "none",
        "forkOf": None,
    },
    {
        "id": "trendalgo-bot",
        "name": "TrendAlgo Bot",
        "group": "Markets",
        "category": "Trading",
        "letters": "TB",
        "tagline": "Self-hosted crypto algo bot stack.",
        "description": "Self-hosted crypto algo stack with Freqtrade, LTS Scanner, portfolio tracker, and AI-recommended strategies.",
        "platforms": ["Server"],
        "releaseStatus": "available",
        "forkOf": None,
    },
]

GROUP_ORDER = [
    "Build",
    "Daily",
    "Knowledge",
    "Create",
    "Health",
    "Vehicle",
    "System",
    "Play",
    "Connect",
    "Markets",
]

CATEGORY_ORDER = {
    "Build": ["Agents"],
    "Daily": ["Inbox", "Calendar", "Alarms", "Speech", "Sharing"],
    "Knowledge": ["Bookmarks", "Memory", "Notes", "Feeds"],
    "Create": ["Camera", "Ingest", "Editing", "Icons", "Codes"],
    "Health": ["Audit", "Battery"],
    "Vehicle": ["Diagnostics", "HUD"],
    "System": ["Hardware", "Boot"],
    "Play": ["Gaming", "Planning"],
    "Connect": ["Messaging"],
    "Markets": ["Trading"],
}


def main() -> None:
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    for app in APPS:
        monogram(APPS_DIR / f"{app['id']}.svg", app["letters"])
        entries.append(
            {
                "id": app["id"],
                "name": app["name"],
                "group": app["group"],
                "category": app["category"],
                "tagline": app["tagline"],
                "description": app["description"],
                "logo": f"img/apps/{app['id']}.svg",
                "repoUrl": f"https://github.com/edwardlthompson/{app['id']}",
                "releasesUrl": f"https://github.com/edwardlthompson/{app['id']}/releases",
                "releaseStatus": app["releaseStatus"],
                "platforms": app["platforms"],
                "forkOf": app["forkOf"],
            }
        )

    catalog = {
        "groupOrder": GROUP_ORDER,
        "categoryOrder": CATEGORY_ORDER,
        "apps": entries,
    }
    (ROOT / "js" / "apps-catalog.json").write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    apps_brand = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-hidden="true">
  <rect x="10" y="10" width="18" height="18" rx="4" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
  <rect x="36" y="10" width="18" height="18" rx="4" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
  <rect x="10" y="36" width="18" height="18" rx="4" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
  <rect x="36" y="36" width="18" height="18" rx="4" fill="none" stroke="#2CFF3B" stroke-width="2.5"/>
</svg>
"""
    (ROOT / "img" / "brands" / "apps.svg").write_text(apps_brand, encoding="utf-8")
    print(f"wrote {len(entries)} apps and brand glyph")


if __name__ == "__main__":
    main()
