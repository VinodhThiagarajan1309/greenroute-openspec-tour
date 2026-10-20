## 1. Contract

- [x] 1.1 Contract agreed with finance, including the breaking-change call; verify by sign-off recorded on the PR

## 2. Pipeline

- [x] 2.1 Write the ledger at capture grain; verify `pytest tests/payments/test_ledger_grain.py`
- [x] 2.2 Attribute refunds to the capture, including late-settling refunds; verify the same tests

## 3. Backfill

- [x] 3.1 Partition-wise MERGE backfill, re-runnable; verify by re-running one partition and diffing to zero

## 4. Verification

- [x] 4.1 Per-partition parity on `sum(net_amount)` with every disagreement explained by the grain change; verify the parity report shows zero unexplained rows
