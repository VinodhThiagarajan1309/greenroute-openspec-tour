## Scope

`2026-01-01` through the day before cutover. 2.8M capture rows across 4 months.

## Method

Recompute each `settlement_date` partition from `silver_payment_events` and MERGE on
`(booking_id, capture_id, settlement_date)`. Idempotent: a re-run of the same partition
produces the same rows, so a partial failure is re-runnable without cleanup.

## Verification

Parity against the existing ledger per partition on `sum(net_amount)`. Expected to
disagree only where booking-grain rows collapsed into capture-grain rows; every
disagreement must be explained by that, and the count of unexplained rows must be zero.
A row count alone does not pass this check — the grain change makes the counts differ
by design.

## Rollback

The previous ledger is retained as `gold_payment_ledger_pre_grain` until two consecutive
clean month-end closes. Rollback is a rename.
