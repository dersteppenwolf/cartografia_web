"""Smoke test WMS, WFS, OGC API - Features, and MVT for one prototype layer."""

from __future__ import annotations

import sys

import requests


BASE = "http://localhost:18080/geoserver"
ENDPOINTS = {
    "WMS": f"{BASE}/ows?service=WMS&request=GetCapabilities",
    "WFS": f"{BASE}/ows?service=WFS&request=GetCapabilities",
    "Features": f"{BASE}/ogc/features/v1/collections/curso:referencia/items",
    "MVT": f"{BASE}/ows?service=WMS&version=1.1.1&request=GetMap&layers=curso:referencia&bbox=-20037508,-20037508,20037508,20037508&width=256&height=256&srs=EPSG:3857&format=application/vnd.mapbox-vector-tile",
}


def main() -> int:
    for name, url in ENDPOINTS.items():
        response = requests.get(url, timeout=30)
        if response.status_code != 200 or not response.content:
            print(f"{name} failed: {response.status_code} {response.text[:300]}", file=sys.stderr)
            return 1
        if name == "MVT" and response.headers.get("Content-Type") != "application/vnd.mapbox-vector-tile":
            print(f"MVT returned unexpected content type: {response.headers.get('Content-Type')}", file=sys.stderr)
            return 1
    print("Validated WMS, WFS, OGC API - Features, and MVT for curso:referencia.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
