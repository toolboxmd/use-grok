---
title: "Grok skill auto invocation and unrestricted delegation policy"
evidence: "/Users/lukaszmaj/dev/toolboxmd/toolboxmd-use-grok/SKILL.md"
evidence_type: "mixed"
capture_kind: "chat-attached"
suggested_action: "augment"
suggested_pages: []
attachments: []
captured_at: "2026-08-21T17-23-53Z"
captured_by: "in-session-agent"
capture_id: "cap-ef3e7e4c77d843948d7976c64781e0f0"
promotion_policy: "selective"
promotion_decision: null
promotion_id: null
propagated_from: null
---

---
title: "Grok skill auto invocation and unrestricted delegation policy"
orphaned_at: "2026-08-21T17-20-07Z"
reason: "headless: workspace routing is unconfigured; run wiki use project|main|both"
---

The toolboxmd-use-grok skill intentionally combines automatic host selection with unrestricted Grok execution, but only when the user explicitly asks to use Grok. The trigger boundary is carried by the portable `description`: the host should select the skill for requests that explicitly ask to ask, send, pass, delegate to, or consult Grok, and must not select it merely because Grok might be useful.

Automatic selection uses host defaults rather than a non-portable SKILL.md flag. OpenAI keeps `policy.allow_implicit_invocation: true` in `agents/openai.yaml`. Claude Code receives no `disable-model-invocation` field, so its documented default `false` for that disabling field applies and the model may invoke the skill. There is no portable `model-invocation: true` field. Omitting the Claude-specific field also keeps SKILL.md compatible with claude.ai and the Claude Skills API, whose upload schema rejects non-standard fields such as `disable-model-invocation` and `argument-hint`.

Unrestricted Grok permissions are an explicit product decision, not a missing safeguard. The default command uses `--always-approve`, leaves shell, web search, editing, MCP, memory, and subagents enabled, and does not add a sandbox or tool allowlist. The skill now says: `Unrestricted permissions are intentional: this skill delegates to Grok as a full agent.` Restrictions such as `--sandbox read-only`, `--no-subagents`, `--disable-web-search`, `--tools`, or `--disallowed-tools` are added only when the user asks to restrict Grok. Research and review briefs may tell Grok not to edit, but the runtime capability remains unrestricted by design.

The portable revision is commit `9096556259580a484661e5d08012974a444db687` on `main`, message `feat: modernize Grok delegation skill`. It removes the wrapper `scripts/consult-grok`, adds `agents/openai.yaml`, moves volatile Grok CLI 1.0.5 details into `references/grok-cli.md`, documents ChatGPT `@`, Codex `$`, and Claude Code `/` invocation, and narrows compatibility to environments with a local shell and `grok` executable. The focused contract suite passed 9 of 9.

Official sources checked 2026-08-21:
- https://developers.openai.com/codex/skills
- https://code.claude.com/docs/en/slash-commands
- https://agentskills.io/specification
