# toolboxmd-use-grok

A skill that teaches a host agent how to delegate to the local Grok Build CLI for research, coding, review, or a second opinion, without wrapping `grok` in an adapter.

The host writes a brief and runs `grok` with `--cwd` at the workspace and `--always-approve`. Grok sees the repo because that is its working directory. Subagents, shell, web search, and file edits stay enabled unless the user asked to restrict them.

The skill targets local Codex and Claude Code environments where `grok` is installed. A hosted environment can use it only when the Grok executable is available there.

## Layout

- `SKILL.md`: when to consult Grok, default command, completion rules, and goal recipes.
- `references/grok-cli.md`: Grok CLI 1.0.5 flags, tools, subagents, and session controls.
- `agents/openai.yaml`: Codex / ChatGPT skill display name and implicit-invocation policy.
- `tests/toolboxmd-use-grok.test.py`: portable frontmatter and workflow contract.

## Test

```bash
bash tests/toolboxmd-use-grok.test.sh
```

## License

Apache 2.0. See `LICENSE`.
