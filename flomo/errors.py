class DBFileNotFoundError(Exception):
    def __init__(self):
        super().__init__("Database file does not exist. Please run `flomo init`.")


class NoSessionsError(Exception):
    def __init__(self):
        super().__init__("No sessions were found.")


class NoSessionError(Exception):
    def __init__(self, session_id):
        super().__init__(f"No session with ID {session_id} was found.")
