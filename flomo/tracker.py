import sqlite3

import flomo.helpers as helpers


class Tracker:
    def __init__(self):
        path = helpers.get_path("sessions.db")

        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()

        self.conn.close()
