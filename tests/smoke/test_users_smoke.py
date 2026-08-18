import pytest
from framework.response_handler import assert_status

@pytest.mark.smoke
def test_get_user(api_client, auth_headers):
    response = api_client.get("/users/1", headers=auth_headers)
    assert_status(response, 200)

@pytest.mark.smoke
def test_list_users(api_client, auth_headers):
    response = api_client.get("/users", headers=auth_headers)
    assert_status(response, 200)
    assert isinstance(response.json(), list)
