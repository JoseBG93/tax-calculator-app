def test_allowed_origin_receives_cors_headers(client, allowed_origin):
    response = client.get("/index", headers={"Origin": allowed_origin})
    assert response.headers.get("Access-Control-Allow-Origin") == allowed_origin


def test_disallowed_origin_does_not_receive_cors_headers(client):
    response = client.get(
        "/index", headers={"Origin": "http://malicious.test"}
    )
    assert "Access-Control-Allow-Origin" not in response.headers
