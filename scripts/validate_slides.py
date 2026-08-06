"""Validate the Unidad 1 Slidev deck under a GitHub Pages-style prefix."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLISHED_BASE = "/cartografia_web/presentaciones/unidad-01/"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="cartografia-web-slides-") as directory:
        output = Path(directory) / "unidad-01"
        command = [
            sys.executable,
            str(ROOT / "scripts" / "build_slides.py"),
            "--baseurl",
            "/cartografia_web",
            "--output",
            str(output),
        ]
        result = subprocess.run(command, cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
        index = output / "index.html"
        if PUBLISHED_BASE not in index.read_text(encoding="utf-8"):
            print(f"Slidev output does not contain expected base: {PUBLISHED_BASE}", file=sys.stderr)
            return 1
        if (output / "assets/slide-001-image-000.jpg").exists():
            print("Slidev output contains a historical capture", file=sys.stderr)
            return 1
        print(f"Validated Slidev deck under {PUBLISHED_BASE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
