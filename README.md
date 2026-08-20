# toolboxmd-use-grok

A bounded, explicit-only skill for asking the local Grok Build CLI for a second opinion.

## Status

- The skill runs only when the user explicitly asks for Grok.
- Repository mutation by Grok is outside the current scope.
- Automatic plan review is disabled and fails closed.
- The deterministic fake-CLI contract is tested locally.
- No current-version real CLI acceptance is claimed.

## Layout

- `SKILL.md`: activation and reconciliation instructions.
- `scripts/consult-grok`: provider adapter, isolation checks, redaction, and evidence output.
- `tests/toolboxmd-use-grok.test.py`: deterministic adapter contract.
- `tests/toolboxmd-use-grok.test.sh`: test entry point.

## Test

```bash
bash tests/toolboxmd-use-grok.test.sh
```

The test suite covers activation boundaries, structured output, environment isolation, secret redaction, incomplete results, timeouts, process-tree cleanup, numeric limits, and the disabled automatic mode.

## Use

Load `SKILL.md`, prepare a minimal prompt file, and run:

```bash
scripts/consult-grok \
  --mode explicit \
  --prompt-file "<brief-path>" \
  --output-dir "<evidence-dir>"
```

Grok's response is a proposal. Reconcile it with the task evidence before changing a plan.
