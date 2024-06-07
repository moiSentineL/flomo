from rich.console import Console
from rich.panel import Panel
# from rich.table import Table
from rich.align import Align


console = Console()

# table = Table(title="test bro")

# table.add_column("Name: tag:", justify="right", no_wrap=True)
# table.add_row("hello")
# table.add_row("Bru")

# console.print(table)

content = "Content of the panel, to be done later with formatting"
title = "Flomo - WORKING"


panel = Panel(content, expand=False, title=title,
              border_style="bold blue", title_align="left")


center_panel = Align.center(panel)

console.print(center_panel)

# with Live(make_layout())
