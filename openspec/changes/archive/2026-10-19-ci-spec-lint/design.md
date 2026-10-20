## Context

Tooling only.

## Decisions

**Pin the OpenSpec version in CI.** The alternative is tracking latest and finding out
during an unrelated pull request. A pinned version makes a validator upgrade its own
change, reviewed on its own merits.

## Risks / Trade-offs

A pinned version goes stale. The upgrade becomes a deliberate change rather than a
surprise, which is the point.
