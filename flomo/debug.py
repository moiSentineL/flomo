import os
import platform


def debug_print(message: str):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = "\\debug.log" if platform.system().lower() == "windows" else "/debug.log"
    path = os.path.join(dir_path + file)

    with open(path, "a") as f:
        f.write(message + "\n")
