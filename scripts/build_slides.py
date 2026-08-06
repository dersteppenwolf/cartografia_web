"""Build the approved Unidad 1 Slidev deck with a deploy-safe base path."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NPM = "npm.cmd" if sys.platform.startswith("win") else "npm"
WORKSPACE = "@cartografia-web/slides-unidad01"
DECK_PATH = "/presentaciones/unidad-01/"
REQUIRED_ASSET = Path("assets/generated/internet_web.svg")
FORBIDDEN_ASSET = Path("assets/slide-001-image-000.jpg")
PROTECTED_DIRECTORIES = (
    ROOT / ".github",
    ROOT / "data",
    ROOT / "docs",
    ROOT / "examples",
    ROOT / "infra",
    ROOT / "plans",
    ROOT / "scripts",
    ROOT / "tests",
)


def normalize_baseurl(value: str) -> str:
    baseurl = value.strip()
    if not baseurl or baseurl == "/":
        return ""
    if not baseurl.startswith("/") or any(marker in baseurl for marker in ("#", "?", "://")):
        raise ValueError("--baseurl must be empty or a path beginning with '/'")
    return "/" + baseurl.strip("/")


def deck_base(baseurl: str) -> str:
    return f"{normalize_baseurl(baseurl)}{DECK_PATH}"


def ensure_safe_output(output: Path) -> Path:
    resolved = output.resolve()
    if resolved == ROOT:
        raise ValueError("--output must not be the repository root")
    if any(source == resolved or source in resolved.parents for source in PROTECTED_DIRECTORIES):
        raise ValueError("--output must not be inside a source directory")
    if resolved.exists() and not resolved.is_dir():
        raise ValueError("--output must be a directory when it already exists")
    return resolved


def verify_build(output: Path) -> None:
    required = output / "index.html"
    asset = output / REQUIRED_ASSET
    forbidden = output / FORBIDDEN_ASSET
    if not required.is_file():
        raise FileNotFoundError(f"Missing Slidev entry point: {required}")
    if not asset.is_file():
        raise FileNotFoundError(f"Missing required Slidev asset: {asset}")
    if forbidden.exists():
        raise RuntimeError(f"Historical capture must not be published: {forbidden}")


def build(baseurl: str, output: Path) -> Path:
    target = ensure_safe_output(output)
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    command = [
        NPM,
        "run",
        "--workspace",
        WORKSPACE,
        "build",
        "--",
        "--out",
        str(target),
        "--base",
        deck_base(baseurl),
        "--router-mode",
        "hash",
    ]
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        raise RuntimeError(f"Slidev build failed with exit code {result.returncode}")
    verify_build(target)
    return target


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        output = build(args.baseurl, args.output)
    except (FileNotFoundError, RuntimeError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1
    print(f"Built slides to {output}")
    print(f"Verified index.html and {REQUIRED_ASSET.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
