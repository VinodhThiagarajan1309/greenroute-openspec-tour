## Why

Nothing enforces the specs. A delta that drops a scenario, or an archived change with
unticked boxes, would reach main unnoticed — which makes the whole method advisory.

## What Changes

- Adds a CI workflow running `openspec validate --all --strict` and
  `openspec validate --archived` on every pull request.
- Pins the CLI version. 1.14.3 introduced strict rules that did not exist in 1.12.0;
  an unpinned upgrade can turn a green repository red with no change to its content.
- No behaviour changes, so this change carries no delta.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- None.

## Impact

`.github/workflows/ci.yml`.
