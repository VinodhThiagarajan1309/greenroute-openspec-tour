## 1. Specification

- [x] 1.1 Proposal agreed in review
- [x] 1.2 ADDED requirement: one active row per service type; verify `openspec validate catalog-service-types --strict`
- [x] 1.3 ADDED requirement: unknown type quarantined; same verification

## 2. Implementation

- [x] 2.1 Catalog lookup with a uniqueness constraint on (service_type, active); verify `pytest tests/service_catalog`
- [x] 2.2 Quarantine path for unresolved service types; verify the same tests

## 3. Verification

- [x] 3.1 One test per scenario — 4 scenarios, 4 tests; verify `pytest`
- [x] 3.2 CI green: `openspec validate --all --strict`
