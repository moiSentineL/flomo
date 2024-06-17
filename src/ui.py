from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time
import threading
import blessed
import sys


class UI:
    def __init__(self, status: int, tag: str, name: str):
        self.tag = f"#{tag}"
        self.name = name
        self.status = status

        self.stopwatch = 0
        self.close_live_panel = False

        self.title = "Flomo - " + ("WORKING" if self.status == 0 else "BREAK")
        self.border_style = "bold blue" if self.status == 0 else "bold red"

        self.terminal = blessed.Terminal()

    def format_time(self, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def generate_panel(self):
        content = Text(self.format_time(self.stopwatch))
        return Panel(content, expand=False, title=self.title,
                     border_style=self.border_style, title_align="left")

    def show_live_panel(self):
        with Live(self.generate_panel(), refresh_per_second=4, screen=True) as _live:
            while not self.close_live_panel:
                time.sleep(1)
                self.stopwatch += 1
                _live.update(self.generate_panel())

    def get_input(self):
        with self.terminal.cbreak(), self.terminal.hidden_cursor():
            return self.terminal.inkey()


def main(tag: str, name: str):
    while True:
        workingUI = UI(0, tag, name)
        t1 = threading.Thread(target=workingUI.show_live_panel, daemon=True)

        try:
            t1.start()
            while True:
                inp = workingUI.get_input()
                if inp == "q":
                    pass
                else:
                    pass
        except KeyboardInterrupt:
            workingUI.close_live_panel = True
            t1.join()
            sys.exit()

    # HERE IS THE IDEA: Use Threading (sigh) to run the workingUI.show_live_panel() in parallel while another is taking input but... it will end up in a lot of threads (unclossed) when multiple cycles are done

    # if workingUI.stopwatch >= 5:
    #     print("hello")
    #     workingUI.close_live_panel = True

    # breakUI = UI(1, tag, name)
    # breakUI.show_live_panel()
    # if breakUI.stopwatch >= 2:
    #     breakUI.close_live_panel = True


if __name__ == "__main__":
    main("Coding", "Work on Flomo")
