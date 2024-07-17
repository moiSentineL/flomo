import json
import os

import flomo.errors as errors
import flomo.helpers as helpers


class Config:
    def __init__(self, initializing: bool = False):
        self.path = helpers.get_path("config.json", in_data=True)

        if not initializing and not self._config_file_exists():
            raise errors.NoConfigError()

    def _config_file_exists(self):
        return os.path.exists(self.path) and self._config_data_check()

    def _config_data_check(self):
        with open(self.path, "r") as f:
            data = json.load(f)

            return all(
                key in data
                for key in [
                    "default_session_data",
                    "notification_priority",
                    "tag_colors",
                ]
            ) and data["notification_priority"].lower() in ["off", "normal", "high"]

    def create_config(self):
        if self._config_file_exists():
            return

        with open(self.path, "w") as f:
            data = {
                "default_session_data": {
                    "tag": "Work",
                    "name": "Working",
                },
                "notification_priority": "normal",
                "tag_colors": {"Work": "blue", "Study": "red", "Exercise": "green"},
            }

            json.dump(data, f, indent=4)

    def get_config(self, key: str):
        with open(self.path, "r") as f:
            data = json.load(f)
            return data[key]
