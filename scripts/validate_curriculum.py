"""Check the eight-unit curriculum traceability contract."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    path = ROOT / "docs" / "governance" / "curriculum-traceability.yml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    units = data["units"]
    required = data["required_topics"]
    topics = [unit["topic"] for unit in units]
    errors = []
    if len(units) != 8:
        errors.append("The curriculum must contain exactly eight units.")
    if topics != required:
        errors.append("Unit topics must match the required topics in order.")
    if len(set(topics)) != len(topics):
        errors.append("Unit topics must be unique.")
    for unit in units:
        for key in ("document", "exercise", "validation", "rubric"):
            if not unit.get(key):
                errors.append(f"Unit {unit['id']} is missing {key}.")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated eight curriculum units with exercises, validations, and rubrics.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
