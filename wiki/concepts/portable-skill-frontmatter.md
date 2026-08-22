---
title: "Portable SKILL.md frontmatter in use-grok"
type: concepts
tags: [agent-skills, skill-frontmatter, openai, claude, portability]
sources:
  - raw/2026-08-21T17-23-52Z-portable-skill-frontmatter-across-openai-and-claude.md
created: "2026-08-22T07:12:19Z"
updated: "2026-08-22T07:12:19Z"
quality:
  accuracy: 5
  completeness: 4
  signal: 5
  interlinking: 3
  overall: 4.25
  rated_at: "2026-08-22T07:12:19Z"
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

Sources checked 2026-08-21: https://developers.openai.com/codex/skills (redirects to https://learn.chatgpt.com/docs/build-skills), https://code.claude.com/docs/en/slash-commands, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview, https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, https://agentskills.io/specification.
