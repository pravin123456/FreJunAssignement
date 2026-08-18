import pytest
from framework.response_handler import assert_status

@pytest.mark.regression
def test_create_user(api_client, auth_headers):
    payload = {"name": "Automation User", "email": "automation@example.com"}
    response = api_client.post("/users", payload, headers=auth_headers)
    assert_status(response, 201)
    body = response.json()
    assert body["name"] == payload["name"]

@pytest.mark.regression
@pytest.mark.parametrize("user_id, expected_status", [(1, 200), (999999, 404)])
def test_get_user(api_client, auth_headers, user_id, expected_status):
    response = api_client.get(f"/users/{user_id}", headers=auth_headers)
    assert_status(response, expected_status)
