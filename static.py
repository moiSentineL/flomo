import shutil
import os
import time
import threading
import curses

first_name = " First Name: "
tag = " Tag: "
stopwatch = 0  

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"

def print_empty_rectangle(width, height, first_name="", tag="", stopwatch=""):
    terminal_size = shutil.get_terminal_size()
    left_padding = (terminal_size.columns - width) // 2
    top_padding = (terminal_size.lines - height) // 2
    
    print("\n" * top_padding, end="")
    print(" " * left_padding + "+" + "-" * (width - 2) + "+")
    
    for i in range(height - 2):
        if i == 1 and first_name:
            print(" " * left_padding + "|" + first_name.ljust(width - 3) + "|")
        elif i == 2 and tag:
            print(" " * left_padding + "|" + tag.ljust(width - 3) + "|")
        elif i == 3 and stopwatch:
            print(" " * left_padding + "| " + stopwatch.ljust(width - 3) + " |")
        else:
            print(" " * left_padding + "|" + " " * (width - 2) + "|")
    
    print(" " * left_padding + "+" + "-" * (width - 2) + "+")

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def update_stopwatch():
    global stopwatch
    while True:
        time.sleep(1)
        stopwatch += 1

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    size = (15, 10)  # Width, Height
    threading.Thread(target=update_stopwatch, daemon=True).start()

    while True:
        stdscr.clear()
        print_empty_rectangle(*size, first_name, tag, format_time(stopwatch))
        stdscr.refresh()
        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(main)
