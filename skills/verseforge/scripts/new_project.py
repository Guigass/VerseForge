#!/usr/bin/env python3
"""Create a VerseForge single, album, or album track without overwriting work."""

from __future__ import annotations

import argparse
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii").lower()
    return re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-") or "sem-titulo"


def write_new(path: Path, content: str) -> None:
    if path.exists():
        raise FileExistsError(f"arquivo ja existe: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def yaml_value(value: str) -> str:
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def song_files(folder: Path, title: str, kind: str, album: str = "", track: int = 0) -> None:
    created = datetime.now(timezone.utc).isoformat()
    metadata = [
        f"title: {yaml_value(title)}",
        f"slug: {yaml_value(folder.name)}",
        f"kind: {yaml_value(kind)}",
        f"status: {yaml_value('draft')}",
        f"voice: {yaml_value('to-define')}",
        f"created_at: {yaml_value(created)}",
        f"current_version: {yaml_value('working')}",
    ]
    if album:
        metadata.extend([f"album: {yaml_value(album)}", f"track_number: {track}"])
    write_new(folder / "project.yaml", "\n".join(metadata) + "\n")
    write_new(folder / "brief.md", f"# {title}\n\n## Intencao\n\nA definir.\n")
    write_new(folder / "lyrics.md", "[Rascunho]\n")
    write_new(folder / "suno-style.txt", "A definir.\n")
    (folder / "sources").mkdir(parents=True, exist_ok=True)
    (folder / "versions").mkdir(parents=True, exist_ok=True)


def create_single(root: Path, title: str) -> Path:
    folder = root / "singles" / slugify(title)
    if folder.exists():
        raise FileExistsError(f"projeto ja existe: {folder}")
    song_files(folder, title, "single")
    return folder


def create_album(root: Path, title: str) -> Path:
    folder = root / "albums" / slugify(title)
    if folder.exists():
        raise FileExistsError(f"album ja existe: {folder}")
    created = datetime.now(timezone.utc).isoformat()
    write_new(folder / "album.yaml", "\n".join([
        f"title: {yaml_value(title)}",
        f"slug: {yaml_value(slugify(title))}",
        f"status: {yaml_value('concept')}",
        f"created_at: {yaml_value(created)}",
        f"default_voice: {yaml_value('to-define')}",
    ]) + "\n")
    write_new(folder / "creative-direction.md", f"# Direcao criativa — {title}\n\n## Ideia inicial\n\nA definir.\n\n## Decisoes confirmadas\n\nA definir.\n\n## Perguntas abertas\n\nA definir.\n\n## Proximo passo\n\nA definir.\n")
    write_new(folder / "identity.md", f"# Identidade — {title}\n\nA definir com a skill `$build-album`.\n")
    write_new(folder / "source-map.md", f"# Mapa de fontes — {title}\n\n| Faixa | Musica-fonte | Funcao | Fidelidade | Transformacao | Voz | Letra recebida? |\n|---:|---|---|---:|---:|---|---|\n")
    write_new(folder / "tracklist.md", f"# Faixas — {title}\n\n| # | Titulo | Funcao no arco | Status |\n|---:|---|---|---|\n")
    (folder / "songs").mkdir(parents=True, exist_ok=True)
    return folder


def create_track(root: Path, album_slug: str, title: str, track: int) -> Path:
    album = root / "albums" / album_slug
    if not (album / "album.yaml").exists():
        raise FileNotFoundError(f"album nao encontrado: {album}")
    folder = album / "songs" / f"{track:02d}-{slugify(title)}"
    if folder.exists():
        raise FileExistsError(f"faixa ja existe: {folder}")
    song_files(folder, title, "album-track", album_slug, track)
    return folder


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=["single", "album", "track"])
    parser.add_argument("--title", required=True)
    parser.add_argument("--root", type=Path, default=Path("projects"))
    parser.add_argument("--album", help="slug do album para kind=track")
    parser.add_argument("--track-number", type=int)
    args = parser.parse_args()
    if args.kind == "single":
        folder = create_single(args.root, args.title)
    elif args.kind == "album":
        folder = create_album(args.root, args.title)
    else:
        if not args.album or not args.track_number or args.track_number < 1:
            parser.error("track exige --album e --track-number maior que zero")
        folder = create_track(args.root, args.album, args.title, args.track_number)
    print(folder.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
