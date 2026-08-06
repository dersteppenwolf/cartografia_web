"""Build the Jekyll documentation with the pinned Ruby container."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUBY_IMAGE = "ruby@sha256:347edd0c70ee08d87de9f01b99de2f14a64cedb5d1bfb38457dfe8cd0bf113c5"
NPM = "npm.cmd" if sys.platform.startswith("win") else "npm"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
    client = ROOT / "examples" / "maplibre" / "app"
    if client.is_dir():
        result = subprocess.run([NPM, "run", "--workspace", "examples/maplibre/app", "build"], cwd=ROOT, check=False)
        if result.returncode:
            return result.returncode
    output_relative = output.relative_to(ROOT).as_posix()
    command = (
        "gem install bundler -v 2.6.2 --no-document "
        "&& bundle _2.6.2_ config set path /tmp/bundle "
        "&& bundle _2.6.2_ install "
        "&& bundle _2.6.2_ exec jekyll build --source docs "
        f"--destination /workspace/{output_relative} --baseurl '{args.baseurl}'"
    )
    result = subprocess.run(
        ["docker", "run", "--rm", "-v", f"{ROOT}:/workspace", "-w", "/workspace", RUBY_IMAGE, "bash", "-lc", command],
        check=False,
    )
    if result.returncode:
        return result.returncode
    slides_output = output.parent / "_site_slides"
    slides = [
        sys.executable,
        str(ROOT / "scripts" / "build_slides.py"),
        "--baseurl",
        args.baseurl,
        "--output",
        str(slides_output),
    ]
    result = subprocess.run(slides, check=False)
    if result.returncode:
        return result.returncode
    assemble = [
        sys.executable,
        str(ROOT / "scripts" / "assemble_site.py"),
        "--jekyll-site",
        str(output),
        "--output",
        str(output.parent / "_site"),
    ]
    leaflet = ROOT / "examples" / "leaflet"
    if leaflet.is_dir():
        assemble.extend(["--leaflet-dir", str(leaflet)])
    maplibre_dist = client / "dist"
    if maplibre_dist.is_dir():
        assemble.extend(["--maplibre-dist", str(maplibre_dist)])
    cloud_assets = ROOT / "data" / "fixtures" / "cloud"
    if cloud_assets.is_dir():
        assemble.extend(["--cloud-assets", str(cloud_assets)])
    assemble.extend(["--slides-dir", str(slides_output)])
    return subprocess.run(assemble, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
