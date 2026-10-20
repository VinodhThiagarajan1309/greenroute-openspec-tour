## MODIFIED Requirements

### Requirement: Booking referencing an unknown service type: be quarantined

A booking SHALL be quarantined when its service type is unknown, and when the service
type requires a licensed applicator and the assigned technician holds no active licence.

#### Scenario: Service type absent from the catalog

- **WHEN** a booking arrives with `service_type = "MOW_STD"` and the catalog holds no active row for it
- **THEN** the row is written to the quarantine table with reason `unknown_service_type`
- **AND** no row is written to `silver_booking_events`

#### Scenario: Unknown service type resembling an active one

- **WHEN** a booking arrives with `service_type = "mowing"` and the catalog's only active row is `mowing-standard`
- **THEN** the row is quarantined
- **AND** it is NOT resolved to `mowing-standard` by prefix or fuzzy match

#### Scenario: Licensed service with an unlicensed technician

- **WHEN** a `pesticide-application` booking is assigned to a technician whose licence is expired
- **THEN** the row is quarantined with reason `unlicensed_applicator`
- **AND** the booking is NOT reassigned automatically
