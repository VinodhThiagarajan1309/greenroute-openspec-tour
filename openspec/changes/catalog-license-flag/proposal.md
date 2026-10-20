## Why

Texas Department of Agriculture rules require a licensed applicator for commercial
pesticide application. Ops handles this today by assigning certain technicians by hand.
That works until the person who knows is on leave.

## What Changes

- **MODIFIED** requirement: a booking is quarantined when its service type is unknown,
  **and also** when the service requires a licensed applicator and none is assigned.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `service-catalog`: quarantine now covers the unlicensed-assignment case.

## Impact

Affected code: `src/greenroute/service_catalog/`.
