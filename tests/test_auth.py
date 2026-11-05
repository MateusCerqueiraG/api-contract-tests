def test_auth_returns_token(session, base_url):
    resp = session.post(f"{base_url}/auth", json={"username": "admin", "password": "password123"})
    assert resp.status_code == 200
    body = resp.json()
    assert "token" in body
    assert isinstance(body["token"], str) and body["token"]


def test_auth_with_wrong_credentials_has_no_token(session, base_url):
    resp = session.post(f"{base_url}/auth", json={"username": "admin", "password": "wrong"})
    assert resp.status_code == 200
    assert resp.json().get("reason") == "Bad credentials"
