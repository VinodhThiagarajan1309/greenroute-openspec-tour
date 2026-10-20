## MODIFIED Requirements

### Requirement: Booking referencing an unknown service type: be quarantined

A booking SHALL be quarantined when its service type is unknown, and when the service
type requires a licensed applicator and the assigned technician holds no active licence.

#### Scenario: Licensed service with an unlicensed technician

- **WHEN** a `pesticide-application` booking is assigned to a technician whose licence is expired
- **THEN** the row is quarantined with reason `unlicensed_applicator`
