---
title: "Installing a local skill as a personal Codex plugin"
evidence: "conversation"
evidence_type: "conversation"
capture_kind: "chat-only"
suggested_action: "create"
suggested_pages: []
attachments: []
captured_at: "2026-08-21T17-51-11Z"
captured_by: "in-session-agent"
capture_id: "cap-0386147da0394912a8aeeebb368512ca"
promotion_policy: "selective"
promotion_decision: "promoted"
promotion_id: "prom-e9ec0f4297de4e8bb1df8e5e"
propagated_from: null
---

Codex plugins can package one or more skills for installation through a marketplace. For a local personal plugin, the validated layout used here is a plugin root under ~/plugins/<plugin-name>, a required .codex-plugin/plugin.json manifest, and the skill package under skills/<skill-name>/SKILL.md. Skill-specific OpenAI metadata remains alongside the skill at skills/<skill-name>/agents/openai.yaml, while references stay under skills/<skill-name>/references/. This preserves the standalone skill package structure inside the plugin.

The personal marketplace lives at ~/.agents/plugins/marketplace.json. Its top-level name is personal, and the plugin entry uses a local source path relative to the marketplace directory. The plugin was installed with codex plugin add toolboxmd-use-grok@personal. Codex reported the plugin as installed and enabled at version 0.1.0 and cached the resolved package under ~/.codex/plugins/cache/personal/toolboxmd-use-grok/0.1.0. A new Codex session is needed for newly installed plugin skills to appear in session discovery.

The plugin manifest includes name, version, description, author, license, homepage, repository, keywords, skills path, and interface metadata. The interface identifies the plugin as Use Grok and explains that it delegates research, coding, and reviews to the local Grok Build CLI. The bundled skill keeps policy.allow_implicit_invocation set to true in agents/openai.yaml. This supports automatic host selection when the user explicitly asks to use or consult Grok. The skill itself preserves unrestricted Grok execution by design.

The plugin-creator validator initially failed before validating the plugin because its Python interpreter lacked the yaml module. Running the same validator through an isolated uv environment with PyYAML supplied resolved the tool dependency without modifying the system Python environment: uv run --with pyyaml python <validate_plugin.py> <plugin-root>. Validation then passed. This is a validator runtime dependency issue, not a manifest or plugin defect.

The source skill remains in the Git repository at /Users/lukaszmaj/dev/toolboxmd/toolboxmd-use-grok. The installed personal plugin is a packaged local copy under /Users/lukaszmaj/plugins/toolboxmd-use-grok. Source changes therefore require repackaging or updating the personal plugin before Codex sees them. The source revision used for the install was commit 9096556259580a484661e5d08012974a444db687 on main.

Sources and evidence checked 2026-08-21:
- https://learn.chatgpt.com/docs/plugins
- Codex CLI 0.149.0 output from codex plugin add and codex plugin list
- Local plugin validator from the installed plugin-creator skill
