# Versioning and release

`VERSION` is the canonical stable SemVer version. `.version-policy.json`
declares the three plugin manifests as mirrors. Use the shared AgentsMD
`versionctl` executable from PATH or the installed AgentsMD plugin's
`bin/versionctl`; do not copy its implementation into this repository.

For a completed change, run these commands from the repository root:

```sh
versionctl doctor --json
versionctl prepare patch --reason "Describe the completed change" --dry-run
versionctl prepare patch --reason "Describe the completed change"
bash tests/use-grok.test.sh
```

Choose `major` for incompatible behavior, `minor` for a backward-compatible
capability, and `patch` otherwise. Review and commit the change, `VERSION`, all
reported mirrors, and `CHANGELOG.md` together. On the clean exact commit, run
`versionctl release-check`. Only `versionctl` writes versions and mirrors.

The contract tests currently require the checkout directory to be named
`use-grok`. For differently named worktrees, test a copy of the complete
candidate under that basename, then verify the clean committed Git archive
under the same basename. These deterministic tests do not prove installation
or real Grok execution.

Release ownership remains with the coordinating human or an explicitly
authorized delivery agent. Releases are manual: after the reviewed candidate
is merged into `main`, re-run the tests and `versionctl release-check` at the
exact release commit, create the annotated `v{version}` tag at that commit,
and create the matching GitHub Release from its changelog entry. Never move
or reuse a version tag. The policy introduces no release workflow or hooks.

Distribution must use released tags. Marketplace promotion, publication,
installation, and live verification are separate authorized operations with
their own evidence; a release alone proves none of them. Existing installation
instructions remain in [README.md](../README.md).

## Shared delivery declarations

[The delivery profile](../.toolboxmd/delivery.json) declares the existing contract
suite for changed-scope and complete proof. Its release commands require a clean
checkout at the full commit substituted for `{sha}`. Run commands from the
repository root in their listed order, with the shared AgentsMD `versionctl`
executable on the proof subprocess's PATH. When using an installed plugin,
prepend that installation's `bin` directory for the subprocess only. The shared
`bin/delivery-profile load --root "$PROJECT_ROOT" --json` command validates the
profile; neither shared executable nor schema is copied here.

[The Project Record](../.toolboxmd/project.json) indexes the existing version,
host manifests, Skill, documentation, requirements, and proof owners. Its schema
and ingestion contract belong to Marketplace. Validate the record and referenced
files from the exact candidate tree using that shared contract before release.

The profile's public representation is this repository's existing GitHub README
at `https://github.com/toolboxmd/use-grok`. It introduces no separate product site
or artifact build. Source release, Marketplace pin, installation, loading, and
behavioral Live Verification require separate evidence.

## Existing release history

Adoption preserves the existing `0.2.0` baseline: `VERSION`, all three plugin
manifests, and annotated tag `v0.2.0` identify the release at commit
`a8ae6ab3c862de836ca576276a221610e3fe274c`. No GitHub Release existed when
this policy was adopted. The existing 0.2.0 changelog entry is preserved;
adoption neither invents a historical release nor retags that commit.
