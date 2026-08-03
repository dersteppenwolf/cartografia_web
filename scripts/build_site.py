"""Build the Jekyll documentation with the pinned Ruby container."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUBY_IMAGE = "ruby@sha256:347edd0c70ee08d87de9f01b99de2f14a64cedb5d1bfb38457dfe8cd0bf113c5"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        shutil.rmtree(output)
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
    return subprocess.run(assemble, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
