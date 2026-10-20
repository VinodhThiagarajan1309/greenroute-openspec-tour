import pytest
from greenroute.service_catalog.catalog import (
    CatalogError, assert_one_active_row, resolve_service_type,
)

ROWS = [
    {"row_id": "r1", "service_type": "mowing-standard", "active": True},
    {"row_id": "r2", "service_type": "mowing-standard", "active": False},
]


def test_two_active_rows_for_the_same_service_type_is_rejected():
    rows = ROWS + [{"row_id": "r3", "service_type": "mowing-standard", "active": True}]
    with pytest.raises(CatalogError) as e:
        assert_one_active_row(rows, "mowing-standard")
    assert "r1" in str(e.value) and "r3" in str(e.value)


def test_superseding_a_service_type_leaves_exactly_one_active():
    assert assert_one_active_row(ROWS, "mowing-standard")["row_id"] == "r1"


def test_service_type_absent_from_the_catalog_is_quarantined():
    row, reason = resolve_service_type({"service_type": "MOW_STD"}, ROWS)
    assert row is None and reason == "unknown_service_type"


def test_unknown_type_resembling_an_active_one_is_not_fuzzy_matched():
    row, reason = resolve_service_type({"service_type": "mowing"}, ROWS)
    assert row is None and reason == "unknown_service_type"
