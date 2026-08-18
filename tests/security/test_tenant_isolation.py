import os
import pytest

@pytest.mark.security
def test_cross_tenant_access_is_denied(api_client, auth_manager):
    if os.getenv("ENABLE_TENANT_TESTS", "false").lower() != "true":
        pytest.skip("Enable against the real SaaS API")

    token = os.environ["TENANT_A_TOKEN"]
    resource_id = os.environ["TENANT_B_RESOURCE_ID"]
    tenant_a = os.environ["TENANT_A_ID"]
    headers = auth_manager.headers(token=token, tenant_id=tenant_a)
    response = api_client.get(f"/api/v1/users/{resource_id}", headers=headers)
    assert response.status_code in (403, 404), response.text
