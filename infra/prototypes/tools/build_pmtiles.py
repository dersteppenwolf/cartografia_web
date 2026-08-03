"""Generate and verify PMTiles with the pinned Planetiler and PMTiles CLIs."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PLANETILER = "ghcr.io/onthegomap/planetiler@sha256:e992a018666bd6f65535b24a3d76c6818fb0fe9f297395d2f7fa7cd8ac6c6751"
PMTILES = "protomaps/go-pmtiles@sha256:06574f01f55a78f78f887bc7ebf729a5c093c0d6e17d9876300cfcb0758b59d3"
SOURCE = ROOT / "data" / "fixtures" / "vector" / "referencia.geojson"
SCHEMA = ROOT / "infra" / "prototypes" / "tools" / "referencia.yml"
OUTPUT = ROOT / "infra" / "prototypes" / "assets" / "referencia.pmtiles"


def main() -> int:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "docker", "run", "--rm", "-v", f"{SOURCE.parent}:/input:ro", "-v", f"{SCHEMA.parent}:/schema:ro", "-v", f"{OUTPUT.parent}:/output", PLANETILER,
        "generate-custom", "--schema=/schema/referencia.yml", "--output=/output/referencia.pmtiles", "--force",
        "--tmpdir=/output/tmp",
    ], check=True)
    subprocess.run(["docker", "run", "--rm", "-v", f"{OUTPUT.parent}:/data:ro", PMTILES, "verify", "/data/referencia.pmtiles"], check=True)
    print(f"Built {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
