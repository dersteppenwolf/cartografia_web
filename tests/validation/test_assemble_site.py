"""Verify the static-site assembler publishes a built Slidev deck."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_assemble_site_copies_slides_to_public_route(tmp_path: Path) -> None:
    jekyll = tmp_path / "jekyll"
    slides = tmp_path / "slides"
    output = tmp_path / "site"
    jekyll.mkdir()
    slides.mkdir()
    (jekyll / "index.html").write_text("<h1>Curso</h1>", encoding="utf-8")
    (slides / "index.html").write_text("<h1>Unidad 1</h1>", encoding="utf-8")
    asset = slides / "assets" / "generated"
    asset.mkdir(parents=True)
    (asset / "internet_web.svg").write_text("<svg></svg>", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/assemble_site.py",
            "--jekyll-site",
            str(jekyll),
            "--slides-dir",
            str(slides),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert (output / "index.html").is_file()
    assert (output / "presentaciones" / "unidad-01" / "index.html").is_file()
    assert (output / "presentaciones" / "unidad-01" / "assets" / "generated" / "internet_web.svg").is_file()
