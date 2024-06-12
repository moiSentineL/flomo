from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.align import Align
import time


class UI:
    def __init__(self, status: int, tag: str, name: str):
        self.stopwatch = 0

        self.title = "Flomo - " + ("WORKING" if status == 0 else "BREAK")
        self.border_style = "bold blue" if status == 0 else "bold red"

        self.close_live_panel = False

        self.tag = f"#{tag}"
        self.name = name

    def format_time(self, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def generate_panel(self):
        content = Text(self.format_time(self.stopwatch))
        panel = Panel(content, expand=False, title=self.title,
                      border_style=self.border_style, title_align="left")
        # return Align.center(panel)
        return panel

    def show_live_panel(self):
        with Live(self.generate_panel(), refresh_per_second=4, screen=True) as _live:
            while not self.close_live_panel:
                time.sleep(1)
                self.stopwatch += 1
                _live.update(self.generate_panel())


if __name__ == "__main__":
    tag, name = "Coding", "Work on Flomo"

    workingUI = UI(0, tag, name)
    workingUI.show_live_panel()

    # HERE IS THE IDEA: Use Threading (sigh) to run the workingUI.show_live_panel() in parallel while another is taking input but... it will end up in a lot of threads (unclossed) when multiple cycles are done

    # if workingUI.stopwatch >= 5:
    #     print("hello")
    #     workingUI.close_live_panel = True

    # breakUI = UI(1, tag, name)
    # breakUI.show_live_panel()
    # if breakUI.stopwatch >= 2:
    #     breakUI.close_live_panel = True
