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
        self.do_check = not initializing and not get_default_session_data

        if self.do_check and self._get_missing_keys() != []:
            raise errors.NoConfigError()

    def _config_file_exists(self):
        missing_keys = self._get_missing_keys()
        return os.path.exists(self.path), missing_keys

    def _get_missing_keys(self):
        if not os.path.exists(self.path):
            return ["default_session_data", "notification_priority", "tag_colors"]

        with open(self.path, "r") as f:
            data = json.load(f)
            missing_keys = []

            if (
                "default_session_data" not in data
                or data["default_session_data"].keys() != default_session_data.keys()
            ):
                missing_keys.append("default_session_data")

            if "notification_priority" not in data or data[
                "notification_priority"
            ].lower() not in ["off", "normal", "high"]:
                missing_keys.append("notification_priority")

            if "tag_colors" not in data:
                missing_keys.append("tag_colors")

            return missing_keys

    def create_config(self):
        file_exists, missing_keys = self._config_file_exists()
        if file_exists and missing_keys == []:
            return

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

        with open(self.path, "r+") as f:
            data = json.load(f)
            for missing_key in missing_keys:
                if missing_key == "default_session_data":
                    data[missing_key] = default_session_data
                if missing_key == "notification_priority":
                    data[missing_key] = "normal"
                if missing_key == "tag_colors":
                    data[missing_key] = tag_colors

            f.seek(0)
            json.dump(data, f, indent=4)

    def get_config(self, key: str):
        if key == "default_session_data" and not self._config_file_exists()[0]:
            return default_session_data

        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                return data[key]
        except KeyError:
            raise errors.InvalidConfigKeyError(key)


def get_default_session_data():
    try:
        conf = Config(get_default_session_data=True).get_config("default_session_data")
        return conf["tag"], conf["name"]
    except (errors.InvalidConfigKeyError, KeyError):
        return default_session_data["tag"], default_session_data["name"]
