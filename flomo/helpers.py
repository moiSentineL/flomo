import os
import platform

from playsound import playsound

import flomo.config as config
import flomo.errors as errors


def get_path(file_name: str, in_data: bool = False, lib: bool = False):
    is_windows = platform.system().lower() == "windows"
    is_mac = platform.system().lower() == "darwin"
    
    dir_path = os.path.dirname(os.path.realpath(__file__))

    sign = "\\" if is_windows else "/"
    data_folder = f"{sign}{'Flomo' if is_windows else 'flomo'}" if in_data else ""

    file = f"{data_folder}{sign}{file_name}"

    if in_data:
        conf_path = (
            str(os.getenv("APPDATA")) or str(os.getenv("LOCALAPPDATA"))
            if is_windows
            else (
                os.path.expanduser("~/Library/Application Support")
                if is_mac
                else os.path.expanduser("~/.config")
            )
        )
        if not os.path.exists(conf_path + data_folder):
            os.makedirs(conf_path + data_folder)
        return os.path.join(conf_path + file)
    elif lib:
        return (
            os.path.join(dir_path + f"{sign}session_id.dll")
            if is_windows
            else (
                os.path.join(dir_path + f"{sign}session_id.dylib")
                if is_mac
                else os.path.join(dir_path + f"{sign}session_id.so")
            )
        )
    else:
        return os.path.join(dir_path + file)

def play_sound():
    try:
        path = get_path("beep.mp3")
        conf = config.Config()

        notification_priority = str(conf.get_config(config.NOTIFICATION_PRIORITY))

        if notification_priority.lower() == "off":
            return

        if not platform.system().lower() in ["windows", "darwin"]:
            priority = (
                "critical" if notification_priority.lower() == "high" else "normal"
            )
            os.system(
                f"notify-send 'Flomo' 'Time to start flowing!' -u {priority} && paplay "
                + path
            )
        else:
            playsound(path)
    except errors.NoConfigError:
        pass  # Error is already getting logged from ui.py


def error_log(error: str):
    path = get_path("error.log", in_data=True)

    with open(path, "a") as f:
        f.write(error + "\n")


def format_time(seconds: int) -> str:
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)

    return f"{hours:02}:{mins:02}:{secs:02}"


def tag_color(tag: str) -> str:
    tag = tag.split("#")[1].lower() if "#" in tag else tag.lower()
    tag_colors = {
        k.lower(): v.lower()
        for k, v in config.Config().get_config(config.TAG_COLORS).items()
    }

    return tag_colors.get(tag, "blue")