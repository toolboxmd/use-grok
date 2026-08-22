---
title: "use-grok Codex plugin identity and ToolboxMD marketplace"
type: concepts
tags: [agent-skills, use-grok, openai, marketplace]
sources:
  - raw/2026-08-21T18-00-05Z-toolboxmd-marketplace-and-use-grok-naming-convention.md
related:
  - /entities/toolboxmd-use-grok-personal-codex-plugin.md
  - /concepts/portable-skill-frontmatter.md
created: "2026-08-22T07:28:35Z"
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

This repo's Codex plugin should install as `use-grok@toolboxmd`. The first local install as `toolboxmd-use-grok@personal` was valid for testing, but it does not match the ToolboxMD distribution convention. Publisher namespace belongs in the marketplace suffix, not inside the plugin name.

## Target identities (this repo, 2026-08-21)

Keep three names distinct:

| Layer | Target | Notes |
| --- | --- | --- |
| Installed Codex plugin | `use-grok@toolboxmd` | Marketplace suffix carries ToolboxMD. Do not ship `toolboxmd-use-grok@toolboxmd`. |
| Bundled skill | `use-grok` | `SKILL.md` frontmatter `name` must match the containing skill directory. Codex invocation is `$use-grok`; Claude Code is `/use-grok`. Natural-language auto-selection stays intact. |
| GitHub repository | may remain `toolboxmd-use-grok` | Repo name is independent of plugin id and skill name. Renaming the repo to `use-grok` under `github.com/toolboxmd` would make the three identities line up, but it is not required for the plugin rename. |

The live local reference for the ToolboxMD marketplace is the `karpathy-wiki` project at `/Users/lukaszmaj/dev/toolboxmd/karpathy-wiki`. Its marketplace manifest is `.agents/plugins/marketplace.json` with top-level `name: toolboxmd` and interface `displayName: toolbox.md`. That plugin is installed as `karpathy-wiki@toolboxmd`. This Grok plugin should use the same marketplace suffix, not a personal marketplace.

This repo's source skill is already named `use-grok`. See [Portable SKILL.md frontmatter in use-grok](/concepts/portable-skill-frontmatter.md). If a bundled plugin copy currently uses `toolboxmd-use-grok` as the skill name or directory, rename that bundled skill to `use-grok` so it matches the source skill.

## Why `toolboxmd-use-grok@personal` is the wrong distribution identity

The 2026-08-21 personal install is recorded in [toolboxmd-use-grok personal Codex plugin](/entities/toolboxmd-use-grok-personal-codex-plugin.md). That layout (`~/plugins/toolboxmd-use-grok`, `codex plugin add toolboxmd-use-grok@personal`, cache under `~/.codex/plugins/cache/personal/toolboxmd-use-grok/0.1.0`) was a local test, not the ToolboxMD catalog identity.

Repeating `toolboxmd` in the plugin name produces the redundant installed id `toolboxmd-use-grok@toolboxmd` once the plugin moves under the ToolboxMD marketplace. The marketplace already names the publisher.

This is a migration of installed identity, not a cosmetic rename. Leave the personal install in place until `use-grok@toolboxmd` validates and installs. Only then uninstall `toolboxmd-use-grok@personal`.

## Immediate local correction (this machine, 2026-08-21)

Using the currently configured ToolboxMD marketplace root:

1. Place a packaged `use-grok` directory inside `/Users/lukaszmaj/dev/toolboxmd/karpathy-wiki`.
2. Add it to that marketplace's `plugins` array.
3. Install `use-grok@toolboxmd`.
4. After the replacement validates, remove `toolboxmd-use-grok@personal`.

Do not point the `karpathy-wiki` marketplace at this repo through an outside-root `source.path`. OpenAI plugin packaging (checked 2026-08-21 at https://developers.openai.com/plugins/build/plugins and https://learn.chatgpt.com/docs/plugins) distinguishes repo and personal marketplaces:

- One marketplace can hold multiple plugins under one top-level marketplace name.
- Repo marketplaces live at `$REPO_ROOT/.agents/plugins/marketplace.json`.
- Each local `source.path` must be relative to the marketplace root, begin with `./`, and stay inside that root.

Making `karpathy-wiki`'s repository permanently own this sibling plugin via an outside-root path would violate that path guidance and make remote distribution brittle.

## Durable marketplace shape (not this ingest)

A robust multi-plugin ToolboxMD umbrella should eventually use a dedicated ToolboxMD marketplace repository, or a monorepo that contains both plugin packages. The immediate local copy inside `karpathy-wiki` is a correction of the currently configured marketplace root, not a decision to keep `use-grok` nested there forever.

Sources checked 2026-08-21:

- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/plugins
- `/Users/lukaszmaj/dev/toolboxmd/karpathy-wiki/.agents/plugins/marketplace.json`
- `/Users/lukaszmaj/dev/toolboxmd/karpathy-wiki/.codex-plugin/plugin.json`
- Local Codex CLI marketplace and plugin listings
