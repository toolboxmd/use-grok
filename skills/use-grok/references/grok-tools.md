# Grok built-in tools

Pinned dump of built-in agent tools captured from `grok 1.0.30 (04b7ffed98c6) [stable]`. Compare `grok --version` to `1.0.30 (04b7ffed98c6)`; `[stable]` is channel metadata and is not part of `grok --version` output. If the version or git hash differs, this list may be incomplete. Never pass `--tools` to list tools; on this CLI it is an allowlist and requires a value, and passing it drops everything else.

Machine-local MCP servers are omitted. For skills, plugins, and MCP, run `grok inspect --json`.

Do not treat `code_interpreter`, LSP tools, or `memory_search` as guaranteed. They may exist in the binary or settings without being injected in a given session.

| Tool | What it does |
|------|--------------|
| `web_search` | Search the web |
| `open_page` | Fetch text from a URL |
| `open_page_with_find` | Fetch a URL and search it with a regex |
| `web_fetch` | Fetch a URL as markdown |
| `x_user_search` | Search for an X user |
| `x_semantic_search` | Semantic search of X posts |
| `x_keyword_search` | Keyword and advanced search of X posts |
| `x_thread_fetch` | Fetch an X post and its thread |
| `read_file` | Read a file |
| `search_replace` | Line-precise edit |
| `write` | Create or overwrite a file |
| `grep` | Regex search with ripgrep |
| `list_dir` | List a directory |
| `run_terminal_command` | Shell |
| `get_command_or_subagent_output` | Read output from a background command or subagent |
| `kill_command_or_subagent` | Stop a background command or subagent |
| `monitor` | Stream events from a long-running command |
| `image_gen` | Generate an image from a text description |
| `image_edit` | Edit existing images |
| `image_to_video` | Animate a source image into a video |
| `reference_to_video` | Generate a video from reference images and/or voices |
| `spawn_subagent` | Child session |
| `todo_write` | Task list |
| `ask_user_question` | Ask the user a structured question |
| `enter_plan_mode` | Enter plan mode |
| `exit_plan_mode` | Leave plan mode |
| `workflow` | Run a saved workflow |
| `search_tool` | Find MCP tools |
| `use_tool` | Call an MCP tool |
| `scheduler_create` | Create a recurring task |
| `scheduler_delete` | Cancel a recurring task |
| `scheduler_list` | List recurring tasks |
| `send_feedback` | Send product feedback |
