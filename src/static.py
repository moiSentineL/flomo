import shutil
import os
import time
import threading

first_name = " First Name: "
tag = " Tag: "
stopwatch = 0

size = 50

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"

def print_empty_rectangle(width, height, first_name="", tag="", stopwatch=""):
    left_padding = (width - size) // 2
    top_padding = (height - 7) // 2
    
    print("\n" * top_padding, end="")
    print(" " * left_padding + "+" + "----FLOMO" + "-"*(size-9) + "+")
    
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
        stopwatch += 1

def get_terminal_size():
    columns, lines = shutil.get_terminal_size()
    return columns, lines

def main():
    threading.Thread(target=update_stopwatch, daemon=True).start()

    while True:
        clear_terminal()
        width, height = get_terminal_size()
        print_empty_rectangle(width, height, first_name, tag, format_time(stopwatch))
        time.sleep(1)

if __name__ == "__main__":
    main()
