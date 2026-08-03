"""Build and verify the course PMTiles asset with pinned containers."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLANETILER = "ghcr.io/onthegomap/planetiler@sha256:e992a018666bd6f65535b24a3d76c6818fb0fe9f297395d2f7fa7cd8ac6c6751"
PMTILES = "protomaps/go-pmtiles@sha256:06574f01f55a78f78f887bc7ebf729a5c093c0d6e17d9876300cfcb0758b59d3"


def main() -> int:
    source = ROOT / "data/fixtures/vector/referencia.geojson"
    schema = ROOT / "scripts/planetiler-referencia.yml"
    output = ROOT / "data/fixtures/cloud/referencia.pmtiles"
    output.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["docker", "run", "--rm", "-v", f"{source.parent}:/input:ro", "-v", f"{schema.parent}:/schema:ro", "-v", f"{output.parent}:/output", PLANETILER, "generate-custom", "--schema=/schema/planetiler-referencia.yml", "--output=/output/referencia.pmtiles", "--force", "--tmpdir=/output/tmp"], check=True)
    subprocess.run(["docker", "run", "--rm", "-v", f"{output.parent}:/data:ro", PMTILES, "verify", "/data/referencia.pmtiles"], check=True)
    print(f"Built and verified {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
