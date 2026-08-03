"""Parse XML and SLD files that are not in blocked historical material."""

from __future__ import annotations

from pathlib import Path

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    paths = [*ROOT.glob("docs/**/*.xml"), *ROOT.glob("docs/**/*.sld")]
    for path in paths:
        etree.parse(str(path))
    print(f"Parsed {len(paths)} approved XML or SLD file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
