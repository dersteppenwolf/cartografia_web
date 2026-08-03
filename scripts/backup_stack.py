"""Create a verified, portable PostGIS backup for the local course stack."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def compose_command(compose_file: Path, *args: str) -> list[str]:
    return ["docker", "compose", "-f", str(compose_file), *args]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compose-file", type=Path, default=ROOT / "infra/compose.yaml")
    parser.add_argument("--backup-dir", type=Path, default=ROOT / ".backups")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.backup_dir.mkdir(parents=True, exist_ok=True)
    dump_path = args.backup_dir / "curso.dump"
    dump = subprocess.run(
        compose_command(args.compose_file, "exec", "-T", "postgis", "pg_dump", "-U", "curso_admin", "-d", "curso", "-Fc"),
        check=True,
        stdout=subprocess.PIPE,
    )
    dump_path.write_bytes(dump.stdout)
    version = subprocess.run(
        compose_command(args.compose_file, "exec", "-T", "postgis", "psql", "-U", "curso_admin", "-d", "curso", "-Atc", "SHOW server_version"),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    manifest = {
        "created_at": datetime.now(UTC).isoformat(),
        "database": "curso",
        "dump": dump_path.name,
        "sha256": hashlib.sha256(dump.stdout).hexdigest(),
        "postgres_version": version,
    }
    (args.backup_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Backup verified at {dump_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
