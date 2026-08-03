"""Copy the published COG UMD bundle into Vite public assets."""

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parents[2] / "node_modules/@geomatico/maplibre-cog-protocol/dist/index.js"
TARGET = ROOT / "public/cog-protocol.js"


def main() -> int:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE, TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
