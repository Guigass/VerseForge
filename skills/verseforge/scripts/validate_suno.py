#!/usr/bin/env python3
"""Validate VerseForge lyrics, Suno style and exclude fields.

Errors block delivery (hard Suno limits, empty fields). Warnings point to
formatting that tends to degrade Suno generations and must be fixed or justified.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LYRICS_LIMIT = 5000
STYLE_LIMIT = 1000
TITLE_LIMIT = 80
LYRICS_SWEET = 3500
STYLE_SAFE = 900
STYLE_MIN = 120
EXCLUDE_MAX_ITEMS = 10
WORDS_MAX = 450
LINE_WORDS_MAX = 14
TAG_WORDS_MAX = 8
PAREN_WORDS_MAX = 6
SECTION_LINES_MAX = 12

KNOWN_SECTIONS = {
    "intro", "verse", "pre-chorus", "prechorus", "chorus", "post-chorus", "hook",
    "bridge", "breakdown", "build", "build-up", "buildup", "drop", "interlude",
    "instrumental", "instrumental break", "instrumental intro", "break", "outro", "end",
    "refrain", "solo", "guitar solo", "sax solo", "saxophone solo", "piano solo",
    "drum solo", "bass solo", "synth solo", "drum break", "percussion break",
    "rap", "spoken word", "male vocal", "female vocal", "duet", "choir", "harmony",
    "ad-lib", "ad-libs", "whisper", "humming", "backing vocals", "fade out", "fade in",
    "call and response", "group chant",
}
PORTUGUESE_TAGS = {
    "verso": "Verse", "refrao": "Chorus", "refrão": "Chorus", "pre-refrao": "Pre-Chorus",
    "pré-refrão": "Pre-Chorus", "pre-refrão": "Pre-Chorus", "ponte": "Bridge",
    "final": "Outro", "fim": "End", "introducao": "Intro", "introdução": "Intro",
    "voz masculina": "Male Vocal", "voz feminina": "Female Vocal", "ambos": "Duet",
    "coro": "Choir", "rascunho": "",
}
PORTUGUESE_TAG_WORDS = re.compile(
    r"\b(verso|refr[aã]o|pr[eé]-refr[aã]o|ponte|voz|vozes|coro|ambos|introdu[cç][aã]o|"
    r"guitarra|violao|violão|bateria|baixo|longo|suave|falado|sussurrado|de|e|com)\b",
    re.IGNORECASE,
)
PT_TO_BASE = {"verso": "verse", "refrao": "chorus", "refrão": "chorus", "ponte": "bridge",
              "pre-refrao": "pre-chorus", "pré-refrão": "pre-chorus", "pre-refrão": "pre-chorus",
              "final": "outro", "fim": "end"}
REPEAT_MARKER = re.compile(r"(\(\s*x\s*\d+\s*\)|\(\s*\d+\s*x\s*\)|\b[x×]\s?\d\b|\b\d\s?[x×]\b|\bbis\b|\brepete\b)", re.IGNORECASE)
INSTRUCTION_WORDS = re.compile(
    r"\b(sussurr\w*|falad\w*|cantad\w*|suave\w*|solo|instrumental|repete|repetir|"
    r"whisper\w*|spoken|softly|belted|fade|build\w*|harmoni\w*|voz|vocal|coro)\b",
    re.IGNORECASE,
)
NEGATIVE_STYLE = re.compile(
    r"(\bno\s+\w|\bwithout\b|\bavoid\w*\b|\bnever\b|\bnot\b|\bevitar\b|\bsem\s+\w|\bnada\s+de\b|\bnao\s+\w|\bnão\s+\w)",
    re.IGNORECASE,
)
PT_STYLE_HINTS = re.compile(r"\b(com|voz|bateria|baixo|violao|violão|refrao|refrão|clima|verso)\b", re.IGNORECASE)


def read_text(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()


def tag_base(tag: str) -> str:
    """Return the section name of a tag like 'Verse 1: Male Vocal' -> 'verse'."""
    head = re.split(r"[:|\-–—]\s", tag, maxsplit=1)[0]
    head = re.sub(r"\s*\d+$", "", head.strip()).lower()
    return head


class Grouped:
    """Collect per-line warnings and collapse repeated kinds into one message."""

    def __init__(self) -> None:
        self.lines: dict[str, list[int]] = {}
        self.order: list[str] = []
        self.plain: list[str] = []

    def at(self, lineno: int, message: str) -> None:
        if message not in self.lines:
            self.lines[message] = []
            self.order.append(message)
        self.lines[message].append(lineno)

    def append(self, message: str) -> None:
        self.plain.append(message)

    def render(self) -> list[str]:
        rendered = []
        for message in self.order:
            numbers = self.lines[message]
            label = "linha" if len(numbers) == 1 else "linhas"
            shown = ", ".join(str(n) for n in numbers[:8]) + (", ..." if len(numbers) > 8 else "")
            rendered.append(f"{label} {shown}: {message}")
        return rendered + self.plain


def lint_lyrics(lyrics: str) -> list[str]:
    grouped = Grouped()
    lines = lyrics.splitlines()
    tags: list[tuple[int, str]] = []
    sung_words = 0
    section_lines = 0
    section_name = ""
    previous_was_tag = False
    previous_blank = True

    def close_section(lineno: int) -> None:
        if section_lines > SECTION_LINES_MAX:
            grouped.append(
                f"secao '{section_name}' antes da linha {lineno} tem {section_lines} linhas; dividir ou cortar"
            )

    for index, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line:
            previous_blank = True
            previous_was_tag = False
            continue
        if line.count("[") != line.count("]") or line.count("(") != line.count(")"):
            grouped.at(index, "colchetes ou parenteses desbalanceados")
        if REPEAT_MARKER.search(line):
            grouped.at(index, "marcador de repeticao; escrever a repeticao por extenso")

        tag_match = re.fullmatch(r"\[([^\]]+)\]", line)
        if tag_match:
            tag = tag_match.group(1).strip()
            base = tag_base(tag)
            if base in PORTUGUESE_TAGS or PORTUGUESE_TAG_WORDS.search(tag):
                suggestion = PORTUGUESE_TAGS.get(base, "")
                number = re.match(r"\D+\s(\d+)", tag)
                if suggestion and number:
                    suggestion = f"{suggestion} {number.group(1)}"
                hint = f" -> [{suggestion}]" if suggestion else ""
                grouped.at(index, f"tag em portugues [{tag}]{hint}; usar tags em ingles")
            elif base not in KNOWN_SECTIONS and not base.endswith("solo"):
                grouped.at(index, f"tag fora do vocabulario conhecido [{tag}]; confirmar se e intencional")
            if len(tag.split()) > TAG_WORDS_MAX:
                grouped.at(index, f"tag longa demais; manter ate {TAG_WORDS_MAX} palavras")
            if previous_was_tag:
                grouped.at(index, f"tags empilhadas; combinar em uma unica tag, ex. [Verse 1: Male Vocal]")
            if not previous_blank and not previous_was_tag and tags:
                grouped.at(index, f"falta linha em branco antes da secao [{tag}]")
            if section_name:
                close_section(index)
            tags.append((index, tag))
            section_name = tag
            section_lines = 0
            previous_was_tag = True
            previous_blank = False
            continue

        previous_was_tag = False
        previous_blank = False
        section_lines += 1
        inline = re.sub(r"^\[[^\]]+\]\s*", "", line)
        for paren in re.findall(r"\(([^)]*)\)", inline):
            words = paren.split()
            if len(words) > PAREN_WORDS_MAX:
                grouped.at(index, f"parenteses longos serao cantados como backing vocal")
            elif INSTRUCTION_WORDS.search(paren) and len(words) <= 3:
                grouped.at(index, f"'({paren})' parece instrucao; instrucoes vao em colchetes")
        sung = re.sub(r"\[[^\]]*\]", " ", inline)
        words = re.findall(r"[\wÀ-ÿ'-]+", sung)
        sung_words += len(words)
        if len(words) > LINE_WORDS_MAX:
            grouped.at(index, f"{len(words)} palavras; linhas longas fazem o Suno atropelar")
        if re.search(r"\d", sung):
            grouped.at(index, f"numero em digitos; escrever por extenso")

    if section_name:
        close_section(len(lines) + 1)
    warnings = grouped.render()
    if not tags:
        warnings.append("letra sem tags de secao; usar [Verse 1], [Chorus], [Bridge], [Outro]")
    else:
        bases = [PT_TO_BASE.get(tag_base(tag), tag_base(tag)) for _, tag in tags]
        if not any(b in {"chorus", "hook", "refrain"} for b in bases):
            warnings.append("letra sem [Chorus] ou [Hook]; o Suno perde o gancho")
        if bases[-1] not in {"outro", "end", "fade out"}:
            warnings.append("letra sem final explicito; terminar com [Outro] e [End]")
    if sung_words > WORDS_MAX:
        warnings.append(f"{sung_words} palavras cantadas; acima de {WORDS_MAX} o Suno tende a cortar ou atropelar")
    return warnings


def lint_style(style: str) -> list[str]:
    warnings: list[str] = []
    if NEGATIVE_STYLE.search(style):
        warnings.append("estilo contem negativos (no/without/avoid/evitar/sem); mover para suno-exclude.txt")
    if len(PT_STYLE_HINTS.findall(style)) >= 3:
        warnings.append("estilo parece estar em portugues; descritores em ingles sao mais obedecidos")
    if style and len(style) < STYLE_MIN:
        warnings.append(f"estilo curto ({len(style)}); detalhar groove, instrumentos, voz e producao")
    if style and not re.search(r"\bvocals?\b|\binstrumental\b|\brap\b|\bsinger\b|\bchoir\b", style, re.IGNORECASE):
        warnings.append("estilo nao descreve a voz; incluir genero, timbre, entrega e idioma")
    return warnings


def lint_exclude(exclude: str, style: str) -> list[str]:
    warnings: list[str] = []
    items = [item.strip().lower() for item in exclude.split(",") if item.strip()]
    if len(items) > EXCLUDE_MAX_ITEMS:
        warnings.append(f"excluir com {len(items)} itens; mirar os 3-8 desvios mais provaveis")
    style_lower = style.lower()
    for item in items:
        if len(item) > 3 and re.search(rf"\b{re.escape(item)}\b", style_lower):
            if not re.search(rf"\b(no|without|avoid)\s+{re.escape(item)}\b", style_lower):
                warnings.append(f"'{item}' aparece no estilo e no excluir; o pedido fica contraditorio")
    return warnings


def validate(lyrics: str, style: str, exclude: str = "", title: str = "") -> dict[str, object]:
    lyrics_count = len(lyrics)
    style_count = len(style)
    errors: list[str] = []
    warnings: list[str] = []
    if lyrics_count > LYRICS_LIMIT:
        errors.append(f"letra excede {LYRICS_LIMIT} por {lyrics_count - LYRICS_LIMIT} caracteres")
    elif lyrics_count > LYRICS_SWEET:
        warnings.append(f"letra com {lyrics_count} caracteres; acima de {LYRICS_SWEET} o Suno tende a cortar ou atropelar")
    if style_count > STYLE_LIMIT:
        errors.append(f"estilo excede {STYLE_LIMIT} por {style_count - STYLE_LIMIT} caracteres")
    elif style_count > STYLE_SAFE:
        warnings.append("estilo dentro do limite absoluto, mas acima da margem segura")
    if title and len(title) > TITLE_LIMIT:
        errors.append(f"titulo excede {TITLE_LIMIT} caracteres")
    if not lyrics:
        errors.append("letra vazia")
    if not style:
        errors.append("estilo vazio")
    if lyrics:
        warnings.extend(lint_lyrics(lyrics))
    if style:
        warnings.extend(lint_style(style))
    if exclude:
        warnings.extend(lint_exclude(exclude, style))
    return {
        "ok": not errors,
        "lyrics_characters": lyrics_count,
        "style_characters": style_count,
        "exclude_characters": len(exclude),
        "errors": errors,
        "warnings": warnings,
    }


def project_title(project: Path) -> str:
    metadata = project / "project.yaml"
    if not metadata.exists():
        return ""
    match = re.search(r'(?m)^title:\s*"?(.*?)"?\s*$', metadata.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, help="pasta com lyrics.md, suno-style.txt e suno-exclude.txt")
    parser.add_argument("--lyrics", type=Path)
    parser.add_argument("--style", type=Path)
    parser.add_argument("--exclude", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true", help="tratar avisos como falha")
    args = parser.parse_args()
    title = ""
    if args.project:
        args.lyrics = args.lyrics or args.project / "lyrics.md"
        args.style = args.style or args.project / "suno-style.txt"
        args.exclude = args.exclude or args.project / "suno-exclude.txt"
        title = project_title(args.project)
    if not args.lyrics or not args.style:
        parser.error("informar --project ou --lyrics e --style")
    result = validate(read_text(args.lyrics), read_text(args.style), read_text(args.exclude), title)
    failed = not result["ok"] or (args.strict and result["warnings"])
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        status = "OK" if not failed else "ERRO"
        print(
            f"{status}: letra={result['lyrics_characters']}/{LYRICS_LIMIT}, "
            f"estilo={result['style_characters']}/{STYLE_LIMIT}, excluir={result['exclude_characters']}"
        )
        for warning in result["warnings"]:
            print(f"AVISO: {warning}")
        for error in result["errors"]:
            print(f"ERRO: {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
