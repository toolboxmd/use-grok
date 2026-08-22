---
title: "toolboxmd-use-grok personal Codex plugin"
type: entities
tags: [agent-skills, use-grok, openai]
sources:
  - raw/2026-08-21T17-51-11Z-installing-a-local-skill-as-a-personal-codex-plugin.md
related:
  - /concepts/portable-skill-frontmatter.md
  - /concepts/unrestricted-grok-delegation.md
created: "2026-08-22T07:22:46Z"
updated: "2026-08-22T07:22:46Z"
quality:
  accuracy: 5
  completeness: 5
  signal: 5
  interlinking: 5
  overall: 5.0
  rated_at: "2026-08-22T07:22:46Z"
  rated_by: ingester
---

This repo's `use-grok` skill was packaged as a personal Codex plugin named `toolboxmd-use-grok` at version 0.1.0 and installed through the local personal marketplace. The record below is the 2026-08-21 install captured in conversation, not a live path check on 2026-08-22.

## Layout that was validated

The install used this local personal-plugin layout:

- plugin root: `~/plugins/toolboxmd-use-grok`
- required manifest: `.codex-plugin/plugin.json`
- skill package: `skills/use-grok/SKILL.md`
- OpenAI metadata beside the skill: `skills/use-grok/agents/openai.yaml`
- references: `skills/use-grok/references/`

That keeps the standalone skill package inside the plugin instead of flattening it.

The plugin manifest included name, version, description, author, license, homepage, repository, keywords, skills path, and interface metadata. The interface identified the plugin as Use Grok and said it delegates research, coding, and reviews to the local Grok Build CLI.

The bundled skill kept `policy.allow_implicit_invocation` set to `true` in `agents/openai.yaml`, matching the source skill's OpenAI invocation policy. See [Portable SKILL.md frontmatter in use-grok](/concepts/portable-skill-frontmatter.md). The packaged skill also kept unrestricted Grok execution. See [Unrestricted Grok delegation in use-grok](/concepts/unrestricted-grok-delegation.md).

## Personal marketplace install (Codex CLI 0.149.0)

The personal marketplace file is `~/.agents/plugins/marketplace.json`. Its top-level name is `personal`. The plugin entry used a local source path relative to the marketplace directory.

Install command:

```bash
codex plugin add toolboxmd-use-grok@personal
```

Codex reported the plugin installed and enabled at version 0.1.0 and cached the resolved package at `~/.codex/plugins/cache/personal/toolboxmd-use-grok/0.1.0`. A new Codex session is required before newly installed plugin skills appear in session discovery.

## Source copy versus installed copy

The capture named the Git source as `/Users/lukaszmaj/dev/toolboxmd/toolboxmd-use-grok` at commit `9096556259580a484661e5d08012974a444db687` on `main`. The installed personal plugin was a packaged local copy at `/Users/lukaszmaj/plugins/toolboxmd-use-grok`. Source edits do not reach Codex until that personal plugin is repackaged or updated.

At ingest time on 2026-08-22, those source, plugin, and cache paths were not present on disk. Treat the paths and version as the captured 2026-08-21 install, not as current live locations.

## plugin-creator validator needed PyYAML

The plugin-creator validator failed before validating this plugin because its Python interpreter lacked the `yaml` module. That was a validator runtime dependency, not a manifest defect. The same validator passed when run in an isolated uv environment with PyYAML supplied:

```bash
uv run --with pyyaml python <validate_plugin.py> <plugin-root>
```

## Evidence checked 2026-08-21

- https://learn.chatgpt.com/docs/plugins
- Codex CLI 0.149.0 output from `codex plugin add` and `codex plugin list`
- Local plugin validator from the installed plugin-creator skill
