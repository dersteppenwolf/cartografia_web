"""Verify HTTP Range and CORS behavior for a local prototype asset."""

from __future__ import annotations

import sys

import requests


URL = "http://localhost:18081/assets/referencia.cog.tif"
HEADERS = {"Origin": "http://localhost:4173", "Range": "bytes=0-15"}


def main() -> int:
    response = requests.get(URL, headers=HEADERS, timeout=30)
    required = {
        "Access-Control-Allow-Origin": "http://localhost:4173",
        "Accept-Ranges": "bytes",
    }
    if response.status_code != 206 or any(response.headers.get(key) != value for key, value in required.items()):
        print(f"Unexpected Range response: {response.status_code} {dict(response.headers)}", file=sys.stderr)
        return 1
    if not response.headers.get("Content-Range", "").startswith("bytes 0-15/"):
        print("Missing expected Content-Range header", file=sys.stderr)
        return 1
    print("Validated HTTP 206, Range, and CORS for the raster prototype.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
