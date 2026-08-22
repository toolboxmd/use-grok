---
title: "use-grok ToolboxMD plugin identity and repository migration"
evidence: "/Users/lukaszmaj/dev/toolboxmd/use-grok/.codex-plugin/plugin.json"
evidence_type: "mixed"
capture_kind: "chat-attached"
suggested_action: "augment"
suggested_pages: []
attachments: []
captured_at: "2026-08-21T18-09-41Z"
captured_by: "in-session-agent"
capture_id: "cap-703f257c86ca462fb2d3173f4d130783"
promotion_policy: "selective"
promotion_decision: "promoted"
promotion_id: "prom-67555011806fa34439cf5b32"
propagated_from: null
---

The Grok delegation project was migrated from the redundant toolboxmd-use-grok identity to use-grok under the ToolboxMD publisher namespace. The local checkout moved from /Users/lukaszmaj/dev/toolboxmd/toolboxmd-use-grok to /Users/lukaszmaj/dev/toolboxmd/use-grok. The public GitHub repository was renamed from https://github.com/toolboxmd/toolboxmd-use-grok to https://github.com/toolboxmd/use-grok, and the local origin remote now uses the new URL.

The repository is now a Codex plugin root. Its manifest is .codex-plugin/plugin.json with plugin name use-grok, version 0.1.0, developerName toolbox.md, category Developer Tools, and skills path ./skills/. The portable skill moved to skills/use-grok/SKILL.md and its frontmatter name changed to use-grok. OpenAI-specific metadata moved with it to skills/use-grok/agents/openai.yaml and still has policy.allow_implicit_invocation set to true. Grok's unrestricted permission policy remains intentional. Explicit invocations are now $use-grok for Codex and /use-grok for Claude Code or Grok.

The shared local ToolboxMD marketplace moved to /Users/lukaszmaj/dev/toolboxmd/.agents/plugins/marketplace.json. Its marketplace name is toolboxmd, display name toolbox.md, and it exposes both ./karpathy-wiki and ./use-grok. Codex now resolves the marketplace root as /Users/lukaszmaj/dev/toolboxmd. Both karpathy-wiki@toolboxmd 0.3.2 and use-grok@toolboxmd 0.1.0 are installed and enabled. The obsolete toolboxmd-use-grok@personal installation was removed. Its personal package and one-entry personal marketplace manifest were archived to Trash rather than deleted permanently.

Source conversion commit 3fc4615af127bd07155de1b16cc137b56e5d4059, message feat: package use-grok plugin, was pushed to toolboxmd/use-grok main. The previous portable-skill revision 9096556259580a484661e5d08012974a444db687 was pushed with it. Local and remote main both resolved to 3fc4615af127bd07155de1b16cc137b56e5d4059 after the push.

Renaming the directory invalidated the path-keyed Karpathy Wiki routing and trusted runtime records. The workspace was reconfigured in both mode at the new path. A new trusted runtime was initialized for the existing project wiki with scheduled dispatch, Grok provider, grok-4.6 model, medium reasoning effort, one process, and auto-commit. The old path-keyed wiki and workspace runtime directories were archived to Trash. Final scheduler status reported zero invalid wikis, eight registered wikis, seven scheduled wikis, and no stalled or failed captures. Pending captures remain queued until the provider cooldown ends.

Validation note: the Codex plugin validator passed the new repository. The bundled quick skill validator rejected the standard compatibility frontmatter key even though current portable Agent Skills guidance permits it, so compatibility was intentionally retained and the stale validator result was treated as a tool-schema mismatch rather than changing the portable skill.
