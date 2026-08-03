"""Execute required notebooks with an explicit local-data mode."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("fixtures", "local"), required=True)
    args = parser.parse_args()
    if args.mode == "local":
        shutil.copyfile(ROOT / "notebooks/config.local.template.json", ROOT / "notebooks/config.local.json")
    environment = {**os.environ, "COURSE_DATA_MODE": args.mode}
    return subprocess.run([sys.executable, "-m", "pytest", "--nbmake", "notebooks"], cwd=ROOT, env=environment, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
