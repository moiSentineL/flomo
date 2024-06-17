# an attempt to make no-ui work

import time
import threading
import os
import sys
from blessed import Terminal


term = Terminal()

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    mins, secs = divmod(remainder, 60)
    return f"{hours:02}:{mins:02}:{secs:02}"


def timer(stopwatch): 

    timer = round(stopwatch/5)

    while notbruh:

        time.sleep(1)
        timer -= 1
        
        if timer != 0:
            print(term.clear + f"--- Flomo - Break ---\n{format_time(timer)}")
        else:
            sys.exit()

def funcstopwatch(): 

    global stopwatch
    stopwatch = 60


    while bruh:

        time.sleep(1)
        stopwatch += 1
        
        print(term.clear + f"--- Flomo - Working ---\n{format_time(stopwatch)}")


if __name__ == "__main__":

    bruh = True

    th1 = threading.Thread(target=funcstopwatch, daemon=True)
    th2 = threading.Thread(target=timer, daemon=True)

    th1.start()


    while True:
        with term.cbreak(), term.hidden_cursor():
            inp = term.inkey()
            if inp == "q":
                # sys.exit() -> to debug if the keypress thingy works or not.
                bruh = False
                stop = stopwatch
                notbruh = True
                timer(stop)
            else:
                pass