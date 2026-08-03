"""Replace only historical Mapbox public-token values without rewriting Git history."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TOKEN_PATTERN = re.compile(r"pk\.[A-Za-z0-9._-]+")
TOKEN_FILES = (
    "01_Fundamentos/ejemplo_leaflet.html",
    "02_Conceptos/html/leaflet_geojson_simple.html",
    "03_Cartografia/example/kepler.gl.html",
    "04_Servicios_Web_Geoservicios_OGC/html/leaflet_wms_2.html",
    "05_Servidores_Mapas/Readme.md",
)
PLACEHOLDER = "MAPBOX_ACCESS_TOKEN_REQUIRED"


def main() -> int:
    changed_files = 0
    replaced_tokens = 0
    for relative_path in TOKEN_FILES:
        path = ROOT / relative_path
        if not path.is_file():
            print(f"Missing known token path: {relative_path}", file=sys.stderr)
            return 1
        original = path.read_text(encoding="utf-8")
        updated, replacements = TOKEN_PATTERN.subn(PLACEHOLDER, original)
        if replacements:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed_files += 1
            replaced_tokens += replacements
    print(f"Sanitized {replaced_tokens} token value(s) in {changed_files} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
