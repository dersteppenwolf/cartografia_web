"""Prove a clean-stack restore preserves a known sentinel row."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SENTINEL_ID = "restore-sentinel-00000000-0000-0000-0000-000000000001"


def compose_command(compose_file: Path, *args: str) -> list[str]:
    return ["docker", "compose", "-f", str(compose_file), *args]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compose-file", type=Path, default=ROOT / "infra/compose.yaml")
    parser.add_argument("--backup-dir", type=Path, default=ROOT / ".backups")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    insert = (
        "INSERT INTO referencia (id, nombre, valor, geom) VALUES "
        f"('{SENTINEL_ID}', 'Fila centinela', 99, ST_SetSRID(ST_MakePoint(-74.02, 4.74), 4326)) "
        "ON CONFLICT (id) DO UPDATE SET nombre = EXCLUDED.nombre, valor = EXCLUDED.valor, geom = EXCLUDED.geom;"
    )
    subprocess.run(compose_command(args.compose_file, "exec", "-T", "postgis", "psql", "-U", "curso_admin", "-d", "curso", "-v", "ON_ERROR_STOP=1", "-c", insert), check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/backup_stack.py"), "--compose-file", str(args.compose_file), "--backup-dir", str(args.backup_dir)], check=True)
    subprocess.run(compose_command(args.compose_file, "down", "--volumes"), check=True)
    subprocess.run(compose_command(args.compose_file, "up", "-d", "--build", "--wait"), check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/restore_stack.py"), "--compose-file", str(args.compose_file), "--manifest", str(args.backup_dir / "manifest.json")], check=True)
    check = subprocess.run(
        compose_command(args.compose_file, "exec", "-T", "postgis", "psql", "-U", "curso_admin", "-d", "curso", "-Atc", f"SELECT id FROM referencia WHERE id = '{SENTINEL_ID}'"),
        check=True,
        capture_output=True,
        text=True,
    )
    if check.stdout.strip() != SENTINEL_ID:
        raise RuntimeError("La fila centinela no se recuperó después de la restauración.")
    subprocess.run(
        compose_command(
            args.compose_file,
            "exec",
            "-T",
            "postgis",
            "psql",
            "-U",
            "curso_admin",
            "-d",
            "curso",
            "-v",
            "ON_ERROR_STOP=1",
            "-c",
            f"DELETE FROM referencia WHERE id = '{SENTINEL_ID}';",
        ),
        check=True,
    )
    print("Clean-stack backup and restore preserved the sentinel row and restored the fixture baseline.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
