# use-grok

A Codex plugin and portable Agent Skill that teach a host agent how to delegate to the local Grok Build CLI for research, coding, review, or a second opinion, without wrapping `grok` in an adapter.

The host writes a brief and runs `grok` with `--cwd` at the workspace and `--always-approve`. Grok sees the repo because that is its working directory. Subagents, shell, web search, and file edits stay enabled unless the user asked to restrict them.

The skill targets local Codex and Claude Code environments where `grok` is installed. A hosted environment can use it only when the Grok executable is available there.

## Layout

- `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, `.grok-plugin/plugin.json`: plugin identity on Codex, Claude Code, and Grok Build.
- `skills/use-grok/SKILL.md`: when to consult Grok, default command, completion rules, and goal recipes.
- `skills/use-grok/references/grok-cli.md`: Grok CLI 1.0.5 flags, tools, subagents, and session controls.
- `skills/use-grok/agents/openai.yaml`: Codex / ChatGPT skill display name and implicit-invocation policy.
- `tests/use-grok.test.py`: plugin, portable frontmatter, and workflow contracts.

## Install

Add marketplace toolboxmd, then install this plugin. Identity is
`use-grok@toolboxmd`.

```bash
codex plugin marketplace add toolboxmd/marketplace
codex plugin add use-grok@toolboxmd
```

```bash
grok plugin marketplace add toolboxmd/marketplace
grok plugin install use-grok --trust
```

Claude Code: add extraKnownMarketplaces `toolboxmd` pointing at
`toolboxmd/marketplace`, then enable `use-grok@toolboxmd`.

## Test

```bash
bash tests/use-grok.test.sh
```

## Project maintenance

[VISION.md](VISION.md), [MISSION.md](MISSION.md), and
[OBJECTIVE.md](OBJECTIVE.md) define Project Direction.
[Versioning and release](docs/versioning.md) describes the canonical version,
manifest mirrors, deterministic checks, and manual release boundary.

## License

Apache 2.0. See `LICENSE`.
