"""Validate the local OpenAPI fixture needed by the interoperability unit."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    path = ROOT / "data" / "fixtures" / "openapi" / "features.json"
    document = json.loads(path.read_text(encoding="utf-8"))
    required_paths = {"/collections", "/collections/referencia/items"}
    if document.get("openapi") != "3.0.3" or not required_paths.issubset(document.get("paths", {})):
        print("OpenAPI fixture is missing required version or paths.", file=sys.stderr)
        return 1
    print("Validated local OpenAPI fixture.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
