from src.debug import debug_print
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.align import Align
import time
import datetime
import threading
import blessed
import sys


class UI:
    def __init__(self, status: int, tag: str, name: str, break_time: int = None):
        self.tag = f"#{tag}"
        self.name = name
        self.status = status

        self.break_time = round(break_time) if break_time else None
        self.stopwatch = 0
        self.close_live_panel = False

        self.title = "Flomo - " + \
            ("FLOWING" if self.status == 0 else "BREAKING")
        self.border_style = "bold blue" if self.status == 0 else "bold red"

        self.terminal = blessed.Terminal()

    def format_time(self, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def generate_panel(self):
        stuff = f"{self.name}\n{self.tag}\n\n{self.format_time(
            self.stopwatch if (self.status == 0) else self.break_time)}"
        content = Text(stuff, justify="center")
        return Align.center(
            Panel(content, expand=False, title=self.title,
                  border_style=self.border_style, title_align="center", padding=(1, 2)),
            vertical="middle",
            height=self.terminal.height
        )

    def show_live_panel(self):
        with Live(self.generate_panel(), refresh_per_second=4, screen=True) as _live:
            while not self.close_live_panel:
                time.sleep(1)
                if self.status == 0:
                    self.stopwatch += 1
                elif self.status == 1:
                    if not (self.break_time > 1):
                        break
                    self.break_time -= 1
                _live.update(self.generate_panel())

    def get_input(self):
        with self.terminal.cbreak(), self.terminal.hidden_cursor():
            return self.terminal.inkey()


def main(tag: str, name: str):
    try:
        while True:
            working_ui = UI(0, tag, name)
            break_ui = None
            working_panel_thread = threading.Thread(
                target=working_ui.show_live_panel, daemon=True)
            working_panel_thread.start()

            inp = ""
            while working_ui.stopwatch == 0 or not (working_ui.stopwatch != 0 and inp == "q"):
                inp = working_ui.get_input()

            break_time = working_ui.stopwatch / 5

            working_ui.close_live_panel = True
            working_panel_thread.join()

            del working_ui

            break_ui = UI(1, tag, name, break_time)
            break_ui.show_live_panel()
            break_ui.close_live_panel = True

            del break_ui
    except (KeyboardInterrupt, Exception) as e:
        if 'working_ui' in locals() and working_ui is not None:
            working_ui.close_live_panel = True
        if 'break_ui' in locals() and break_ui is not None:
            break_ui.close_live_panel = True
        if 'working_panel_thread' in locals() and working_panel_thread.is_alive():
            working_panel_thread.join()

        if isinstance(e, Exception):
            debug_print(f"{datetime.datetime.now()} - Error: {e}")
    finally:
        sys.exit()
