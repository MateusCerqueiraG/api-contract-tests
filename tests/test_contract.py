from jsonschema import validate

from schemas.booking import BOOKING_SCHEMA, CREATE_RESPONSE_SCHEMA, BOOKING_IDS_SCHEMA


def test_create_response_matches_contract(session, base_url, token, sample_booking):
    resp = session.post(f"{base_url}/booking", json=sample_booking)
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=CREATE_RESPONSE_SCHEMA)
    session.delete(
        f"{base_url}/booking/{resp.json()['bookingid']}",
        headers={"Cookie": f"token={token}"},
    )


def test_single_booking_matches_contract(session, base_url, created_booking):
    booking_id, _ = created_booking
    resp = session.get(f"{base_url}/booking/{booking_id}")
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=BOOKING_SCHEMA)


def test_booking_list_matches_contract(session, base_url):
    resp = session.get(f"{base_url}/booking")
    assert resp.status_code == 200
    validate(instance=resp.json(), schema=BOOKING_IDS_SCHEMA)
