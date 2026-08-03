"""Copy the pinned Leaflet distribution and approved fixture into the example."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "node_modules" / "leaflet" / "dist"
TARGET = ROOT / "examples" / "leaflet" / "mapa_basico" / "vendor"
FIXTURE = ROOT / "data" / "fixtures" / "vector" / "referencia.geojson"
DATA_TARGET = ROOT / "examples" / "leaflet" / "mapa_basico" / "data" / "referencia.geojson"


def main() -> int:
    if not SOURCE.is_dir():
        raise FileNotFoundError("Install npm dependencies before preparing Leaflet assets")
    if not FIXTURE.is_file():
        raise FileNotFoundError("Generate approved fixtures before preparing Leaflet assets")
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.mkdir(parents=True)
    for filename in ("leaflet.css", "leaflet.js"):
        shutil.copy2(SOURCE / filename, TARGET / filename)
    shutil.copytree(SOURCE / "images", TARGET / "images")
    DATA_TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(FIXTURE, DATA_TARGET)
    print("Prepared local Leaflet assets and approved vector fixture.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
