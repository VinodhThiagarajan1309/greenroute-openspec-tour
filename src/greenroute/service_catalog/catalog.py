"""The service catalog: what GreenRoute sells.

Both requirements in the `service-catalog` capability are enforced here rather
than documented elsewhere, so a booking that breaks them cannot be published.
"""


class CatalogError(ValueError):
    """Raised when a write would break a catalog requirement."""


def assert_one_active_row(rows, service_type):
    """Exactly one active row per billable service type."""
    active = [r for r in rows if r["service_type"] == service_type and r["active"]]
    if len(active) > 1:
        raise CatalogError(
            "service type %r has %d active rows: %s"
            % (service_type, len(active), ", ".join(r["row_id"] for r in active))
        )
    return active[0] if active else None


def resolve_service_type(booking, rows):
    """Resolve a booking's service type, or say why it must be quarantined.

    Returns (resolved_row, None) or (None, quarantine_reason). Never guesses:
    an unrecognised type is quarantined rather than matched to the nearest
    catalog entry.
    """
    wanted = booking.get("service_type")
    match = assert_one_active_row(rows, wanted) if wanted else None
    if match is None:
        return None, "unknown_service_type"
    return match, None
