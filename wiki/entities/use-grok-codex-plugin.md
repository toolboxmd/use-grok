---
title: "use-grok Codex plugin (ToolboxMD)"
type: entities
tags: [agent-skills, use-grok, openai, marketplace]
sources:
  - raw/2026-08-21T18-09-41Z-plugin.json
related:
  - /concepts/use-grok-codex-plugin-identity.md
  - /entities/toolboxmd-use-grok-personal-codex-plugin.md
  - /concepts/portable-skill-frontmatter.md
  - /concepts/unrestricted-grok-delegation.md
created: "2026-08-22T07:33:52Z"
updated: "2026-08-22T07:33:52Z"
quality:
  accuracy: 5
  completeness: 5
  signal: 5
  interlinking: 5
  overall: 5.0
  rated_at: "2026-08-22T07:33:52Z"
  rated_by: ingester
---

This checkout is the ToolboxMD Codex plugin `use-grok` at version 0.1.0. The local path is `/Users/lukaszmaj/dev/toolboxmd/use-grok`. The public GitHub repository is `https://github.com/toolboxmd/use-grok`.

## Plugin root (captured 2026-08-21)

The repository is a Codex plugin root. The manifest is `.codex-plugin/plugin.json`. The copied evidence file records:

- `name: use-grok`
- `version: 0.1.0`
- `skills: ./skills/`
- `license: Apache-2.0`
- `homepage` / `repository`: `https://github.com/toolboxmd/use-grok`
- `interface.developerName: toolbox.md`
- `interface.category: Developer Tools`
- `interface.displayName: Use Grok`

The portable skill lives at `skills/use-grok/SKILL.md` with frontmatter `name: use-grok`. OpenAI metadata is `skills/use-grok/agents/openai.yaml` and still has `policy.allow_implicit_invocation: true`. Explicit invocations are `$use-grok` in Codex and `/use-grok` in Claude Code or Grok. Unrestricted Grok permissions remain intentional. See [Portable SKILL.md frontmatter in use-grok](/concepts/portable-skill-frontmatter.md) and [Unrestricted Grok delegation in use-grok](/concepts/unrestricted-grok-delegation.md).

## Repository migration (this machine, 2026-08-21)

The Grok delegation project left the redundant `toolboxmd-use-grok` identity:

| Layer | Previous | Current |
| --- | --- | --- |
| Local checkout | `/Users/lukaszmaj/dev/toolboxmd/toolboxmd-use-grok` | `/Users/lukaszmaj/dev/toolboxmd/use-grok` |
| GitHub repository | `https://github.com/toolboxmd/toolboxmd-use-grok` | `https://github.com/toolboxmd/use-grok` |
| Installed Codex plugin | `toolboxmd-use-grok@personal` | `use-grok@toolboxmd` 0.1.0 |

The local `origin` remote uses the new GitHub URL. Source conversion commit `3fc4615af127bd07155de1b16cc137b56e5d4059` (`feat: package use-grok plugin`) was pushed to `toolboxmd/use-grok` `main`. The previous portable-skill revision `9096556259580a484661e5d08012974a444db687` was pushed with it. Local and remote `main` both resolved to `3fc4615af127bd07155de1b16cc137b56e5d4059` after the push.

This is the live successor to [toolboxmd-use-grok personal Codex plugin](/entities/toolboxmd-use-grok-personal-codex-plugin.md). Naming rules for why the personal id was wrong live in [use-grok Codex plugin identity and ToolboxMD marketplace](/concepts/use-grok-codex-plugin-identity.md).

## ToolboxMD marketplace (this machine, 2026-08-21)

The shared local marketplace moved to `/Users/lukaszmaj/dev/toolboxmd/.agents/plugins/marketplace.json`. Marketplace `name` is `toolboxmd`, `displayName` is `toolbox.md`. It exposes both `./karpathy-wiki` and `./use-grok`. Codex resolves the marketplace root as `/Users/lukaszmaj/dev/toolboxmd`.

Installed and enabled after the move:

- `karpathy-wiki@toolboxmd` 0.3.2
- `use-grok@toolboxmd` 0.1.0

The obsolete `toolboxmd-use-grok@personal` installation was removed. Its personal package and one-entry personal marketplace manifest were archived to Trash, not deleted permanently.

## Wiki routing after the directory rename

Renaming the checkout invalidated path-keyed Karpathy Wiki routing and trusted runtime records for the old path. The workspace was reconfigured in `both` mode at `/Users/lukaszmaj/dev/toolboxmd/use-grok`. A new trusted runtime was initialized for the existing project wiki with scheduled dispatch, Grok provider, `grok-4.6`, medium reasoning effort, one process, and auto-commit. Old path-keyed wiki and workspace runtime directories were archived to Trash.

Final scheduler status in the capture: zero invalid wikis, eight registered wikis, seven scheduled wikis, and no stalled or failed captures. Pending captures remained queued until the provider cooldown ended.

## Validator note (2026-08-21)

The Codex plugin validator passed the new repository. The bundled quick skill validator rejected the standard `compatibility` frontmatter key even though current portable Agent Skills guidance permits it. Compatibility was kept. That rejection was treated as a tool-schema mismatch, not as a reason to change the portable skill.
