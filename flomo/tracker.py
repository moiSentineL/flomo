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
            "CREATE TABLE IF NOT EXISTS sessions (id FLOAT PRIMARY KEY, date_time TEXT, tag TEXT, name TEXT, total_time TEXT)"
        )
        self.conn.commit()

    def create_session(
        self, tag: str, name: str, start_time: datetime.datetime
    ) -> float:
        session_id = start_time.timestamp() % 1000000
        self.cursor.execute(
            "INSERT INTO sessions (id, date_time, tag, name) VALUES (?, ?, ?, ?)",
            (session_id, start_time.strftime("%Y-%m-%d %H:%M:%S"), tag, name),
        )
        self.conn.commit()
        return session_id

    def update_session(self, session_id: float, end_time: datetime.datetime):
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
            headers=["ID", "Session Date & Time", "Tag", "Name", "Total Time"],
            tablefmt="psql",
            showindex=False,
        )
    )
