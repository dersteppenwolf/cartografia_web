"""Verify HTTP Range and CORS for a cloud-native course asset."""

from __future__ import annotations

import argparse
import sys

import requests


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default="http://localhost:18081/assets")
    parser.add_argument("--asset", required=True)
    parser.add_argument("--origin", default="http://localhost:4173")
    args = parser.parse_args()
    response = requests.get(f"{args.base_url.rstrip('/')}/{args.asset}", headers={"Origin": args.origin, "Range": "bytes=0-15"}, timeout=30)
    if response.status_code != 206 or response.headers.get("Access-Control-Allow-Origin") != args.origin or response.headers.get("Accept-Ranges") != "bytes" or not response.headers.get("Content-Range", "").startswith("bytes 0-15/"):
        print(f"Unexpected Range response: {response.status_code} {dict(response.headers)}", file=sys.stderr)
        return 1
    print(f"Validated HTTP Range and CORS for {args.asset}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
