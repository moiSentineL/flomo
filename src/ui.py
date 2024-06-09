from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time


console = Console()


def rich_panel(status):
    global stopwatch
    stopwatch = 0

    if status == 1:
        text = "WORKING"
        color_plot = "bold blue"
    elif status == 2:
        text = "BREAK"
        color_plot = "bold red"

    title = "Flomo - " + text

    def format_time(seconds):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    # def update_stopwatch():  # for now redudant ...
    #     global stopwatch
    #     stopwatch = 0

    #     while True:
    #         time.sleep(1)
    #         # if not stop_timer:
    #         stopwatch += 1

    def generate_panel() -> Panel:
        global stopwatch
        content = Text(format_time(stopwatch))
        stopwatch += 1
        panel = Panel(content, expand=False, title=title,
                      border_style=color_plot, title_align="left")
        # stopwatch += 1
        # return Align.center(panel)
        return panel

    with Live(generate_panel(), refresh_per_second=4) as _live:
        # stop_timer = False -> can be used as a failsafe?
        while True:
            time.sleep(1)
            Live.update(_live, generate_panel())


if __name__ == "__main__":
    rich_panel(1)
