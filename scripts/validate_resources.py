"""Validate Hito 0 governance inventories without mutating the repository."""

from __future__ import annotations

import fnmatch
import hashlib
import json
import subprocess
import sys
from pathlib import Path
import argparse

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> object:
    with path.open(encoding="utf-8") as source:
        return yaml.safe_load(source)


def validate_schema(instance_path: Path, schema_path: Path) -> list[str]:
    instance = load_yaml(instance_path)
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    return [f"{instance_path}: {error.message}" for error in validator.iter_errors(instance)]


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [path for path in result.stdout.decode("utf-8").split("\0") if path]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, default=ROOT / "data/manifests/datasets.yml")
    parser.add_argument("--inventory", type=Path, default=ROOT / "docs/governance/resource-inventory.yml")
    args = parser.parse_args()
    dataset_path = args.dataset
    dataset_schema = ROOT / "data/schemas/dataset-manifest.schema.json"
    inventory_path = args.inventory
    inventory_schema = ROOT / "docs/governance/resource-inventory.schema.json"
    errors = validate_schema(dataset_path, dataset_schema)
    errors.extend(validate_schema(inventory_path, inventory_schema))

    inventory = load_yaml(inventory_path)
    resources = inventory["resources"]
    patterns = [entry["path_glob"] for entry in resources]
    uncovered = [
        path
        for path in tracked_files()
        if not any(fnmatch.fnmatchcase(path, pattern) for pattern in patterns)
    ]
    errors.extend(f"Uninventoried tracked file: {path}" for path in uncovered)

    dataset_ids = [dataset["id"] for dataset in load_yaml(dataset_path)["datasets"]]
    if len(dataset_ids) != len(set(dataset_ids)):
        errors.append("Dataset IDs must be unique")
    for dataset in load_yaml(dataset_path)["datasets"]:
        files = dataset["files"]
        if len(files) != 1:
            errors.append(f"Dataset {dataset['id']} must describe exactly one checksummed file")
            continue
        fixture_path = ROOT / files[0]
        if not fixture_path.is_file():
            errors.append(f"Dataset {dataset['id']} references a missing file: {files[0]}")
            continue
        checksum = "sha256:" + hashlib.sha256(fixture_path.read_bytes()).hexdigest()
        if checksum != dataset["checksum"]:
            errors.append(f"Dataset {dataset['id']} checksum does not match {files[0]}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(resources)} inventory entries and {len(tracked_files())} tracked files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
