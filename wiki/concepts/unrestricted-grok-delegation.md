---
title: "Unrestricted Grok delegation in use-grok"
type: concepts
tags: [agent-skills, grok-cli, always-approve, permissions, use-grok]
sources:
  - raw/2026-08-21T17-23-53Z-use-grok-SKILL.md
related:
  - /concepts/portable-skill-frontmatter.md
created: "2026-08-22T07:16:52Z"
updated: "2026-08-22T07:16:52Z"
quality:
  accuracy: 5
  completeness: 4
  signal: 5
  interlinking: 4
  overall: 4.5
  rated_at: "2026-08-22T07:16:52Z"
  rated_by: ingester
---

In this repo, `skills/use-grok/SKILL.md` runs the local `grok` CLI as a full agent with `--always-approve` and no sandbox or tool allowlist. Unrestricted permissions are an explicit product decision, not a missing safeguard.

## Default command

Always start from this. Do not add `--no-subagents`, `--disable-web-search`, `--tools`, `--disallowed-tools`, or `--sandbox` unless the user asked to restrict Grok.

```bash
grok \
  --prompt-file "<brief-path>" \
  --verbatim \
  --cwd "<workspace>" \
  --always-approve \
  --output-format json
```

`--always-approve` is `--yolo` and `--permission-mode bypassPermissions`. Tools run without prompts. Prefer `--prompt-file` plus `--verbatim` over `-p` so the brief is not smashed by the shell. A path in the brief is a hint; Grok sees the workspace because `--cwd` points at it.

The default command leaves shell, web search, editing, MCP, memory, and subagents enabled. It does not add a sandbox or tool allowlist. The skill text states: `Unrestricted permissions are intentional: this skill delegates to Grok as a full agent.`

## Brief-level "do not edit" is not a runtime restriction

Research and review recipes tell Grok not to modify files in the brief. Runtime capability still stays unrestricted by design. Add `--sandbox read-only` (or other restriction flags) only when the user explicitly asks to restrict Grok.

Optional catalog details live in `skills/use-grok/references/grok-cli.md` (Grok CLI 1.0.5 interface). The default invocation does not need that catalog.

## Portable revision that locked this in

Commit `9096556259580a484661e5d08012974a444db687` on `main` (`feat: modernize Grok delegation skill`) removed the wrapper `scripts/consult-grok`, added `agents/openai.yaml`, moved volatile Grok CLI 1.0.5 details into `references/grok-cli.md`, documented ChatGPT `@`, Codex `$`, and Claude Code `/` invocation, and narrowed compatibility to environments with a local shell and `grok` executable. The focused contract suite passed 9 of 9.

Host auto-selection of the skill is a separate decision: see [Portable SKILL.md frontmatter in use-grok](/concepts/portable-skill-frontmatter.md).
