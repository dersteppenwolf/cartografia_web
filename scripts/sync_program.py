"""Generate the Jekyll copy of the canonical course program."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Programa.md"
TARGET = ROOT / "docs" / "programa.md"
FRONT_MATTER = "---\nlayout: default\ntitle: Programa\npermalink: /programa/\n---\n\n"


def main() -> int:
    TARGET.write_text(FRONT_MATTER + SOURCE.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
