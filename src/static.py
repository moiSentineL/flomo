import shutil
import os
import platform
import signal
import time
import threading

first_name = " First Name: "
tag = " Tag: "
stopwatch = 0  

def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{mins:02}:{secs:02}"

def print_empty_square(size, first_name="", tag="", stopwatch=""):
    terminal_size = shutil.get_terminal_size()
    vet = terminal_size.columns
    hai = terminal_size.lines
    
    left_padding = (vet - (size * 2 + 2)) // 2
    top_padding = (hai - (size + 2)) // 2
    
    print("\n" * top_padding, end="")
    print(" " * left_padding + "----FLOMO-----------------------")
    
    for i in range(size):
        if i == 1 and first_name:
            print(" " * left_padding + "8" + first_name.ljust(size * 2) + "8")
        elif i == 2 and tag:
            print(" " * left_padding + "8" + tag.ljust(size * 2) + "8")
        elif i == 3 and stopwatch:
            print(" " * left_padding + "8" + stopwatch.ljust(size * 2) + "8")
        else:
            print(" " * left_padding + "8" + " " * (size * 2) + "8")
    
    print(" " * left_padding + "8" + "_" * (size * 2) + "8")

def clear_terminal():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")

def handle_resize(signum, frame):
    clear_terminal()
    print_empty_square(size, first_name, tag, format_time(stopwatch))
def update_stopwatch():
    global stopwatch
    while True:
        time.sleep(1)
        stopwatch += 1
        handle_resize(None, None)

if __name__ == "__main__":
    size = 15

    signal.signal(signal.SIGWINCH, handle_resize)

    clear_terminal()
    print_empty_square(size, first_name, tag, format_time(stopwatch))
    threading.Thread(target=update_stopwatch, daemon=True).start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
