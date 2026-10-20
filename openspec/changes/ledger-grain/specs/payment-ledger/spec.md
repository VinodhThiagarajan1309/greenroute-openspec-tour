## Purpose

The gold table finance reads — its grain, and how refund activity is attributed to the
capture it reverses rather than to the booking.

## ADDED Requirements

### Requirement: Ledger: hold exactly one row per booking, capture and settlement date

The ledger SHALL hold exactly one row per `(booking_id, capture_id, settlement_date)`.

#### Scenario: Two captures against one booking

- **WHEN** booking `bk_1043` has captures `cap_3301` and `cap_3302` settling on `2026-04-02`
- **THEN** `gold_payment_ledger` holds two rows for `bk_1043` on that date
- **AND** neither row aggregates the other's amount

#### Scenario: One capture re-delivered by the processor

- **WHEN** the settlement feed delivers `cap_3301` twice for `2026-04-02`
- **THEN** `gold_payment_ledger` holds exactly one row for that key
- **AND** `captured_amount` is not doubled

### Requirement: Refund activity: be aggregated onto the capture it reverses

Refund activity SHALL be aggregated onto the capture it reverses, never onto the booking.

#### Scenario: Partial refund against one of two captures

- **WHEN** `cap_3301` is refunded 40.00 and `cap_3302` is untouched
- **THEN** the `cap_3301` row shows `refunded_amount = 40.00`
- **AND** the `cap_3302` row shows `refunded_amount = 0.00`

#### Scenario: Refund arriving in a later settlement window

- **WHEN** a refund for `cap_3301` settles on `2026-04-09`, a week after the capture
- **THEN** the refund is attributed to the `2026-04-02` capture row
- **AND** no new row is created in the `2026-04-09` partition for it
