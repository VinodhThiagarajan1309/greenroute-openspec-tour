## Why

A dispatcher reassigning a crew after a rain-out reassigns one booking at a time. A
washed-out Tuesday is 40 bookings, so the job takes twenty minutes during the exact
window when customers are calling.

## What Changes

- **ADDED** requirement: the schedule SHALL allow selecting many bookings and
  reassigning them in one action.
- **ADDED** requirement: a bulk reassignment SHALL be rejected whole when any booking
  in it would break the licence gate.

## Capabilities

### New Capabilities

- `crew-scheduling`: How a dispatcher moves bookings between crews, individually and
  in bulk.

### Modified Capabilities

- None.

## Impact

Affected code: the dispatcher schedule view.
