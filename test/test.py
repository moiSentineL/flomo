import random
import time

from rich.live import Live
from rich.panel import Panel
from rich.text import Text


def generate_panel() -> Panel:
    """Generate a new panel with a random value and status."""
    value = random.random() * 100
    status = "[red]ERROR" if value < 50 else "[green]SUCCESS"
    panel_content = Text(f"Value: {value:3.2f}\nStatus: {status}")
    panel = Panel(panel_content, title=f"ID: {random.randint(1, 100)}")
    return panel


with Live(generate_panel(), refresh_per_second=4) as live:
    for _ in range(40):
        time.sleep(0.4)
        live.update(generate_panel())
