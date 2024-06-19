from rich.panel import Panel
from rich.live import Live
from rich.text import Text
import time
import threading
import blessed
import sys


class UI:
    def __init__(self, status: int, tag: str, name: str, break_time: int = None):
        self.tag = f"#{tag}"
        self.name = name
        self.status = status

        self.break_time = break_time
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
        content = Text(self.format_time(
            self.stopwatch if self.status == 0 else self.break_time))
        return Panel(content, expand=False, title=self.title,
                     border_style=self.border_style, title_align="left")

    def show_live_panel(self):
        with Live(self.generate_panel(), refresh_per_second=4, screen=True) as _live:
            while not self.close_live_panel:
                time.sleep(1)
                if self.status == 0:
                    self.stopwatch += 1
                elif self.status == 1:
                    # Solve Bug
                    self.break_time -= 1
                _live.update(self.generate_panel())

    def get_input(self):
        with self.terminal.cbreak(), self.terminal.hidden_cursor():
            return self.terminal.inkey()

# Here is the Idea: We call the main function with the tag and name of the task, which will start the working_ui and the break_ui when the user presses "q". After the break is over, we will call the main function again recursively.


def main(tag: str, name: str):
    # Thinking of doing it Recursively
    working_ui = UI(0, tag, name)
    working_panel_thread = threading.Thread(
        target=working_ui.show_live_panel, daemon=True)

    try:
        working_panel_thread.start()
        while True:
            inp = working_ui.get_input()
            if inp == "q":
                # break

                # the below code shouldnt be here! wip
                break_time = working_ui.stopwatch / 5
                working_ui.close_live_panel = True
                working_panel_thread.join()

                break_ui = UI(1, tag, name, break_time)
                break_panel_thread = threading.Thread(
                    target=break_ui.show_live_panel, daemon=True)
                break_panel_thread.start()
    except KeyboardInterrupt:
        working_ui.close_live_panel = True
        break_ui.close_live_panel = True
        working_panel_thread.join()
        break_panel_thread.join()
        sys.exit()


if __name__ == "__main__":
    main("Coding", "Work on Flomo")
