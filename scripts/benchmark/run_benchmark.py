"""Measure repeatable HTTP transport baselines for the course delivery routes."""

from __future__ import annotations

import argparse
import json
import statistics
import time
from datetime import UTC, datetime
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[2]
ROUTES = {
    "vector": {
        "geojson": "http://localhost:18080/geoserver/ogc/features/v1/collections/curso:referencia/items",
        "pmtiles": "http://localhost:18081/assets/referencia.pmtiles",
    },
    "raster": {
        "wms": "http://localhost:18080/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=curso:referencia&bbox=-74.12,4.70,-74.04,4.74&width=256&height=256&srs=EPSG:4326&format=image/png",
        "cog": "http://localhost:18081/assets/referencia.cog.tif",
    },
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--route", choices=ROUTES, required=True)
    parser.add_argument("--runs", type=int, default=5)
    parser.add_argument("--output", type=Path, default=ROOT / ".reports/benchmark.json")
    args = parser.parse_args()
    if args.runs < 5:
        raise ValueError("--runs must be at least 5")
    results: dict[str, list[dict[str, float | int]]] = {}
    for name, url in ROUTES[args.route].items():
        samples = []
        for _ in range(args.runs):
            headers = {"Range": "bytes=0-65535"} if name in {"pmtiles", "cog"} else {}
            started = time.perf_counter()
            response = requests.get(url, headers=headers, timeout=30)
            elapsed = (time.perf_counter() - started) * 1000
            response.raise_for_status()
            samples.append({"milliseconds": round(elapsed, 3), "bytes": len(response.content), "status": response.status_code})
        results[name] = samples
    report = {
        "generated_at": datetime.now(UTC).isoformat(),
        "route": args.route,
        "runs": args.runs,
        "measurement": "HTTP transport baseline; browser rendering is measured separately.",
        "results": results,
        "median_milliseconds": {name: round(statistics.median(sample["milliseconds"] for sample in samples), 3) for name, samples in results.items()},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["median_milliseconds"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
