import json
import os

import flomo.errors as errors
import flomo.helpers as helpers

default_session_data = {
    "tag": "Work",
    "name": "Working",
}

tag_colors = {"Work": "red", "Study": "blue", "Exercise": "green"}


class Config:
    def __init__(
        self, initializing: bool = False, get_default_session_data: bool = False
    ):
        self.path = helpers.get_path("config.json", in_data=True)

        if (
            not initializing
            and not get_default_session_data
            and not self._config_data_check()
        ):
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
                "default_session_data": default_session_data,
                "notification_priority": "normal",
                "tag_colors": tag_colors,
            }

            json.dump(data, f, indent=4)

    def get_config(self, key: str):
        if key == "default_session_data" and not self._config_file_exists():
            return default_session_data

        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                return data[key]
        except KeyError:
            raise errors.InvalidConfigKeyError(key)
