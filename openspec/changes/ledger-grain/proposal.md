## Why

`gold_payment_ledger` has no agreed grain. Finance reads one row per capture; the
refunds job writes one row per booking. Both are "the ledger", and they disagree by
about 2% in any month with refund activity.

## What Changes

- **ADDED** requirement: the ledger SHALL hold exactly one row per
  `(booking_id, capture_id, settlement_date)`.
- **ADDED** requirement: refund activity SHALL be aggregated onto the capture it
  reverses, never onto the booking.

## Capabilities

### New Capabilities

- `payment-ledger`: The gold table finance reads — its grain, and how refunds are
  attributed to the capture they reverse.

### Modified Capabilities

- None.

## Tables touched

| table | read | written | breaking |
|---|---|---|---|
| `silver_payment_events` | yes | no | no |
| `gold_payment_ledger` | no | yes | **yes** |

## Impact

Affected code: `src/greenroute/payments/`, and every downstream finance query.
