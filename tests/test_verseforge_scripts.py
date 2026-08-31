from __future__ import annotations

import importlib.util
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


class SkillRoutingTests(unittest.TestCase):
    def test_guided_concept_skill_is_registered_and_routed(self):
        guided = ROOT / "skills" / "develop-music-concept" / "SKILL.md"
        orchestrator = ROOT / "skills" / "verseforge" / "SKILL.md"
        album = ROOT / "skills" / "build-album" / "SKILL.md"

        self.assertTrue(guided.exists())
        self.assertIn("$develop-music-concept", orchestrator.read_text(encoding="utf-8"))
        self.assertIn("$develop-music-concept", album.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
