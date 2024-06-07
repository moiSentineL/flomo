from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.live import Live
from rich.text import Text
import time


console = Console()
def rich_panel(status):
    global stopwatch
    stopwatch = 0

    # status = int(input("Enter 1 for WORKING and 2 for BREAK: ")) #This is the main val to chagne break time and working also the color (Degub- Remove this)
    # < redundant, passed on as parameter in main funtion


    if status == 1 :
        text = "WORKING"
        color_plot = "bold blue"
    elif status == 2:
        text = "BREAK"
        color_plot = "bold red"
        
    content = "Content of the panel, to be done later with formatting"
    title = "Flomo - " + text 

    

    def format_time(seconds):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def update_stopwatch(): # for now redudant ...
        
        global stopwatch
        stopwatch = 0

        while True:
            time.sleep(1)
            # if not stop_timer:
            stopwatch += 1


    def generate_panel() -> Panel:

        global stopwatch
        content = Text(format_time(stopwatch)) 
        stopwatch += 1
        panel = Panel(content, expand=False, title=title,
                      border_style=color_plot, title_align="left")
        # stopwatch += 1
        return panel




    with Live(generate_panel(), refresh_per_second=4):
        # stop_timer = False -> can be used as a failsafe?
        for n in range(5):
            time.sleep(0.4)
            Live.update(generate_panel())



if __name__ == "__main__":
    rich_panel(1)
