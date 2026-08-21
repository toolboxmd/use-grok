#!/usr/bin/env python3
"""Contract tests for the toolboxmd-use-grok skill text."""

from __future__ import annotations

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
FRONTMATTER = SKILL.split("---", 2)[1]
REFERENCE = (ROOT / "references/grok-cli.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")

PORTABLE_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}


def fm_line(key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.*)$", FRONTMATTER, re.MULTILINE)
    if not match:
        raise AssertionError(f"missing frontmatter key {key}")
    return match.group(1).strip().strip('"').strip("'")


class UseGrokSkillTests(unittest.TestCase):
    def test_frontmatter_matches_current_skill_specs(self) -> None:
        top_level_keys = {
            match.group(1)
            for match in re.finditer(r"^([a-z][a-z0-9-]*):", FRONTMATTER, re.MULTILINE)
        }
        self.assertTrue(top_level_keys <= PORTABLE_FRONTMATTER_KEYS)
        self.assertNotIn("disable-model-invocation", FRONTMATTER)
        self.assertNotIn("argument-hint", FRONTMATTER)
        name = fm_line("name")
        self.assertEqual(name, ROOT.name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        description = fm_line("description")
        self.assertTrue(description)
        self.assertNotIn("\n", description)
        self.assertLessEqual(len(description), 1024)
        self.assertNotRegex(description, r"<[^>]+>")
        self.assertIn("Do not use unless the user asked to consult Grok", description)
        for phrase in ("ask", "send", "pass", "delegate", "consult"):
            self.assertIn(phrase, description)
        self.assertEqual(fm_line("license"), "Apache-2.0")
        compatibility = fm_line("compatibility")
        self.assertIn("grok", compatibility.lower())
        self.assertIn("local shell", compatibility.lower())
        self.assertLessEqual(len(compatibility), 500)
        self.assertIn("short-description: Consult local Grok Build CLI", FRONTMATTER)

    def test_codex_openai_yaml_allows_implicit_invocation(self) -> None:
        openai = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", openai)
        self.assertIn('display_name: "Use Grok"', openai)
        self.assertIn('short_description: "Consult the local Grok Build CLI"', openai)

    def test_host_invocation_syntax_is_documented(self) -> None:
        self.assertIn("`/toolboxmd-use-grok`", SKILL)
        self.assertIn("`$toolboxmd-use-grok`", SKILL)
        self.assertIn("select the skill with `@` in ChatGPT", SKILL)

    def test_default_invocation_is_full_power_headless(self) -> None:
        for flag in (
            "--prompt-file",
            "--verbatim",
            "--cwd",
            "--always-approve",
            "--output-format json",
        ):
            self.assertIn(flag, SKILL)
        self.assertIn("`--always-approve` is `--yolo`", SKILL)
        self.assertIn("A path in the brief is a hint", SKILL)
        self.assertIn("Unrestricted permissions are intentional", SKILL)

    def test_completion_is_process_exit(self) -> None:
        self.assertIn("## When Grok is done", SKILL)
        self.assertIn("blocking", SKILL)
        self.assertIn("`end_turn`", SKILL)
        self.assertIn("`max_turn_requests`", SKILL)
        self.assertIn("Do not poll", SKILL)

    def test_does_not_restrict_by_default(self) -> None:
        self.assertIn("Do **not** add `--no-subagents`", SKILL)
        self.assertNotIn("--deny Read", SKILL)
        self.assertNotIn("consult-grok", SKILL)
        self.assertNotIn("--mode explicit", SKILL)
        self.assertNotIn("Automatic review", SKILL)

    def test_tool_and_flag_catalog_is_progressively_disclosed(self) -> None:
        self.assertIn("[references/grok-cli.md](references/grok-cli.md)", SKILL)
        self.assertIn("Grok CLI 1.0.5", REFERENCE)
        for tool in (
            "read_file",
            "search_replace",
            "grep",
            "list_dir",
            "run_terminal_command",
            "web_search",
            "web_fetch",
            "todo_write",
            "spawn_subagent",
            "memory_search",
        ):
            self.assertIn(tool, REFERENCE)
        for flag in (
            "--max-turns",
            "--json-schema",
            "--resume",
            "--sandbox",
            "--disallowed-tools",
            "--reasoning-effort",
        ):
            self.assertIn(flag, REFERENCE)
        for kind in ("general-purpose", "explore", "plan"):
            self.assertIn(kind, REFERENCE)

    def test_repository_text_follows_global_style(self) -> None:
        self.assertNotIn("\N{EM DASH}", SKILL)
        self.assertNotIn("\N{EM DASH}", README)

    def test_goal_recipes_exist(self) -> None:
        for heading in (
            "### Research",
            "### Implement / coding",
            "### Review / second opinion",
            "### Continue a prior consult",
        ):
            self.assertIn(heading, SKILL)
        self.assertIn("Goal: research", SKILL)
        self.assertIn("Goal: implement", SKILL)
        self.assertIn("Goal: review", SKILL)


if __name__ == "__main__":
    unittest.main(verbosity=2)
