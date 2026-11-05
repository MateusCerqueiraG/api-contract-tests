def test_get_nonexistent_booking_returns_404(session, base_url):
    resp = session.get(f"{base_url}/booking/99999999")
    assert resp.status_code == 404


def test_create_with_incomplete_payload_is_rejected(session, base_url):
    """restful-booker rejects an incomplete body with 500 (no partial create)."""
    resp = session.post(f"{base_url}/booking", json={"firstname": "OnlyName"})
    assert resp.status_code == 500


def test_update_without_auth_is_forbidden(session, base_url, created_booking):
    booking_id, _ = created_booking
    resp = session.put(f"{base_url}/booking/{booking_id}", json={"firstname": "NoAuth"})
    assert resp.status_code == 403


def test_delete_without_auth_is_forbidden(session, base_url, created_booking):
    booking_id, _ = created_booking
    resp = session.delete(f"{base_url}/booking/{booking_id}")
    assert resp.status_code == 403
