# Grok CLI when-to-use

Last checked against `grok 1.0.30 (04b7ffed98c6) [stable]`. Compare `grok --version` to `1.0.30 (04b7ffed98c6)`; `[stable]` is channel metadata and is not part of `grok --version` output. This is a when-to-use map, not a flag dump and not a supported-version contract. Live `grok --help` and `~/.grok/docs/user-guide/` are authoritative when they differ. Run `grok <cmd> --help` for a named subcommand.

The default consult in `SKILL.md` needs none of the extras below.

## Continue the same consult

Use `--resume "<sessionId>"` with the prior JSON `.sessionId`. Linear follow-up keeps later history on that session.

Find a session: `grok sessions list` or `grok sessions search <query>`.

## Alternate history

Keep the source id. Fork with `--resume "<sourceSessionId>" --fork-session` and a throwaway prompt (headless requires a prompt). The child id is JSON `.sessionId`, or the unused UUID from optional `--session-id`. Then rewind **only the child**.

`/rewind` (alias `/undo`) is a TUI slash command on that child, not a CLI flag. It opens a rewind-point picker. Do not rewind the source.

Do not rewind the only copy. `/rewind` truncates conversation history to an earlier user prompt; files on disk stay. See `~/.grok/docs/user-guide/17-sessions.md`.

Then `--resume "<childSessionId>"` with the real alternate brief. The source stays resumable with `--resume "<sourceSessionId>"`.

`--session-id` sets a new unused UUID; it does not resume. With `-r`/`-c` it is valid only with `--fork-session`.

`--worktree` starts the session in a new git worktree. It is not combinable with `--fork-session`. `--restore-code` restores the original session's repository snapshot when resuming (remote sessions require `--worktree`).

## Recover the exact answer

JSON `.text` is the final answer. If the TUI or stdout looks truncated, run `grok export <sessionId>`. Do not treat a partial display as complete.

## Cost of that consult

`grok usage <sessionId>` prints persisted token and cost usage for the session.

## What Grok loaded for this workspace

`grok inspect` or `grok inspect --json` shows discovered skills, plugins, MCP servers, agents, permissions, and config.

Inspect does not enumerate built-in tool ids such as `image_gen`. Those stay available because the default invoke does not pass `--tools`. Never pass `--tools` to list tools: on this CLI it is a headless allowlist and drops everything else.

For every built-in id captured from grok 1.0.30, read [grok-tools.md](grok-tools.md). If the live version or git hash differs from `1.0.30 (04b7ffed98c6)`, ask Grok in the brief to list tools, or trust the live session.

## Models and turn caps

- `grok models`: live model list and default.
- `--max-turns <n>`: cap model rounds in headless mode.
- `--json-schema <schema>`: constrain the final answer; implies JSON output.

## Media, X, web, subagents

Put the ask in the brief. Grok uses its tools when unrestricted:

- Web: search the web and open pages.
- X: `x_user_search`, `x_semantic_search`, `x_keyword_search`, `x_thread_fetch`.
- Media: `image_gen`, `image_edit`, `image_to_video`, `reference_to_video`.
- Subagents: `explore`, `plan`, `general-purpose`. Do not pass `--no-subagents` unless asked.

## Restrict only when asked

Do not add `--tools`, `--no-subagents`, `--disable-web-search`, `--disallowed-tools`, or `--sandbox` unless the user asked to restrict Grok. `--tools` is an allowlist. `--disallowed-tools` removes named ids and wins over `--tools`. `--sandbox` applies a kernel filesystem and network profile.

## Stay out of skill recipes

Do not teach these as consult recipes: `dashboard`, `leader`, `grok agent stdio`/`serve`, `cursor-worker`, `clone`, `wrap`, `plugin`, `mcp`, `memory`, `doctor`, `update`, `setup`, `trace`, `completions`, `--minimal`, `--fullscreen`.
