from __future__ import annotations

from pathlib import Path

LEDGER_PATH = Path(__file__).resolve().parent.parent / "CORPUS.md"


def text() -> str:
    return LEDGER_PATH.read_text(encoding="utf-8")
