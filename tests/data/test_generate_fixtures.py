from __future__ import annotations

import subprocess
import sys
from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def test_fixture_generation_is_deterministic(tmp_path: Path) -> None:
    first = tmp_path / "first"
    second = tmp_path / "second"
    for destination in (first, second):
        subprocess.run(
            [sys.executable, "scripts/generate_fixtures.py", "--output-dir", str(destination)],
            cwd=ROOT,
            check=True,
        )
    for relative in ("vector/referencia.geojson", "vector/referencia.csv", "raster/referencia.tif"):
        assert digest(first / relative) == digest(second / relative)
