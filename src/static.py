import shutil
import os
import platform
import signal
import time
import threading

# Initial values for the text elements
first_name = "First Name: "
tag = "Tag: "
stopwatch = 0  # Start the stopwatch at 0

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
            print(" " * left_padding + "|" + first_name.ljust(size * 2) + "|")
        elif i == 2 and tag:
            print(" " * left_padding + "|" + tag.ljust(size * 2) + "|")
        elif i == 3 and stopwatch:
            print(" " * left_padding + "|" + stopwatch.ljust(size * 2) + "|")
        else:
            print(" " * left_padding + "|" + " " * (size * 2) + "|")
    
    print(" " * left_padding + "|" + "_" * (size * 2) + "|")

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

    # Set up signal handling for terminal resize events
    signal.signal(signal.SIGWINCH, handle_resize)

    clear_terminal()
    print_empty_square(size, first_name, tag, format_time(stopwatch))

    # Start the stopwatch in a separate thread
    threading.Thread(target=update_stopwatch, daemon=True).start()

    # Keep the program running to handle resize events and update the stopwatch
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
