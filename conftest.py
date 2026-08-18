import pytest
from framework.config_manager import ConfigManager
from framework.api_client import APIClient
from framework.auth_manager import AuthManager

@pytest.fixture(scope="session")
def config():
    return ConfigManager()

@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(config)

@pytest.fixture(scope="session")
def auth_manager():
    return AuthManager()

@pytest.fixture
def auth_headers(auth_manager):
    return auth_manager.headers(auth_manager.get_token())
