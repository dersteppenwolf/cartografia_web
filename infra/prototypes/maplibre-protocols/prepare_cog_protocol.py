"""Copy the published UMD COG protocol bundle into Vite public assets."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "node_modules" / "@geomatico" / "maplibre-cog-protocol" / "dist" / "index.js"
TARGET = ROOT / "infra" / "prototypes" / "maplibre-protocols" / "public" / "cog-protocol.js"


def main() -> int:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
