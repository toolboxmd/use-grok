# Objective

Make use-grok a reliably installable and maintainable delegation capability
across its supported local agent hosts, so a fresh installation can carry an
explicit request through Grok execution and return a verifiable result without
configuration drift, lost work, or ambiguous completion.

The Objective is complete when:

- Supported hosts discover the same versioned Skill through their documented
  installation paths, with source, package, and distribution identity aligned.
- The Skill clearly binds a delegated request to its workspace, scope, granted
  permissions, and completion evidence while keeping final judgment and
  protected external actions with the coordinator.
- Current invocation and continuation behavior is source-verified, and the
  agreed policy for evolving CLI interfaces prevents stale guidance from
  silently changing a task's meaning or losing session history.
- Deterministic tests cover packaging and the maintained workflow contracts,
  while real-path verification remains distinct from those tests.
- The Project owns coherent direction, canonical versioning, release and
  documentation references, and a small delivery profile that reuses the
  shared Delivery System without duplicating its control plane.

Building a Grok wrapper, changing Grok's product behavior, choosing a global
model default, and replacing the host agent's authority model are outside this
Objective.
