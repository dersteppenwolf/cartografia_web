"""Ensure Hito 1 validators reject deliberately malformed fixtures."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INVALID = ROOT / "tests" / "fixtures" / "invalid"
NPX = "npx.cmd" if sys.platform.startswith("win") else "npx"


def run(*command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)


def test_markdownlint_rejects_invalid_markdown() -> None:
    assert run(NPX, "--no-install", "markdownlint-cli2", str(INVALID / "invalid.md")).returncode != 0


def test_html_validate_rejects_invalid_html() -> None:
    assert run(NPX, "--no-install", "html-validate", str(INVALID / "invalid.html")).returncode != 0


def test_json_parser_rejects_invalid_json() -> None:
    result = run(sys.executable, "-m", "json.tool", str(INVALID / "invalid.json"))
    assert result.returncode != 0


def test_lxml_rejects_invalid_xml() -> None:
    result = run(sys.executable, "-c", "from lxml import etree; etree.parse(r'tests/fixtures/invalid/invalid.xml')")
    assert result.returncode != 0


def test_inventory_validator_rejects_invalid_inventory() -> None:
    result = run(
        sys.executable,
        "scripts/validate_resources.py",
        "--inventory",
        str(INVALID / "invalid-inventory.yml"),
    )
    assert result.returncode != 0
