"""Run pinned Gitleaks and Trivy images without writing reports into the repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GITLEAKS = "zricethezav/gitleaks@sha256:b5918eb91b8d2473cec722f066abb4352e4ffdc4ec9f4283ec143aba9ec9ebc4"
TRIVY = "aquasec/trivy@sha256:029e990b328d149bf0a9ffe355919041e1f86192db2df47e217f8a36dd42ceac"


def run(command: list[str]) -> int:
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scope", choices=("worktree", "history", "dependencies"), required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.scope == "worktree":
        with tempfile.TemporaryDirectory() as empty_dir:
            command = [
                "docker", "run", "--rm", "-v", f"{ROOT}:/repo:ro",
                "-v", f"{empty_dir}:/repo/.git:ro", "-v", f"{empty_dir}:/repo/.venv:ro",
                GITLEAKS, "detect", "--source", "/repo", "--no-git", "--max-target-megabytes", "1",
                "--redact=100", "--no-banner",
            ]
            if args.report is not None:
                command[5:5] = ["-v", f"{args.report.parent}:/reports"]
                command.extend(["--report-format", "json", "--report-path", f"/reports/{args.report.name}"])
            return run(command)
    if args.scope == "history":
        if args.report is None:
            parser.error("--report is required for history")
        return run([
            "docker", "run", "--rm", "-v", f"{ROOT}:/repo:ro",
            "-v", f"{args.report.parent}:/reports", GITLEAKS,
            "git", "/repo", "--log-opts=--all", "--max-target-megabytes", "5",
            "--redact=100", "--report-format", "json", "--report-path", f"/reports/{args.report.name}",
            "--no-banner",
        ])
    return run([
        "docker", "run", "--rm", "-v", f"{ROOT}:/workspace:ro", TRIVY,
        "fs", "--exit-code", "1", "--severity", "CRITICAL,HIGH", "--scanners", "vuln,secret,misconfig",
        "--skip-dirs", ".git,.venv", "/workspace",
    ])


if __name__ == "__main__":
    raise SystemExit(main())
