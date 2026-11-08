#!/usr/bin/env python3
"""Validate the Coach-DY repository.

Checks:
- required files exist
- JSON parses and has expected top-level keys/counts
- SKILL.md has valid YAML frontmatter with name and description
- relative markdown links to local files resolve
- no audio/video/transcript files are committed

Run from anywhere:
    python scripts/validate.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "README.pl.md",
    "LICENSE",
    "NOTICE.md",
    "repo-about.json",
    "references/knowledge_base_dy.md",
    "references/knowledge_base_dy.json",
    "references/evidence_base.md",
    "agents/openai.yaml",
]

MEDIA_SUFFIXES = {".wav", ".mp3", ".m4a", ".flac", ".mp4", ".mov", ".aac", ".ogg"}

errors: list[str] = []
warnings: list[str] = []


def check_required_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")


def check_json() -> None:
    path = ROOT / "references" / "knowledge_base_dy.json"
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return

    expected = {
        "principles": 20,
        "numbers": 12,
        "evidence_map": 12,
    }
    for key, count in expected.items():
        if key not in data:
            errors.append(f"JSON missing key: {key}")
        elif len(data[key]) != count:
            warnings.append(f"JSON '{key}' has {len(data[key])} entries, expected {count}")

    for key in ("evidence_base", "evidence_summary", "contextual_optimization", "n_of_1_caveat"):
        if key not in data:
            errors.append(f"JSON missing key: {key}")


def check_repo_about() -> None:
    path = ROOT / "repo-about.json"
    if not path.is_file():
        return
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in repo-about.json: {exc}")
        return

    description = data.get("description", "")
    if not isinstance(description, str) or not description.strip():
        errors.append("repo-about.json: description must be a non-empty string")
    elif len(description) > 350:
        errors.append(f"repo-about.json: description is {len(description)} chars (max 350)")

    topics = data.get("topics", [])
    if not isinstance(topics, list) or not all(isinstance(t, str) for t in topics):
        errors.append("repo-about.json: topics must be a list of strings")
        return
    if len(topics) > 20:
        errors.append(f"repo-about.json: {len(topics)} topics (max 20)")
    for topic in topics:
        if not re.match(r"^[a-z0-9][a-z0-9-]*$", topic):
            errors.append(f"repo-about.json: invalid topic {topic!r}")


def check_skill_frontmatter() -> None:
    path = ROOT / "SKILL.md"
    if not path.is_file():
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter (---)")
        return
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append("SKILL.md frontmatter is not closed with ---")
        return
    frontmatter = text[4:end]
    if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
        errors.append("SKILL.md frontmatter missing 'name'")
    if not re.search(r"^description:\s*\S+", frontmatter, re.MULTILINE):
        errors.append("SKILL.md frontmatter missing 'description'")
    if "name: Coach-DY" not in frontmatter:
        warnings.append("SKILL.md name is not 'Coach-DY'")


def check_local_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for target in link_re.findall(md.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            if not (md.parent / clean).exists():
                errors.append(f"broken local link in {md.relative_to(ROOT)}: {target}")


def check_no_media() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in MEDIA_SUFFIXES:
            errors.append(f"media file should not be committed: {path.relative_to(ROOT)}")


def main() -> int:
    check_required_files()
    check_json()
    check_repo_about()
    check_skill_frontmatter()
    check_local_links()
    check_no_media()

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    if errors:
        print("Errors:")
        for error in errors:
            print(f"  - {error}")
        print(f"\nFAILED: {len(errors)} error(s)")
        return 1

    print("OK: required files, JSON, frontmatter, links, and media checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
