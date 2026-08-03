from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_prepare_vector_data_creates_geopackage(tmp_path: Path) -> None:
    outputs = [tmp_path / "first.gpkg", tmp_path / "second.gpkg"]
    for output in outputs:
        subprocess.run(
            [
                sys.executable,
                "scripts/prepare_vector_data.py",
                "--input",
                "data/fixtures/vector/referencia.geojson",
                "--output",
                str(output),
            ],
            cwd=ROOT,
            check=True,
        )
        assert output.is_file()
        assert output.stat().st_size > 0
    assert outputs[0].read_bytes() == outputs[1].read_bytes()
