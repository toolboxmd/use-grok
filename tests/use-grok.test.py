#!/usr/bin/env python3
"""Contract tests for the use-grok plugin and skill text."""

from __future__ import annotations

from pathlib import Path
import json
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "use-grok"
SKILL = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
FRONTMATTER = SKILL.split("---", 2)[1]
REFERENCE = (SKILL_ROOT / "references/grok-cli.md").read_text(encoding="utf-8")
TOOLS_DUMP = (SKILL_ROOT / "references/grok-tools.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
LIVE_HELP_POLICY = (
    "Live `grok --help` and `~/.grok/docs/user-guide/` are authoritative when they differ."
)
TOOLS_DUMP_STAMP = "grok 1.0.30 (04b7ffed98c6) [stable]"
PLUGIN = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
CLAUDE_PLUGIN = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
GROK_PLUGIN = json.loads((ROOT / ".grok-plugin/plugin.json").read_text(encoding="utf-8"))
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

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
    def test_plugin_identity_matches_source_layout(self) -> None:
        self.assertEqual(PLUGIN["name"], ROOT.name)
        self.assertEqual(PLUGIN["name"], SKILL_ROOT.name)
        self.assertEqual(PLUGIN["skills"], "./skills/")
        self.assertEqual(PLUGIN["interface"]["developerName"], "toolbox.md")
        self.assertEqual(PLUGIN["repository"], "https://github.com/toolboxmd/use-grok")
        self.assertEqual(PLUGIN["version"], VERSION)
        for manifest in (PLUGIN, CLAUDE_PLUGIN, GROK_PLUGIN):
            self.assertEqual(manifest["name"], "use-grok")
            self.assertEqual(manifest["version"], VERSION)
        self.assertNotEqual(PLUGIN["name"], "toolboxmd-use-grok")

    def test_frontmatter_matches_current_skill_specs(self) -> None:
        top_level_keys = {
            match.group(1)
            for match in re.finditer(r"^([a-z][a-z0-9-]*):", FRONTMATTER, re.MULTILINE)
        }
        self.assertTrue(top_level_keys <= PORTABLE_FRONTMATTER_KEYS)
        self.assertNotIn("disable-model-invocation", FRONTMATTER)
        self.assertNotIn("argument-hint", FRONTMATTER)
        name = fm_line("name")
        self.assertEqual(name, SKILL_ROOT.name)
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
        openai = (SKILL_ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn("allow_implicit_invocation: true", openai)
        self.assertIn('display_name: "Use Grok"', openai)
        self.assertIn('short_description: "Consult the local Grok Build CLI"', openai)

    def test_host_invocation_syntax_is_documented(self) -> None:
        self.assertIn("`/use-grok`", SKILL)
        self.assertIn("`$use-grok`", SKILL)
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
        self.assertIn("Do **not** add `--no-subagents`, `--disable-web-search`, `--tools`", SKILL)
        self.assertNotIn("--deny Read", SKILL)
        self.assertNotIn("consult-grok", SKILL)
        self.assertNotIn("--mode explicit", SKILL)
        self.assertNotIn("Automatic review", SKILL)

    def test_hybrid_references_and_live_help_policy(self) -> None:
        self.assertIn("[references/grok-cli.md](references/grok-cli.md)", SKILL)
        self.assertIn("[references/grok-tools.md](references/grok-tools.md)", SKILL)
        self.assertIn(LIVE_HELP_POLICY, SKILL)
        self.assertIn(LIVE_HELP_POLICY, REFERENCE)
        self.assertNotIn("Grok CLI 1.0.5", SKILL)
        self.assertNotIn("Grok CLI 1.0.5", REFERENCE)
        self.assertNotIn("Grok CLI 1.0.5", README)
        self.assertIn("Never pass `--tools` to list tools", SKILL)
        self.assertIn("Never pass `--tools` to list tools", REFERENCE)
        self.assertIn("Never pass `--tools` to list tools", TOOLS_DUMP)

    def test_session_recipes_teach_resume_fork_rewind_and_export(self) -> None:
        self.assertIn("### Continue a prior consult", SKILL)
        self.assertIn("### Alternate history", SKILL)
        self.assertIn("--resume \"<sessionId>\"", SKILL)
        self.assertIn("--fork-session", SKILL)
        self.assertIn("Do not rewind the only copy", SKILL)
        self.assertIn("`/rewind`", SKILL)
        self.assertIn("files on disk stay", SKILL)
        self.assertIn("grok export \"<sessionId>\"", SKILL)
        self.assertIn("creates a new UUID only", SKILL)
        self.assertIn("`--worktree` is not combinable with `--fork-session`", SKILL)
        self.assertIn("Auth failure: `grok login` or `XAI_API_KEY`.", SKILL)

    def test_named_x_media_and_subagent_teaching(self) -> None:
        for tool in (
            "x_user_search",
            "x_semantic_search",
            "x_keyword_search",
            "x_thread_fetch",
            "image_gen",
            "image_edit",
            "image_to_video",
            "reference_to_video",
        ):
            self.assertIn(f"`{tool}`", SKILL)
        for kind in ("explore", "plan", "general-purpose"):
            self.assertIn(f"`{kind}`", SKILL)
        self.assertIn("search the web and open pages", SKILL)
        self.assertNotIn("open_page", SKILL)
        self.assertNotIn("open_page_with_find", SKILL)
        self.assertNotIn("api.x.ai", SKILL)
        self.assertNotIn("images/generations", SKILL)

    def test_when_to_use_map_covers_inspect_usage_and_session_controls(self) -> None:
        self.assertIn("`grok usage <sessionId>`", REFERENCE)
        self.assertIn("`grok inspect`", REFERENCE)
        self.assertIn("`grok inspect --json`", REFERENCE)
        self.assertIn("`grok sessions list`", REFERENCE)
        self.assertIn("`grok sessions search", REFERENCE)
        self.assertIn("`grok models`", REFERENCE)
        self.assertIn("`--max-turns", REFERENCE)
        self.assertIn("`--json-schema", REFERENCE)
        self.assertIn("`--restore-code`", REFERENCE)
        self.assertIn("`--worktree`", REFERENCE)
        self.assertIn("not combinable with `--fork-session`", REFERENCE)
        self.assertIn("`--sandbox`", REFERENCE)
        self.assertIn("`--disallowed-tools`", REFERENCE)
        for kind in ("general-purpose", "explore", "plan"):
            self.assertIn(f"`{kind}`", REFERENCE)

    def test_tools_dump_has_provenance_stamp_and_builtin_ids(self) -> None:
        self.assertIn(TOOLS_DUMP_STAMP, TOOLS_DUMP)
        self.assertIn(TOOLS_DUMP_STAMP, REFERENCE)
        self.assertIn("If `grok --version` differs, this list may be incomplete", TOOLS_DUMP)
        self.assertIn("Machine-local MCP servers are omitted", TOOLS_DUMP)
        for tool in (
            "web_search",
            "open_page",
            "open_page_with_find",
            "web_fetch",
            "x_user_search",
            "x_semantic_search",
            "x_keyword_search",
            "x_thread_fetch",
            "read_file",
            "search_replace",
            "write",
            "grep",
            "list_dir",
            "run_terminal_command",
            "get_command_or_subagent_output",
            "kill_command_or_subagent",
            "monitor",
            "image_gen",
            "image_edit",
            "image_to_video",
            "reference_to_video",
            "spawn_subagent",
            "todo_write",
            "ask_user_question",
            "enter_plan_mode",
            "exit_plan_mode",
            "workflow",
            "search_tool",
            "use_tool",
            "scheduler_create",
            "scheduler_delete",
            "scheduler_list",
            "send_feedback",
        ):
            self.assertIn(f"`{tool}`", TOOLS_DUMP)
        self.assertIn("Do not treat `code_interpreter`, LSP tools, or `memory_search` as guaranteed", TOOLS_DUMP)

    def test_repository_text_follows_global_style(self) -> None:
        self.assertNotIn("\N{EM DASH}", SKILL)
        self.assertNotIn("\N{EM DASH}", README)
        self.assertNotIn("\N{EM DASH}", REFERENCE)
        self.assertNotIn("\N{EM DASH}", TOOLS_DUMP)

    def test_goal_recipes_exist(self) -> None:
        for heading in (
            "### Research",
            "### Implement / coding",
            "### Review / second opinion",
            "### Continue a prior consult",
            "### Alternate history",
        ):
            self.assertIn(heading, SKILL)
        self.assertIn("Goal: research", SKILL)
        self.assertIn("Goal: implement", SKILL)
        self.assertIn("Goal: review", SKILL)


if __name__ == "__main__":
    unittest.main(verbosity=2)
