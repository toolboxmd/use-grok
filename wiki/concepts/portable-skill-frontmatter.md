---
title: "Portable SKILL.md frontmatter in use-grok"
type: concepts
tags: [agent-skills, skill-frontmatter, openai, claude, portability]
sources:
  - raw/2026-08-21T17-23-52Z-portable-skill-frontmatter-across-openai-and-claude.md
  - raw/2026-08-21T17-23-53Z-use-grok-SKILL.md
  - raw/2026-08-21T17-51-11Z-installing-a-local-skill-as-a-personal-codex-plugin.md
  - raw/2026-08-21T18-00-05Z-toolboxmd-marketplace-and-use-grok-naming-convention.md
related:
  - /concepts/unrestricted-grok-delegation.md
  - /entities/toolboxmd-use-grok-personal-codex-plugin.md
  - /concepts/use-grok-codex-plugin-identity.md
created: "2026-08-22T07:12:19Z"
updated: "2026-08-22T07:28:35Z"
quality:
  accuracy: 5
  completeness: 5
  signal: 5
  interlinking: 5
  overall: 5.0
  rated_at: "2026-08-22T07:28:35Z"
  rated_by: ingester
---

The `use-grok` skill is shipped as a portable Agent Skills package. Keep `skills/use-grok/SKILL.md` on the six standard frontmatter keys so the same file works in ChatGPT, Codex, Claude Code, claude.ai, and the Claude Skills API.

## What this repo actually ships

`skills/use-grok/SKILL.md` currently declares only portable keys:

- `name: use-grok` (matches the parent directory `skills/use-grok/`)
- `description` stating both what the skill does (delegate to the local Grok Build CLI) and when it applies (only when the user asks to consult Grok)
- `license: Apache-2.0`
- `compatibility` requiring a local `grok` CLI on PATH plus `grok login` or `XAI_API_KEY`
- `metadata.short-description: Consult local Grok Build CLI`

There is no `argument-hint`, `disable-model-invocation`, `user-invocable`, `when_to_use`, `arguments`, tool field, model field, context, agents, hooks, or paths key in this SKILL.md. That is intentional. Claude Code accepts those local-only keys, but claude.ai uploads, Skills API uploads, and `package_skill.py` reject them.

OpenAI-specific UI and invocation policy live in `skills/use-grok/agents/openai.yaml`, not in SKILL.md:

```yaml
interface:
  display_name: "Use Grok"
  short_description: "Consult the local Grok Build CLI"

policy:
  allow_implicit_invocation: true
```

`policy.allow_implicit_invocation` defaults to true on the OpenAI side. This repo sets it true explicitly. Implicit matching remains allowed; explicit `$use-grok` / `@` selection still works if a host later sets the flag false.

Omitting `disable-model-invocation` preserves Claude Code's default model-invocable behavior. The skill description already gates auto-use ("Do not use unless the user asked to consult Grok"). Adding `disable-model-invocation: true` would force slash-command-only invocation and would be a Claude Code-only key, so it must not be added to SKILL.md.

## Portable contract (checked 2026-08-21)

Agent Skills required keys: `name`, `description`. Optional: `license`, `compatibility`, `metadata`, experimental `allowed-tools`.

`name` must be 1 to 64 characters, lowercase ASCII letters, digits, and hyphens only, not start or end with a hyphen, not contain consecutive hyphens, and match the parent directory name. `use-grok` satisfies that. `description` must be 1 to 1024 characters. `compatibility` is capped at 500 characters. `metadata` is a string-to-string map.

Keep SKILL.md under 500 lines. This skill already moves CLI flag catalog detail into `skills/use-grok/references/grok-cli.md`.

OpenAI (ChatGPT and Codex) uses `name` and `description` for progressive disclosure and implicit matching. Front-load trigger words in `description`. Plugins are the recommended distribution path for reusable skills.

Claude portable surfaces accept only: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. An extra key such as `argument-hint` produces:

`Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name`

## Edit rule for this repo

When changing `skills/use-grok/SKILL.md` frontmatter:

1. Stay on the six standard keys.
2. Put OpenAI UI names and `policy.allow_implicit_invocation` in `agents/openai.yaml`.
3. Do not add Claude Code-only keys to SKILL.md even if they would be convenient locally.
4. Leave `disable-model-invocation` unset so Claude Code can still select the skill from natural-language "consult Grok" prompts, matching the OpenAI implicit-invocation policy.

## Auto-invocation trigger (this repo, 2026-08-21)

The host should select `use-grok` only for requests that explicitly ask to ask, send, pass, delegate to, or consult Grok. Do not select it merely because Grok might be useful. That boundary is carried by the portable `description`, not by a SKILL.md flag.

Automatic selection uses host defaults rather than a non-portable SKILL.md field. There is no portable `model-invocation: true` field. OpenAI keeps `policy.allow_implicit_invocation: true` in `skills/use-grok/agents/openai.yaml`. Claude Code receives no `disable-model-invocation` field, so its documented default `false` for that disabling field applies and the model may invoke the skill. Omitting the Claude-specific field also keeps SKILL.md compatible with claude.ai and the Claude Skills API, whose upload schema rejects non-standard fields such as `disable-model-invocation` and `argument-hint`.

The portable revision is commit `9096556259580a484661e5d08012974a444db687` on `main` (`feat: modernize Grok delegation skill`). It adds `agents/openai.yaml`, documents ChatGPT `@`, Codex `$`, and Claude Code `/` invocation, and narrows compatibility to environments with a local shell and `grok` executable.

Runtime tool approval is a separate product decision: see [Unrestricted Grok delegation in use-grok](/concepts/unrestricted-grok-delegation.md).

## Personal Codex plugin packaging (this repo, 2026-08-21)

This skill was also installed as a personal Codex plugin so Codex can load it from the local marketplace. The plugin bundle keeps `skills/use-grok/agents/openai.yaml` with `policy.allow_implicit_invocation: true`, the same OpenAI invocation policy as the source skill. Source changes do not reach Codex until that personal plugin copy is repackaged. See [toolboxmd-use-grok personal Codex plugin](/entities/toolboxmd-use-grok-personal-codex-plugin.md).

The source skill name is already `use-grok` and already matches `skills/use-grok/`. The 2026-08-21 marketplace capture says the bundled plugin skill must stay `use-grok` as well, producing `$use-grok` in Codex and `/use-grok` in Claude Code, while the installed plugin identity should be `use-grok@toolboxmd` rather than `toolboxmd-use-grok@personal`. Plugin identity is separate from SKILL.md portability. See [use-grok Codex plugin identity and ToolboxMD marketplace](/concepts/use-grok-codex-plugin-identity.md).

Sources checked 2026-08-21: https://developers.openai.com/codex/skills (redirects to https://learn.chatgpt.com/docs/build-skills), https://code.claude.com/docs/en/slash-commands, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, https://agentskills.io/specification.
