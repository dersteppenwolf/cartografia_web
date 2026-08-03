"""Build and inspect the course Cloud Optimized GeoTIFF with GDAL."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GDAL = "ghcr.io/osgeo/gdal@sha256:dab45abca3ca83695d442018692f4f8a0f41955871c57e6101d7f89a92375caa"


def main() -> int:
    source = ROOT / "data/fixtures/raster/referencia.tif"
    output = ROOT / "data/fixtures/cloud/referencia.cog.tif"
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["docker", "run", "--rm", "-v", f"{source.parent}:/input:ro", "-v", f"{output.parent}:/output", GDAL, "gdal_translate", "-of", "COG", "-co", "COMPRESS=DEFLATE", "-co", "BLOCKSIZE=256", f"/input/{source.name}", f"/output/{output.name}"], check=True)
    subprocess.run(["docker", "run", "--rm", "-v", f"{output.parent}:/output:ro", GDAL, "gdalinfo", "-json", f"/output/{output.name}"], check=True)
    print(f"Built and inspected {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
