import datetime
import sqlite3
from typing import Tuple

import pandas
import tabulate

import flomo.errors as errors
import flomo.helpers as helpers


class Tracker:
    def __init__(self, initializing: bool = False):
        path = helpers.get_path("sessions.db", in_data=True)

        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

        if not initializing and not self._db_file_exists():
            raise errors.DBFileNotFoundError()

    def _db_file_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return bool(self.cursor.fetchall())

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sessions (id FLOAT PRIMARY KEY, date_time TEXT, tag TEXT, name TEXT, total_time TEXT)"
        )
        self.conn.commit()

    def create_session(self, tag: str, name: str, start_time: datetime.datetime) -> int:
        session_id = int(start_time.timestamp() % 1000000)
        self.cursor.execute(
            "INSERT INTO sessions (id, date_time, tag, name) VALUES (?, ?, ?, ?)",
            (session_id, start_time.strftime("%Y-%m-%d %H:%M:%S"), tag, name),
        )
        self.conn.commit()
        return session_id

    def end_session(self, session_id: int, end_time: datetime.datetime):
        date_time = self.get_session(session_id)[1]
        total_time = end_time - datetime.datetime.strptime(
            date_time, "%Y-%m-%d %H:%M:%S"
        )
        self.cursor.execute(
            "UPDATE sessions SET total_time = ? WHERE id = ?",
            (
                helpers.format_time(round(total_time.total_seconds())),
                session_id,
            ),
        )
        self.conn.commit()

    def get_sessions(self):
        self.cursor.execute("SELECT * FROM sessions")
        return self.cursor.fetchall()

    def get_session(self, session_id: int):
        self.cursor.execute("SELECT * FROM sessions WHERE id = ?", (session_id,))
        return self.cursor.fetchone()

    def delete_session(self, session_ids: Tuple[str]):
        for session_id in session_ids:
            session_id = int(session_id)
            if not self.get_session(session_id):
                raise errors.NoSessionError(session_id)

        self.cursor.execute(
            "DELETE FROM sessions WHERE id IN ({seq})".format(
                seq=",".join(["?"] * len(session_ids))
            ),
            session_ids,
        )
        self.conn.commit()

    def update_session(self, session_id: int, tag: str | None, name: str | None):
        if not self.get_session(session_id):
            raise errors.NoSessionError(session_id)

        if tag:
            self.cursor.execute(
                "UPDATE sessions SET tag = ? WHERE id = ?", (tag.lower(), session_id)
            )
            print(f'Tag updated to "{tag.lower()}" for session {session_id}')
        if name:
            self.cursor.execute(
                "UPDATE sessions SET name = ? WHERE id = ?", (name, session_id)
            )
            print(f'Name updated to "{name}" for session {session_id}')
        self.conn.commit()


def end_session(session_id: int):
    db = Tracker()
    db.end_session(session_id, datetime.datetime.now())
    db.conn.close()


def show_sessions():
    # TODO: Use a proper UI to show the sessions
    db = Tracker()
    sessions = db.get_sessions()
    db.conn.close()

    print(
        tabulate.tabulate(
            pandas.DataFrame(sessions),  # type: ignore
            headers=["ID", "Session Date & Time", "Tag", "Name", "Total Time"],
            tablefmt="psql",
            showindex=False,
        )
    )
