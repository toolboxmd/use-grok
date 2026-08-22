---
title: "ToolboxMD marketplace and use-grok naming convention"
evidence: "conversation"
evidence_type: "conversation"
capture_kind: "chat-only"
suggested_action: "augment"
suggested_pages: []
attachments: []
captured_at: "2026-08-21T18-00-05Z"
captured_by: "in-session-agent"
capture_id: "cap-fdf9b7eae8fa4f46b9323ecd3208ee4a"
promotion_policy: "selective"
promotion_decision: "promoted"
promotion_id: "prom-7f8ebe5be2c1774f446acc15"
propagated_from: null
---

The Grok delegation plugin should use the ToolboxMD marketplace umbrella rather than the personal marketplace used for the first local installation. The first installation as toolboxmd-use-grok@personal was technically valid for local testing, but it did not match the established ToolboxMD distribution convention.

The live local reference is the karpathy-wiki project at /Users/lukaszmaj/dev/toolboxmd/karpathy-wiki. Its marketplace manifest is .agents/plugins/marketplace.json with top-level name toolboxmd and interface displayName toolbox.md. Its plugin manifest identifies the plugin as karpathy-wiki, so Codex shows the installed identity as karpathy-wiki@toolboxmd. The Grok plugin should analogously use the stable installed identity use-grok@toolboxmd. The publisher namespace belongs in the marketplace suffix and developer metadata, so repeating toolboxmd inside the plugin name creates a redundant toolboxmd-use-grok@toolboxmd identifier.

The bundled skill should also be renamed from toolboxmd-use-grok to use-grok. The SKILL.md frontmatter name and its containing directory must match. This produces the shorter explicit invocations $use-grok in Codex and /use-grok in Claude Code while leaving natural-language automatic selection intact. The GitHub repository name is technically independent of both the plugin identifier and the skill name. It can remain toolboxmd-use-grok, although renaming the repository to use-grok would make the repository, plugin, and skill identities consistent under the github.com/toolboxmd organization namespace.

OpenAI's current plugin packaging documentation distinguishes repo and personal marketplaces. A marketplace can contain multiple plugins under one top-level marketplace name, and one marketplace is intended to grow into a curated catalog. Repo marketplaces live at $REPO_ROOT/.agents/plugins/marketplace.json. Each local source.path should be relative to the marketplace root, begin with ./, and stay inside that root. Therefore a robust multi-plugin ToolboxMD umbrella should eventually use a dedicated ToolboxMD marketplace repository or a monorepo that contains both plugin packages. Making karpathy-wiki's repository permanently own a sibling plugin through an outside-root path would violate the documented path guidance and make remote distribution brittle.

For an immediate local correction using the currently configured ToolboxMD marketplace root, a packaged use-grok directory can be placed inside /Users/lukaszmaj/dev/toolboxmd/karpathy-wiki, added to that marketplace's plugins array, installed as use-grok@toolboxmd, and the obsolete toolboxmd-use-grok@personal installation removed. This is a migration of installed identity, not merely a cosmetic rename, so the old plugin should be uninstalled only after the replacement validates and installs successfully.

Sources checked 2026-08-21:
- https://developers.openai.com/plugins/build/plugins
- https://learn.chatgpt.com/docs/plugins
- /Users/lukaszmaj/dev/toolboxmd/karpathy-wiki/.agents/plugins/marketplace.json
- /Users/lukaszmaj/dev/toolboxmd/karpathy-wiki/.codex-plugin/plugin.json
- Local Codex CLI marketplace and plugin listings
