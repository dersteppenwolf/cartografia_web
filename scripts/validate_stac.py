"""Validate every static STAC document and local asset link."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAC = ROOT / "data" / "fixtures" / "stac"
STAC_VALIDATOR = "stac-validator.exe" if sys.platform.startswith("win") else "stac-validator"


def main() -> int:
    documents = [STAC / "catalog.json", STAC / "collection.json", STAC / "item-referencia.json"]
    for document in documents:
        result = subprocess.run([STAC_VALIDATOR, "validate", str(document)], cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
    item = json.loads((STAC / "item-referencia.json").read_text(encoding="utf-8"))
    for asset in item["assets"].values():
        if not (STAC / asset["href"]).resolve().is_file():
            print(f"STAC item asset is missing: {asset['href']}", file=sys.stderr)
            return 1
    print("Validated Catalog, Collection, Item, and local cloud-native assets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
