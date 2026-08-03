"""Build and inspect a Cloud Optimized GeoTIFF from the synthetic raster."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
GDAL = "ghcr.io/osgeo/gdal@sha256:dab45abca3ca83695d442018692f4f8a0f41955871c57e6101d7f89a92375caa"
SOURCE = ROOT / "data" / "fixtures" / "raster" / "referencia.tif"
OUTPUT = ROOT / "infra" / "prototypes" / "assets" / "referencia.cog.tif"


def run(arguments: list[str]) -> None:
    subprocess.run(arguments, check=True)


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    run([
        "docker", "run", "--rm", "-v", f"{SOURCE.parent}:/input:ro", "-v", f"{OUTPUT.parent}:/output", GDAL,
        "gdal_translate", "-of", "COG", "-co", "COMPRESS=DEFLATE", "-co", "BLOCKSIZE=256",
        f"/input/{SOURCE.name}", f"/output/{OUTPUT.name}",
    ])
    run([
        "docker", "run", "--rm", "-v", f"{OUTPUT.parent}:/output:ro", GDAL,
        "gdalinfo", "-json", f"/output/{OUTPUT.name}",
    ])
    print(f"Built {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
