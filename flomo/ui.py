from flomo.debug import debug_print

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
    def __init__(self, status: int, tag: str, name: str, chilling_time: int = None):
        self.tag = f"#{tag}"
        self.name = name
        self.status = status

        self.chilling_time = round(chilling_time) if chilling_time else None
        self.stopwatch = 0
        self.close_live_panel = False

        self.title = "Flomo - " + \
            ("FLOWING" if self.status == 0 else "CHILLIN")
        self.border_style = "bold blue" if self.status == 0 else "bold red"

        self.terminal = blessed.Terminal()

    def format_time(self, seconds: int):
        hours, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def generate_panel(self):
        stuff = f"{self.name}\n[grey70]{self.tag}[/grey70]\n\n{self.format_time(
            self.stopwatch if (self.status == 0) else self.chilling_time)}\n\n\\[q] - {'break' if self.status == 0 else 'skip?'}    [Ctrl+C] - quit"
        content = Text.from_markup(stuff, justify="center", style="yellow")
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
                    if not (self.chilling_time > 1):
                        break
                    self.chilling_time -= 1
                _live.update(self.generate_panel())

    def get_input(self):
        with self.terminal.cbreak(), self.terminal.hidden_cursor():
            return self.terminal.inkey().lower()


def main(tag: str, name: str):
    try:
        while True:
            flowing_ui = UI(0, tag, name)
            flowing_panel_thread = threading.Thread(
                target=flowing_ui.show_live_panel, daemon=True)
            flowing_panel_thread.start()

            inp = ""
            while flowing_ui.stopwatch == 0 or not (flowing_ui.stopwatch != 0 and inp == "q"):
                inp = flowing_ui.get_input()

            chilling_time = flowing_ui.stopwatch / 5

            flowing_ui.close_live_panel = True
            flowing_panel_thread.join()

            del flowing_ui

            chilling_ui = UI(1, tag, name, chilling_time)
            chilling_ui.show_live_panel()
            # chilling_panel_thread = threading.Thread(
            #     target=chilling_ui.show_live_panel, daemon=True)
            # chilling_panel_thread.start()

            # while True:
            #     if chilling_ui.chilling_time == 1:
            #         break
            #     debug_print(str(chilling_ui.chilling_time))
            #     inp = chilling_ui.get_input()
            #     if inp == "q":
            #         break

            chilling_ui.close_live_panel = True
            # chilling_panel_thread.join()

            del chilling_ui
    except (KeyboardInterrupt, Exception) as e:
        if 'flowing_ui' in locals() and flowing_ui is not None:
            flowing_ui.close_live_panel = True
        if 'chilling_ui' in locals() and chilling_ui is not None:
            chilling_ui.close_live_panel = True
        if 'flowing_panel_thread' in locals() and flowing_panel_thread.is_alive():
            flowing_panel_thread.join()
        # if 'chilling_panel_thread' in locals() and chilling_panel_thread.is_alive():
        #     chilling_panel_thread.join()

        if isinstance(e, Exception):
            debug_print(f"{datetime.datetime.now()} - Error: {e}")
    finally:
        sys.exit()
