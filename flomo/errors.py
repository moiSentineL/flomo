class DBFileNotFoundError(Exception):
    def __init__(self):
        super().__init__("Database file does not exist. Please run `flomo init`.")


class NoConfigError(Exception):
    def __init__(self):
        super().__init__("No config file found. Please run `flomo init`.")


class InvalidConfigKeyError(Exception):
    def __init__(self, key: str):
        super().__init__(f"Invalid config key: {key}.")


class NoSessionsError(Exception):
    def __init__(self):
        super().__init__("No sessions were found.")


class NoSessionError(Exception):
    def __init__(self, session_id: str):
        super().__init__(f"No session with ID {session_id} was found.")
