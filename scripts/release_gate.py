"""Prepare a factual candidate report without inventing pilot evidence."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NPM = "npm.cmd" if sys.platform.startswith("win") else "npm"


def run(*command: str) -> bool:
    return subprocess.run(command, cwd=ROOT, check=False).returncode == 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("prepared", "ready"), required=True)
    args = parser.parse_args()
    report = {"started_at": datetime.now(UTC).isoformat(), "mode": args.mode, "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(), "checks": {}}
    if args.mode == "ready":
        report["checks"]["clean_worktree"] = not subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True).strip()
    report["checks"]["validation"] = run(NPM, "run", "validate")
    report["checks"]["manual_accessibility"] = "- [ ]" not in (ROOT / "docs/governance/manual-accessibility-review.md").read_text(encoding="utf-8")
    report["checks"]["safari_real"] = "result: pending" not in (ROOT / "docs/pilot/browser-matrix.yml").read_text(encoding="utf-8")
    report["checks"]["pilot_completed"] = "Estado: no iniciado" not in (ROOT / "docs/pilot/results.md").read_text(encoding="utf-8")
    report["status"] = "candidate-ready" if all(report["checks"].values()) else "blocked"
    output = ROOT / ".reports/release-gate.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(report["status"])
    return 0 if report["status"] != "blocked" else 1


if __name__ == "__main__":
    raise SystemExit(main())
