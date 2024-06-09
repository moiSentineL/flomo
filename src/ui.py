from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time


class UI:
    def __init__(self, status: int):
        self.console = Console()
        self.stopwatch = 0

        self.title = "Flomo - " + ("WORKING" if status == 1 else "BREAK")
        self.border_style = "bold blue" if status == 1 else "bold red"

    def format_time(self, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def generate_panel(self):
        content = Text(self.format_time(self.stopwatch))
        panel = Panel(content, expand=False, title=self.title,
                      border_style=self.border_style, title_align="left")
        return panel

    def show_live_panel(self):
        with Live(self.generate_panel(), refresh_per_second=4) as _live:
            while True:
                time.sleep(1)
                self.stopwatch += 1
                _live.update(self.generate_panel())


if __name__ == "__main__":
    ui = UI(1)
    ui.show_live_panel()
