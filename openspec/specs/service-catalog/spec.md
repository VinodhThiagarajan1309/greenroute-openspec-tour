# service-catalog Specification

## Purpose
What GreenRoute sells — service types, the constraints that attach to selling a given
service, and what happens to a booking that names something else.

## Requirements

### Requirement: Catalog: define exactly one active row per billable service

The catalog SHALL define exactly one active row per billable service type.

#### Scenario: Two active rows for the same service type

- **WHEN** a second row for `mowing-standard` is written with `active = true` while the first is still active
- **THEN** the write is rejected
- **AND** the error names `mowing-standard` and both row ids

#### Scenario: Superseding a service type

- **WHEN** `mowing-standard` is repriced by deactivating the old row and inserting a new active one
- **THEN** both writes succeed
- **AND** exactly one `mowing-standard` row has `active = true`

### Requirement: Booking referencing an unknown service type: be quarantined

A booking referencing an unknown service type SHALL be quarantined, not defaulted.

#### Scenario: Service type absent from the catalog

- **WHEN** a booking arrives with `service_type = "MOW_STD"` and the catalog holds no active row for it
- **THEN** the row is written to the quarantine table with reason `unknown_service_type`
- **AND** no row is written to `silver_booking_events`

#### Scenario: Unknown service type resembling an active one

- **WHEN** a booking arrives with `service_type = "mowing"` and the catalog's only active row is `mowing-standard`
- **THEN** the row is quarantined
- **AND** it is NOT resolved to `mowing-standard` by prefix or fuzzy match
