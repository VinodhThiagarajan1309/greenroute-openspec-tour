## Context

See proposal.md. First capability in this repository, so it also sets the delta
conventions the rest of the repo follows.

## Goals / Non-Goals

**Goals:** one authority for what GreenRoute sells.

**Non-Goals:** pricing tiers and add-ons. Both are real and both are deferred; widening
this change to cover them would make the quarantine decision harder to review.

## Decisions

**Unknown service types quarantine rather than default.** The cheaper alternative is to
resolve an unknown type to its closest catalog match, which keeps the pipeline flowing.
Rejected: defaulting books revenue against the wrong service type and nobody notices
until finance asks why mulching tripled. A quarantined row is visible; a defaulted row
is a lie that reconciles.

## Risks / Trade-offs

Quarantine is only better than dropping if something reads the quarantine table. If its
row count is not monitored, this decision degrades into a slower silent drop.
