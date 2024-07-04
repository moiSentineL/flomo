import sqlite3

import flomo.helpers as helpers


class Tracker:
    def __init__(self):
        path = helpers.get_path("sessions.db")

        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS sessions (tag TEXT, name TEXT, start_time TEXT, end_time TEXT, total_time TEXT)"
        )
        self.conn.commit()

    def insert_session(self, tag: str, name: str, start_time: str, end_time: str, total_time: str):
        self.cursor.execute(
            "INSERT INTO sessions (tag, name, start_time, end_time, total_time) VALUES (?, ?, ?, ?, ?)",
            (tag, name, start_time, end_time, total_time),
        )
        self.conn.commit()

    def get_sessions(self):
        self.cursor.execute("SELECT * FROM sessions")
        return self.cursor.fetchall()


if __name__ == "__main__":
    tracker = Tracker()
    tracker.create_table()

    tracker.insert_session("study", "work", "10:00", "11:00", "1:00")
    tracker.insert_session("code", "work", "10:00", "11:00", "1:00")
    tracker.insert_session("music", "work", "10:00", "11:00", "1:00")

    print(tracker.get_sessions())

    tracker.conn.close()
