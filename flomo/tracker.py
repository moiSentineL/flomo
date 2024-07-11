import datetime
import sqlite3
import pandas
import tabulate

import flomo.helpers as helpers


class Tracker:
    def __init__(self):
        path = helpers.get_path("sessions.db", True)

        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sessions (id FLOAT PRIMARY KEY, tag TEXT, name TEXT, start_time TEXT, end_time TEXT, total_time TEXT)"
        )
        self.conn.commit()

    def create_session(
        self, tag: str, name: str, start_time: datetime.datetime
    ) -> float:
        session_id = start_time.timestamp()
        self.cursor.execute(
            "INSERT INTO sessions (id, tag, name, start_time) VALUES (?, ?, ?, ?)",
            (session_id, tag, name, start_time.strftime("%Y-%m-%d %H:%M:%S")),
        )
        self.conn.commit()
        return session_id

    def update_session(self, session_id: float, end_time: datetime.datetime):
        total_time = end_time - datetime.datetime.fromtimestamp(session_id)
        self.cursor.execute(
            "UPDATE sessions SET end_time = ?, total_time = ? WHERE id = ?",
            (
                end_time.strftime("%Y-%m-%d %H:%M:%S"),
                helpers.format_time(round(total_time.total_seconds())),
                session_id,
            ),
        )
        self.conn.commit()

    def get_sessions(self):
        self.cursor.execute("SELECT * FROM sessions")
        return self.cursor.fetchall()

    def get_session(self, session_id: float):
        self.cursor.execute("SELECT * FROM sessions WHERE id = ?", (session_id,))
        return self.cursor.fetchone()


def show_sessions():
    db = Tracker()
    sessions = db.get_sessions()
    db.conn.close()

    print(
        tabulate.tabulate(
            pandas.DataFrame(sessions),  # type: ignore
            headers=["ID", "Tag", "Name", "Start Time", "End Time", "Total Time"],
            tablefmt="psql",
            showindex=False,
        )
    )
