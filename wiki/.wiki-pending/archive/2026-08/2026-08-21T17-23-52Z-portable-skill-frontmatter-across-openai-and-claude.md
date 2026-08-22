---
title: "Portable skill frontmatter across OpenAI and Claude"
evidence: "conversation"
evidence_type: "conversation"
capture_kind: "chat-only"
suggested_action: "create"
suggested_pages: []
attachments: []
captured_at: "2026-08-21T17-23-52Z"
captured_by: "in-session-agent"
capture_id: "cap-c36c43ee785e43ac86313b08ebfdc075"
promotion_policy: "selective"
promotion_decision: "promoted"
promotion_id: "prom-48a6fb449632d01925a7dfb4"
propagated_from: null
---

---
title: "Portable skill frontmatter across OpenAI and Claude"
orphaned_at: "2026-08-21T16-13-43Z"
reason: "headless: workspace routing is unconfigured; run wiki use project|main|both"
---

OpenAI and Anthropic now converge on the Agent Skills open standard for portable SKILL.md packages, but Claude Code supports additional local-only frontmatter that is not portable to Claude.ai or the Claude Skills API.

Portable Agent Skills frontmatter has two required fields: `name` and `description`. The standard allows four optional fields: `license`, `compatibility`, `metadata`, and experimental `allowed-tools`. `name` must be 1 to 64 characters, contain lowercase ASCII letters, digits, and hyphens only, not start or end with a hyphen, not contain consecutive hyphens, and match the parent directory name. `description` must be 1 to 1024 characters and should state both what the skill does and when it applies. `compatibility`, if present, is capped at 500 characters. `metadata` is a string-to-string map. Keep SKILL.md under 500 lines and move conditional or detailed material into one-level-deep references for progressive disclosure.

OpenAI documentation says ChatGPT and Codex use `name` and `description` for progressive disclosure and implicit matching. It recommends concise descriptions with key use cases and trigger words front-loaded. OpenAI additionally supports optional `agents/openai.yaml` for UI fields, tool dependencies, and invocation policy. `policy.allow_implicit_invocation` defaults to true; false disables implicit selection while retaining explicit `$skill` invocation. ChatGPT explicit selection uses `@`; Codex CLI and IDE can use `$` and `/skills`. OpenAI recommends plugins when distributing reusable skills rather than only authoring them locally.

Claude Code accepts local-only extensions including `argument-hint`, `disable-model-invocation`, `user-invocable`, `when_to_use`, `arguments`, tool fields, model fields, context, agents, hooks, and paths. This does not mean those keys are portable. The current Claude Code documentation explicitly states that claude.ai uploads, Skills API uploads, and `package_skill.py` accept only `name`, `description`, `license`, `compatibility`, `metadata`, and `allowed-tools`. An extra key such as `argument-hint` produces the hard error: `Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name`. Therefore a skill meant for both OpenAI and all Claude surfaces should keep SKILL.md frontmatter to the six standard keys and place OpenAI-specific invocation policy in `agents/openai.yaml`. Omitting `disable-model-invocation` preserves Claude Code's default model-invocable behavior.

Claude Code recommends `disable-model-invocation: true` for workflows with side effects or timing that users should control directly. That is a product-specific safety choice, not part of the portable standard. If a skill intentionally permits model selection only after explicit natural-language trigger phrases, document that policy clearly and assess whether unrestricted tool approval is consistent with the action semantics.

Sources checked 2026-08-21:
- https://developers.openai.com/codex/skills (redirects to https://learn.chatgpt.com/docs/build-skills)
- https://code.claude.com/docs/en/slash-commands (current Claude Code Skills page)
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://agentskills.io/specification
