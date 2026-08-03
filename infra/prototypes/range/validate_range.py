"""Verify HTTP Range and CORS behavior for a local prototype asset."""

from __future__ import annotations

import sys
import argparse

import requests


HEADERS = {"Origin": "http://localhost:4173", "Range": "bytes=0-15"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--asset", default="referencia.cog.tif")
    args = parser.parse_args()
    url = f"http://localhost:18081/assets/{args.asset}"
    response = requests.get(url, headers=HEADERS, timeout=30)
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
    print(f"Validated HTTP 206, Range, and CORS for {args.asset}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
