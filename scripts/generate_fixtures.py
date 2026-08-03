"""Generate deterministic vector, tabular, and raster course fixtures."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import os
from pathlib import Path

RASTERIO_SPEC = importlib.util.find_spec("rasterio")
if RASTERIO_SPEC is None or RASTERIO_SPEC.origin is None:
    raise RuntimeError("rasterio is required to generate the raster fixture")
PROJ_DATA = Path(RASTERIO_SPEC.origin).parent / "proj_data"
os.environ["PROJ_DATA"] = str(PROJ_DATA)
os.environ["PROJ_LIB"] = str(PROJ_DATA)

import numpy as np  # noqa: E402
import rasterio  # noqa: E402
from rasterio.transform import from_origin  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "data" / "fixtures")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    vector_dir = output / "vector"
    raster_dir = output / "raster"
    vector_dir.mkdir(parents=True, exist_ok=True)
    raster_dir.mkdir(parents=True, exist_ok=True)

    features = []
    rows = []
    for index, value in enumerate((12, 18, 25, 31), start=1):
        longitude = -74.10 + (index - 1) * 0.02
        latitude = 4.70 + (index - 1) * 0.01
        features.append({
            "type": "Feature",
            "id": f"zona-{index}",
            "properties": {"id": f"zona-{index}", "nombre": f"Zona {index}", "valor": value},
            "geometry": {"type": "Point", "coordinates": [longitude, latitude]},
        })
        rows.append({"id": f"zona-{index}", "nombre": f"Zona {index}", "valor": value})
    geojson_path = vector_dir / "referencia.geojson"
    geojson_path.write_text(
        json.dumps({"type": "FeatureCollection", "features": features}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    csv_path = vector_dir / "referencia.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=["id", "nombre", "valor"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    raster_path = raster_dir / "referencia.tif"
    array = np.arange(16, dtype="uint8").reshape((4, 4))
    with rasterio.open(
        raster_path,
        "w",
        driver="GTiff",
        height=4,
        width=4,
        count=1,
        dtype="uint8",
        crs="EPSG:4326",
        transform=from_origin(-74.12, 4.74, 0.01, 0.01),
        nodata=0,
    ) as dataset:
        dataset.write(array, 1)
        dataset.update_tags(ACQUIRED="2026-08-03")

    for path in (geojson_path, csv_path, raster_path):
        display_path = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"{display_path} {sha256(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
