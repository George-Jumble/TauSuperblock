"""Deprecated Tau entry. The live engine is sb_engine via research_tool.py."""

from __future__ import annotations

import sys


def main() -> None:
    print(
        "Tau-Superblock runner is retired.\n"
        "Live corpus is Superblock / Mirron only.\n"
        "Run:  python research_tool.py --help",
        file=sys.stderr,
    )
    sys.exit(2)


if __name__ == "__main__":
    main()
