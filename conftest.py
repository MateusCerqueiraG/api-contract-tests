import pytest
import requests

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json", "Accept": "application/json"})
    s.request = _with_timeout(s.request)
    return s


def _with_timeout(request, timeout=30):
    def wrapped(method, url, **kwargs):
        kwargs.setdefault("timeout", timeout)
        return request(method, url, **kwargs)
    return wrapped


@pytest.fixture(scope="session")
def token(session, base_url):
    resp = session.post(f"{base_url}/auth", json={"username": "admin", "password": "password123"})
    assert resp.status_code == 200, resp.text
    return resp.json()["token"]


@pytest.fixture
def sample_booking():
    return {
        "firstname": "Mateus",
        "lastname": "Cerqueira",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-10"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def created_booking(session, base_url, token, sample_booking):
    """Creates a booking and guarantees cleanup after the test."""
    resp = session.post(f"{base_url}/booking", json=sample_booking)
    assert resp.status_code == 200, resp.text
    booking_id = resp.json()["bookingid"]
    yield booking_id, sample_booking
    session.delete(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={token}"})
