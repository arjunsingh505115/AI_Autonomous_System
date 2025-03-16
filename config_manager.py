import json
import os

class ConfigManager:
    CONFIG_FILE = "config.json"

    def __init__(self):
        if not os.path.exists(self.CONFIG_FILE):
            self._create_default_config()

    def _create_default_config(self):
        default_config = {
            "auto_upgrade": True,
            "error_scan_interval": 10,
            "api_endpoint": "https://api.example.com",
            "max_commands": 100
        }
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)

    def get_config(self):
        with open(self.CONFIG_FILE, "r") as f:
            return json.load(f)

    def update_config(self, key, value):
        config = self.get_config()
        if key in config:
            config[key] = value
            with open(self.CONFIG_FILE, "w") as f:
                json.dump(config, f, indent=4)
            print(f"✅ Configuration updated: {key} = {value}")
        else:
            print(f"⚠️ Invalid configuration key: {key}")
