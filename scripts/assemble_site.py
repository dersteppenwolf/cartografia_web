"""Assemble Jekyll output and approved examples into one static site tree."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def copy_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(source)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jekyll-site", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--leaflet-dir", type=Path)
    parser.add_argument("--maplibre-dist", type=Path)
    parser.add_argument("--cloud-assets", type=Path)
    parser.add_argument("--slides-dir", type=Path)
    args = parser.parse_args()

    output = args.output.resolve()
    if output == args.jekyll_site.resolve():
        raise ValueError("--output must differ from --jekyll-site")
    if output.exists():
        shutil.rmtree(output)
    copy_tree(args.jekyll_site.resolve(), output)

    optional_trees = (
        (args.leaflet_dir, output / "examples" / "leaflet"),
        (args.maplibre_dist, output / "examples" / "maplibre"),
        (args.cloud_assets, output / "assets" / "data"),
        (args.slides_dir, output / "presentaciones" / "unidad-01"),
    )
    for source, destination in optional_trees:
        if source is not None:
            copy_tree(source.resolve(), destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
