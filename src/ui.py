import shutil
import os
import time
import threading

first_name = " First Name: "
tag = " Tag: "
stopwatch = 0
status = 1  # debug
size = 50
stop_timer = False

# Platform-specific imports
if os.name == 'nt':  # For Windows
    import msvcrt
else:  # For Unix-like systems
    import sys
    import termios
    import tty


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"


def print_empty_rectangle(width, height, first_name="", tag="", stopwatch=""):
    left_padding = (width - size) // 2
    top_padding = (height - 7) // 2

    print("\n" * top_padding, end="")

    if status == 1:
        print(" " * left_padding + "+" +
              "----Flomo - WORKING" + "-"*(size-19) + "+")

    elif status == 2:
        print(" " * left_padding + "+" +
              "----Flomo - BREAK" + "-"*(size-17) + "+")

    for i in range(7):
        if i == 1 and first_name:
            print(" " * left_padding + "|" + first_name.center(size) + "|")
        elif i == 2 and tag:
            print(" " * left_padding + "|" + tag.center(size) + "|")
        elif i == 3 and stopwatch:
            print(" " * left_padding + "|" + stopwatch.center(size) + "|")
        else:
            print(" " * left_padding + "|" + " " * size + "|")

    print(" " * left_padding + "+" + "-" * size + "+")


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def update_stopwatch():
    global stopwatch
    while True:
        time.sleep(1)
        if not stop_timer:
            stopwatch += 1


def get_terminal_size():
    columns, lines = shutil.get_terminal_size()
    return columns, lines


# def user_input():
#     global stop_timer
#     global status
#     while True:

def unix():
    global stop_timer
    global status
    while True:
        tty.setcbreak(sys.stdin.fileno())
        key = sys.stdin.read(1)
        # print("hit")
        if key == 'q':
            stop_timer = True
            status = 2
        


def main():
    global stop_timer
    global status

    threading.Thread(target=update_stopwatch, daemon=True).start()
    if os.name == 'nt':  # For Windows
        pass
    else:  # For Unix-like systems
        threading.Thread(target=unix, daemon=True).start()

    while True:
        if os.name == 'nt':  # For Windows
            if msvcrt.kbhit():
                key = msvcrt.getch().decode()
                if key == 'q':
                    stop_timer = True
                    status = 2
        else:  # For Unix-like systems
            pass

        clear_terminal()
        width, height = get_terminal_size()

        print_empty_rectangle(width, height, first_name,
                              tag, format_time(stopwatch))
        time.sleep(1)


if __name__ == "__main__":
    main()
    # user_input()
