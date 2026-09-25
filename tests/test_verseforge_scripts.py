from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "verseforge" / "scripts"


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


new_project = load_module("new_project")
validate_suno = load_module("validate_suno")


class ProjectCreationTests(unittest.TestCase):
    def test_single_album_and_track_layout(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            single = new_project.create_single(root, "Noite em Casa")
            album = new_project.create_album(root, "Cidade em Frequencias")
            track = new_project.create_track(root, album.name, "Luzes da Janela", 1)

            self.assertEqual(single.name, "noite-em-casa")
            self.assertTrue((single / "project.yaml").exists())
            self.assertTrue((single / "versions").is_dir())
            self.assertTrue((album / "identity.md").exists())
            self.assertTrue((album / "creative-direction.md").exists())
            self.assertTrue((album / "source-map.md").exists())
            self.assertEqual(track.name, "01-luzes-da-janela")
            self.assertTrue((track / "suno-style.txt").exists())
            self.assertTrue((track / "suno-exclude.txt").exists())
            self.assertIn('model: "v6"', (single / "project.yaml").read_text(encoding="utf-8"))

    def test_existing_project_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            new_project.create_single(root, "Mesmo Nome")
            with self.assertRaises(FileExistsError):
                new_project.create_single(root, "Mesmo Nome")


class SunoValidationTests(unittest.TestCase):
    def test_absolute_limits_are_accepted(self):
        result = validate_suno.validate("x" * 5000, "y" * 1000)
        self.assertTrue(result["ok"])

    def test_limits_are_blocking(self):
        result = validate_suno.validate("x" * 5001, "y" * 1001)
        self.assertFalse(result["ok"])
        self.assertEqual(len(result["errors"]), 2)


GOOD_LYRICS = """[Intro: soft nylon guitar]

[Verse 1: Male Vocal]
Acordei com o sol na janela
O cafe esfriando na mesa
Teu casaco ainda na cadeira
E a casa inteira em silencio

[Chorus: Duet, harmony]
Fica mais um pouco (fica)
Que a manha ainda e nossa
Fica mais um pouco
Que a manha ainda e nossa

[Bridge: stripped, half-time]
[Female Vocal] Onde voce tava?
[Male Vocal] Tava te esperando

[Outro: fade out]
Fica mais um pouco

[End]"""

GOOD_STYLE = (
    "Bossa nova with neo-soul, 78 BPM, gentle swung groove. Syncopated nylon-string guitar, "
    "soft brushed drums, warm upright bass, Rhodes chords. Duet: male baritone, calm; female alto, "
    "airy, harmony on the chorus. Brazilian Portuguese vocals, intimate close-mic. Tender morning mood. "
    "Sparse verses, lifted chorus, stripped bridge. Warm analog mix."
)


class SunoLintTests(unittest.TestCase):
    def test_well_formed_song_has_no_warnings(self):
        result = validate_suno.validate(GOOD_LYRICS, GOOD_STYLE, "samba, autotune, EDM drop")
        self.assertTrue(result["ok"])
        self.assertEqual(result["warnings"], [])

    def test_portuguese_and_stacked_tags_are_flagged(self):
        lyrics = "[Refrão]\n[Voz masculina]\nFica comigo\n\n[Outro]\nTchau"
        warnings = " ".join(validate_suno.validate(lyrics, GOOD_STYLE)["warnings"])
        self.assertIn("[Chorus]", warnings)
        self.assertIn("[Male Vocal]", warnings)
        self.assertIn("empilhadas", warnings)

    def test_numbered_portuguese_tag_keeps_number(self):
        lyrics = "[Verso 2]\nFica comigo\n\n[Chorus]\nFica\n\n[Outro]\nTchau"
        warnings = " ".join(validate_suno.validate(lyrics, GOOD_STYLE)["warnings"])
        self.assertIn("[Verse 2]", warnings)

    def test_lyric_formatting_problems_are_flagged(self):
        lyrics = "[Chorus]\nFica comigo (x2)\nEram 2 da manha\nVem (sussurrado)\n\n[Verse 1]\nNada"
        warnings = " ".join(validate_suno.validate(lyrics, GOOD_STYLE)["warnings"])
        self.assertIn("repeticao", warnings)
        self.assertIn("extenso", warnings)
        self.assertIn("instrucao", warnings)
        self.assertIn("final explicito", warnings)

    def test_style_problems_are_flagged(self):
        style = "Samba com bateria leve e voz masculina, clima de roda, sem trap e evitar EDM."
        warnings = " ".join(validate_suno.validate(GOOD_LYRICS, style)["warnings"])
        self.assertIn("negativos", warnings)
        self.assertIn("portugues", warnings)

    def test_exclude_conflict_is_flagged(self):
        warnings = " ".join(validate_suno.validate(GOOD_LYRICS, GOOD_STYLE, "rhodes, trap")["warnings"])
        self.assertIn("contraditorio", warnings)

    def test_title_limit_is_blocking(self):
        result = validate_suno.validate(GOOD_LYRICS, GOOD_STYLE, title="t" * 81)
        self.assertFalse(result["ok"])

    def test_cli_project_mode_and_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = new_project.create_single(Path(temp), "Fica Mais")
            (folder / "lyrics.md").write_text(GOOD_LYRICS, encoding="utf-8")
            (folder / "suno-style.txt").write_text(GOOD_STYLE, encoding="utf-8")
            (folder / "suno-exclude.txt").write_text("samba, autotune", encoding="utf-8")
            check = subprocess.run(
                [sys.executable, str(SCRIPTS / "validate_suno.py"), "--project", str(folder), "--strict"],
                capture_output=True, text=True, encoding="utf-8",
            )
            self.assertEqual(check.returncode, 0, check.stdout)
            subprocess.run(
                [sys.executable, str(SCRIPTS / "snapshot_version.py"), str(folder), "--note", "teste"],
                check=True, capture_output=True,
            )
            snapshot = (folder / "versions" / "v001.md").read_text(encoding="utf-8")
            self.assertIn("## EXCLUIR", snapshot)
            self.assertIn("style_influence: 70", snapshot)
            self.assertIn('current_version: "v001"', (folder / "project.yaml").read_text(encoding="utf-8"))


class SkillRoutingTests(unittest.TestCase):
    def test_guided_concept_skill_is_registered_and_routed(self):
        guided = ROOT / "skills" / "develop-music-concept" / "SKILL.md"
        orchestrator = ROOT / "skills" / "verseforge" / "SKILL.md"
        album = ROOT / "skills" / "build-album" / "SKILL.md"

        self.assertTrue(guided.exists())
        self.assertIn("$develop-music-concept", orchestrator.read_text(encoding="utf-8"))
        self.assertIn("$develop-music-concept", album.read_text(encoding="utf-8"))

    def test_suno_guide_is_referenced_by_composition_skills(self):
        for name in ["verseforge", "write-original-song", "reinterpret-song", "mashup-songs", "refine-song"]:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("suno-guide.md", text, name)


if __name__ == "__main__":
    unittest.main()
