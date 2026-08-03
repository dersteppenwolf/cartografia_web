"""Verify the locally reproducible course stack."""

from __future__ import annotations

import sys

import requests


GEOSERVER = "http://localhost:18080/geoserver"
STATIC = "http://localhost:18081/assets"
ENDPOINTS = {
    "WMS": f"{GEOSERVER}/ows?service=WMS&request=GetCapabilities",
    "WFS": f"{GEOSERVER}/ows?service=WFS&request=GetCapabilities",
    "OGC API - Features": f"{GEOSERVER}/ogc/features/v1",
    "Collections": f"{GEOSERVER}/ogc/features/v1/collections",
    "Items": f"{GEOSERVER}/ogc/features/v1/collections/curso:referencia/items",
    "MVT": f"{GEOSERVER}/ows?service=WMS&version=1.1.1&request=GetMap&layers=curso:referencia&bbox=-20037508,-20037508,20037508,20037508&width=256&height=256&srs=EPSG:3857&format=application/vnd.mapbox-vector-tile",
}


def main() -> int:
    for name, url in ENDPOINTS.items():
        response = requests.get(url, timeout=30)
        if response.status_code != 200 or not response.content:
            print(f"{name} fallo: {response.status_code} {response.text[:300]}", file=sys.stderr)
            return 1
        if name == "MVT" and response.headers.get("Content-Type") != "application/vnd.mapbox-vector-tile":
            print(f"MVT devolvio Content-Type inesperado: {response.headers.get('Content-Type')}", file=sys.stderr)
            return 1

    for asset in ("referencia.pmtiles", "referencia.cog.tif"):
        response = requests.get(
            f"{STATIC}/{asset}",
            headers={"Origin": "http://localhost:4173", "Range": "bytes=0-15"},
            timeout=30,
        )
        if response.status_code != 206 or response.headers.get("Access-Control-Allow-Origin") != "http://localhost:4173":
            print(f"{asset} no ofrece Range/CORS: {response.status_code} {dict(response.headers)}", file=sys.stderr)
            return 1
    print("Validated PostGIS-backed OGC services, MVT, HTTP Range, and CORS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
