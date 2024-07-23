import os
import sys


def get_path(file_name: str, in_data: bool = False):
    # TODO: Change data folder to documents folder (and the equivalent in other OSes).

    conf_path = (
        os.path.expanduser("~/Documents/flomo")
        if platform.system().lower() == "windows"
        else os.path.expanduser("~/.config/flomo")
    )

    dir_path = os.path.dirname(os.path.realpath(conf_path))

    sign = "\\" if platform.system().lower() == "windows" else "/"
    data_folder = f"{sign}data" if in_data else ""

    if in_data and not os.path.exists(dir_path + data_folder):
        os.makedirs(dir_path + data_folder)

    file = f"{data_folder}{sign}{file_name}"

    return os.path.join(dir_path + file)
