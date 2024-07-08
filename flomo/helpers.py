import datetime
import os
import platform

from playsound import playsound

import flomo.tracker as tracker


def get_path(file_name: str, in_data: bool = False):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    sign = "\\" if platform.system().lower() == "windows" else "/"
    data_folder = f"{sign}data" if in_data else ""

    if in_data and not os.path.exists(dir_path + data_folder):
        os.makedirs(dir_path + data_folder)

    file = f"{data_folder}{sign}{file_name}"

    return os.path.join(dir_path + file)


def play_sound():
    path = get_path("beep.mp3")

    if not platform.system().lower() in ["windows", "darwin"]:
        os.system(
            "notify-send 'Flomo' 'Time to start flowing!' -u normal && paplay " + path
        )
    else:
        playsound(path)


def message_log(message: str):
    path = get_path("message.log", True)

    with open(path, "a") as f:
        f.write(message + "\n")


def format_time(seconds: int) -> str:
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)

    return f"{hours:02}:{mins:02}:{secs:02}"


def end_session(session_id: float):
    db = tracker.Tracker()
    db.end_session(session_id, datetime.datetime.now())
    db.conn.close()
