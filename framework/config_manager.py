import os
from pathlib import Path
import yaml

class ConfigManager:
    def __init__(self, environment=None):
        self.environment = environment or os.getenv("TEST_ENV", "qa")
        path = Path(__file__).parent.parent / "config" / f"{self.environment}.yaml"
        if not path.exists():
            raise FileNotFoundError(path)
        self.config = yaml.safe_load(path.read_text()) or {}
        self.base_url = os.getenv("BASE_URL", self.config.get("base_url")).rstrip("/")
        self.timeout = int(os.getenv("API_TIMEOUT", self.config.get("timeout", 30)))
        self.verify_ssl = str(os.getenv("VERIFY_SSL", self.config.get("verify_ssl", True))).lower() == "true"
