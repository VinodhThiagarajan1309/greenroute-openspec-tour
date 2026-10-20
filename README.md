# greenroute-openspec-tour

Every OpenSpec CLI command, run for real, in one small repository — plus three
**custom workflow schemas** showing that the artifact set is not fixed.

Companion to [`greenroute-pipeline`](https://github.com/VinodhThiagarajan1309/greenroute-pipeline),
which shows the *practice* over four simulated months. This repo shows the *tool*.
Same world (GreenRoute, a lawn-care company in Austin). No personas here — the only
thing being demonstrated is how each artifact evolves.

## Read it as a git log

Each change is one merge commit. Three changes, chosen to cover the cases rather
than to tell a story:

| Change | Shape | Covers |
|---|---|---|
| `catalog-service-types` | `ADDED`, new capability | The full loop, first archive, `## Purpose` creation |
| `catalog-license-flag` | `MODIFIED` | The dropped-scenario refusal, then the fix |
| `ci-spec-lint` | zero-delta | The `skip_specs` escape hatch |

## Custom schemas

`openspec/schemas/` carries three workflows beyond the default. The `requires:`
graph in each `schema.yaml` **is** the gate, so the artifact set changes with the
kind of work:

| Schema | Chain | The artifact that only exists here |
|---|---|---|
| `data-change` | proposal → **contract** → specs → **backfill** → tasks | the published shape, agreed before behaviour |
| `ui-feature` | proposal → **interaction** → specs → **accessibility** → tasks | every state, enumerated before the spec |
| `spike` | hypothesis → experiment → findings → **decision** | no spec at all — the output is a decision |

Try them:

```bash
openspec schemas
openspec status --change ledger-grain        # data-change gate
openspec status --change crew-bulk-assign    # ui-feature gate
openspec status --change spike-duckdb-parity # spike gate
```

## Verified against

OpenSpec 1.14.3.

```bash
npm install -g @fission-ai/openspec
openspec validate --all --strict
openspec validate --archived
```
