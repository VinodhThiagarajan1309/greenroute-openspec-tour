## Why

Service types are implied by strings in the booking payload. `"mow"`, `"mowing"` and
`"MOW_STD"` all appear in the last 90 days of data. Nothing downstream can price,
schedule or report reliably on that, and every team has built its own mapping.

## What Changes

- **ADDED** requirement: the catalog SHALL define exactly one active row per billable
  service type.
- **ADDED** requirement: a booking referencing an unknown service type SHALL be
  quarantined, not defaulted.

## Capabilities

### New Capabilities

- `service-catalog`: What GreenRoute sells — service types, the constraints that attach
  to selling a given service, and what happens to a booking that names something else.

### Modified Capabilities

- None.

## Impact

Affected code: `src/greenroute/service_catalog/`, `tests/service_catalog/`.
