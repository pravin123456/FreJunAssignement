import os

class AuthManager:
    def get_token(self):
        return os.getenv("API_TOKEN")

    def headers(self, token=None, tenant_id=None):
        headers = {"Accept": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        if tenant_id:
            headers["X-Tenant-ID"] = tenant_id
        return headers
