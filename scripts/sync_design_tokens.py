"""Synchronize the canonical course tokens into the MapLibre application."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/assets/css/tokens.css"
TARGET = ROOT / "examples/maplibre/app/src/styles/tokens.css"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source = SOURCE.read_text(encoding="utf-8")
    if args.check:
        if TARGET.read_text(encoding="utf-8") != source:
            print(f"{TARGET.relative_to(ROOT)} no coincide con {SOURCE.relative_to(ROOT)}", file=sys.stderr)
            return 1
        return 0
    TARGET.write_text(source, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
