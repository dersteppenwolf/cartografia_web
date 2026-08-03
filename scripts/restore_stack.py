"""Restore a verified PostGIS backup and rebuild the GeoServer configuration."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def compose_command(compose_file: Path, *args: str) -> list[str]:
    return ["docker", "compose", "-f", str(compose_file), *args]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compose-file", type=Path, default=ROOT / "infra/compose.yaml")
    parser.add_argument("--manifest", type=Path, default=ROOT / ".backups/manifest.json")
    parser.add_argument("--secret-file", type=Path, default=ROOT / "infra/secrets/geoserver_password.example")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    dump_path = args.manifest.parent / manifest["dump"]
    dump = dump_path.read_bytes()
    if hashlib.sha256(dump).hexdigest() != manifest["sha256"]:
        raise RuntimeError(f"El checksum de {dump_path} no coincide con el manifiesto.")
    subprocess.run(
        compose_command(args.compose_file, "exec", "-T", "postgis", "pg_restore", "-U", "curso_admin", "-d", "curso", "--clean", "--if-exists", "--no-owner"),
        input=dump,
        check=True,
    )
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/configure_geoserver.py"), "--secret-file", str(args.secret_file)],
        check=True,
    )
    subprocess.run([sys.executable, str(ROOT / "infra/smoke/smoke_stack.py")], check=True)
    print(f"Restored and verified {dump_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
