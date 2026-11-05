def test_ping_is_alive(session, base_url):
    """GET /ping is the health endpoint and must return 201 Created."""
    resp = session.get(f"{base_url}/ping")
    assert resp.status_code == 201
