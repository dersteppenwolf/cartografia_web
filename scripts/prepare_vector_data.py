"""Convert and validate vector data with the pinned GDAL container."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


GDAL_IMAGE = "ghcr.io/osgeo/gdal@sha256:dab45abca3ca83695d442018692f4f8a0f41955871c57e6101d7f89a92375caa"


def run(command: list[str]) -> None:
    result = subprocess.run(command, check=False)
    if result.returncode:
        raise RuntimeError(f"GDAL command failed with exit code {result.returncode}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--target-crs", default="EPSG:4326")
    parser.add_argument("--simplify-tolerance", type=float, default=0.0)
    args = parser.parse_args()
    source = args.input.resolve()
    output = args.output.resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".tmp.gpkg")
    if temporary.exists():
        temporary.unlink()
    command = [
        "docker", "run", "--rm",
        "-v", f"{source.parent}:/input:ro",
        "-v", f"{output.parent}:/output",
        "-e", "OGR_CURRENT_DATE=2026-08-03T00:00:00Z",
        GDAL_IMAGE,
        "ogr2ogr", "-f", "GPKG", f"/output/{temporary.name}", f"/input/{source.name}",
        "-t_srs", args.target_crs,
        "-makevalid",
    ]
    if args.simplify_tolerance > 0:
        command.extend(["-simplify", str(args.simplify_tolerance)])
    run(command)
    run([
        "docker", "run", "--rm", "-v", f"{output.parent}:/output:ro", GDAL_IMAGE,
        "ogrinfo", "-ro", "-al", "-so", f"/output/{temporary.name}",
    ])
    temporary.replace(output)
    print(f"Prepared {output} in {args.target_crs}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, RuntimeError) as error:
        print(error, file=sys.stderr)
        raise SystemExit(1)
