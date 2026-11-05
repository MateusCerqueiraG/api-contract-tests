def test_full_booking_lifecycle(session, base_url, token, sample_booking):
    """Create -> read -> full update -> partial update -> delete -> confirm gone."""
    auth = {"Cookie": f"token={token}"}

    # CREATE
    resp = session.post(f"{base_url}/booking", json=sample_booking)
    assert resp.status_code == 200, resp.text
    booking_id = resp.json()["bookingid"]

    try:
        # READ
        resp = session.get(f"{base_url}/booking/{booking_id}")
        assert resp.status_code == 200
        assert resp.json()["firstname"] == "Mateus"

        # FULL UPDATE (PUT)
        updated = {**sample_booking, "firstname": "Mat", "totalprice": 200}
        resp = session.put(f"{base_url}/booking/{booking_id}", json=updated, headers=auth)
        assert resp.status_code == 200
        assert resp.json()["firstname"] == "Mat"
        assert resp.json()["totalprice"] == 200

        # PARTIAL UPDATE (PATCH)
        resp = session.patch(f"{base_url}/booking/{booking_id}", json={"lastname": "Gonzaga"}, headers=auth)
        assert resp.status_code == 200
        assert resp.json()["lastname"] == "Gonzaga"
    finally:
        # DELETE
        resp = session.delete(f"{base_url}/booking/{booking_id}", headers=auth)
        assert resp.status_code == 201

    # CONFIRM GONE
    resp = session.get(f"{base_url}/booking/{booking_id}")
    assert resp.status_code == 404


def test_list_bookings_returns_ids(session, base_url):
    resp = session.get(f"{base_url}/booking")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
