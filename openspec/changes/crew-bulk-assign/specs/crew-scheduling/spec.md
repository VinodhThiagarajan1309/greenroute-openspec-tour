## Purpose

How a dispatcher moves bookings between crews, one at a time and in bulk, including
what happens when part of a bulk move is not allowed.

## ADDED Requirements

### Requirement: Schedule: allow selecting many bookings and reassigning in one action

The schedule SHALL allow selecting many bookings and reassigning them in one action.

#### Scenario: Twelve bookings moved to another crew

- **WHEN** a dispatcher selects 12 bookings and chooses Crew B
- **THEN** all 12 show Crew B after one confirmation
- **AND** the dispatcher is not asked to confirm each one

#### Scenario: Selection survives a crew filter change

- **WHEN** 12 bookings are selected and the dispatcher filters the view to Crew A
- **THEN** the selection is unchanged and the action bar still reads 12

#### Scenario: Selection is cleared by a date change

- **WHEN** 12 bookings are selected and the dispatcher moves to the next day
- **THEN** the selection is empty
- **AND** no bookings from the previous day remain selected

### Requirement: Bulk reassignment: be rejected whole when any booking breaks the licence gate

A bulk reassignment SHALL be rejected whole when any booking in it would break the
licence gate.

#### Scenario: One pesticide booking in a batch of twelve

- **WHEN** 11 mowing bookings and 1 `pesticide-application` booking are moved to a crew with no licensed applicator
- **THEN** none of the 12 are moved
- **AND** the error names the one offending booking and the reason

#### Scenario: The same batch after the offending booking is deselected

- **WHEN** the dispatcher deselects the pesticide booking and retries
- **THEN** the remaining 11 move
