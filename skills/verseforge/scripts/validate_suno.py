#!/usr/bin/env python3
"""Validate VerseForge lyrics and Suno style character limits."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


LYRICS_LIMIT = 5000
STYLE_LIMIT = 1000
LYRICS_SAFE = 4800
STYLE_SAFE = 900


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def validate(lyrics: str, style: str) -> dict[str, object]:
    lyrics_count = len(lyrics)
    style_count = len(style)
    errors: list[str] = []
    warnings: list[str] = []
    if lyrics_count > LYRICS_LIMIT:
        errors.append(f"letra excede {LYRICS_LIMIT} por {lyrics_count - LYRICS_LIMIT} caracteres")
    elif lyrics_count > LYRICS_SAFE:
        warnings.append("letra dentro do limite absoluto, mas acima da margem segura")
    if style_count > STYLE_LIMIT:
        errors.append(f"estilo excede {STYLE_LIMIT} por {style_count - STYLE_LIMIT} caracteres")
    elif style_count > STYLE_SAFE:
        warnings.append("estilo dentro do limite absoluto, mas acima da margem segura")
    if not lyrics:
        errors.append("letra vazia")
    if not style:
        errors.append("estilo vazio")
    return {
        "ok": not errors,
        "lyrics_characters": lyrics_count,
        "style_characters": style_count,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lyrics", required=True, type=Path)
    parser.add_argument("--style", required=True, type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(read_text(args.lyrics), read_text(args.style))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "OK" if result["ok"] else "ERRO"
        print(f"{status}: letra={result['lyrics_characters']}/5000, estilo={result['style_characters']}/1000")
        for warning in result["warnings"]:
            print(f"AVISO: {warning}")
        for error in result["errors"]:
            print(f"ERRO: {error}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
