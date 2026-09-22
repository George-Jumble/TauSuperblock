"""Menu layout for the Superblock suite. Tau / Tav folders are not created."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MENU_LAYOUT: dict[str, list[str]] = {
    "astronomical": ["sparc", "desi"],
    "particle": ["cms", "casimir"],
    "geometry": [],
    "bounce": [],
}


def ensure_menu_folders(root: Path | None = None) -> None:
    root = root or PROJECT_ROOT
    for domain, submenus in MENU_LAYOUT.items():
        domain_path = root / "menus" / domain
        domain_path.mkdir(parents=True, exist_ok=True)
        _touch_init(domain_path, domain)
        for name in submenus:
            sub_path = domain_path / name
            sub_path.mkdir(parents=True, exist_ok=True)
            _touch_init(sub_path, f"{domain}/{name}")


def _touch_init(path: Path, rel: str) -> None:
    init = path / "__init__.py"
    if not init.exists():
        init.write_text(f'"""Superblock menu package: {rel}"""\n', encoding="utf-8")
