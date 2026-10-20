## Table: gold_payment_ledger

**Grain:** one row per `(booking_id, capture_id, settlement_date)`
**Partitioned on:** `settlement_date`
**Freshness:** published by 06:00 CT for the previous settlement day
**Breaking for existing consumers:** **yes** — the refunds job currently writes one row
per booking; those rows disappear and are replaced by capture-level rows.

| column | type | nullable | notes |
|---|---|---|---|
| `booking_id` | string | no | |
| `capture_id` | string | no | part of the grain |
| `settlement_date` | date | no | partition column |
| `captured_amount` | decimal(12,2) | no | |
| `refunded_amount` | decimal(12,2) | no | aggregated onto the capture, defaults to 0 |
| `net_amount` | decimal(12,2) | no | `captured_amount - refunded_amount` |
