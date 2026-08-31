#!/usr/bin/env python3
"""Snapshot current VerseForge song files into an immutable version file."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project", type=Path)
    parser.add_argument("--note", default="Nova versao")
    args = parser.parse_args()
    lyrics_path = args.project / "lyrics.md"
    style_path = args.project / "suno-style.txt"
    if not lyrics_path.exists() or not style_path.exists():
        parser.error("a pasta precisa conter lyrics.md e suno-style.txt")
    versions = args.project / "versions"
    versions.mkdir(exist_ok=True)
    numbers = []
    for path in versions.glob("v*.md"):
        match = re.fullmatch(r"v(\d+)\.md", path.name)
        if match:
            numbers.append(int(match.group(1)))
    number = max(numbers, default=0) + 1
    target = versions / f"v{number:03d}.md"
    lyrics = lyrics_path.read_text(encoding="utf-8").strip()
    style = style_path.read_text(encoding="utf-8").strip()
    content = (
        f"# Versao {number:03d}\n\n"
        f"- Data UTC: {datetime.now(timezone.utc).isoformat()}\n"
        f"- Nota: {args.note}\n"
        f"- Caracteres da letra: {len(lyrics)}\n"
        f"- Caracteres do estilo: {len(style)}\n\n"
        f"## LETRA\n\n{lyrics}\n\n"
        f"## ESTILO PARA O SUNO\n\n{style}\n"
    )
    target.write_text(content, encoding="utf-8")
    metadata = args.project / "project.yaml"
    if metadata.exists():
        project_text = metadata.read_text(encoding="utf-8")
        version_line = f'current_version: "v{number:03d}"'
        if re.search(r"(?m)^current_version:.*$", project_text):
            project_text = re.sub(r"(?m)^current_version:.*$", version_line, project_text)
        else:
            project_text = project_text.rstrip() + "\n" + version_line + "\n"
        metadata.write_text(project_text, encoding="utf-8")
    print(target.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
