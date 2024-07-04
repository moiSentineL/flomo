import os
import platform

from playsound import playsound


def get_path(file_name: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = (
        f"\\{file_name}" if platform.system().lower() == "windows" else f"/{file_name}"
    )
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
    path = get_path("message.log")

    with open(path, "a") as f:
        f.write(message + "\n")


def format_time(seconds: int) -> str:
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"
