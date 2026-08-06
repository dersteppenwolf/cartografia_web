"""Verify the published Slidev build can be reproduced under a base path."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_validate_slides_builds_prefixed_output() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_slides.py"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Validated Slidev deck under /cartografia_web/presentaciones/unidad-01/" in result.stdout
