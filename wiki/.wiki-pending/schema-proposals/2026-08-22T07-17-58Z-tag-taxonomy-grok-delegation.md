---
title: "Schema proposal: add Grok delegation tags"
captured_at: "2026-08-22T07:17:58Z"
trigger: "wiki-lint-tags.py reported new tags on concepts/unrestricted-grok-delegation.md"
---

`schema.md` Tag Taxonomy is still empty (a prior proposal covers the frontmatter page tags). This ingest introduced additional tags, new relative to the rest of the wiki:

- `grok-cli`
- `always-approve`
- `permissions`
- `use-grok`

Recommended: add them under Tag Taxonomy in `schema.md` if skill-runtime pages should share a bounded set with the packaging tags. Do not rename them inline on the page; this proposal is for a later schema edit.
