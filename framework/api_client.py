import requests
from .logger import get_logger

class APIClient:
    def __init__(self, config):
        self.base_url = config.base_url
        self.timeout = config.timeout
        self.verify_ssl = config.verify_ssl
        self.session = requests.Session()
        self.logger = get_logger()

    def _request(self, method, endpoint, **kwargs):
        url = endpoint if endpoint.startswith("http") else f"{self.base_url}{endpoint}"
        kwargs.setdefault("timeout", self.timeout)
        kwargs.setdefault("verify", self.verify_ssl)
        self.logger.info("%s %s", method.upper(), url)
        response = self.session.request(method, url, **kwargs)
        self.logger.info("Response=%s", response.status_code)
        return response

    def get(self, endpoint, headers=None, params=None):
        return self._request("GET", endpoint, headers=headers, params=params)

    def post(self, endpoint, payload=None, headers=None):
        return self._request("POST", endpoint, json=payload, headers=headers)

    def put(self, endpoint, payload=None, headers=None):
        return self._request("PUT", endpoint, json=payload, headers=headers)

    def patch(self, endpoint, payload=None, headers=None):
        return self._request("PATCH", endpoint, json=payload, headers=headers)

    def delete(self, endpoint, headers=None):
        return self._request("DELETE", endpoint, headers=headers)
