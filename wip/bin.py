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
status = int(input("Enter 1 for WORKING and 2 for BREAK: ")) #This is the main val to chagne break time and working also the color (Degub- Remove this)



if status == 1 :
    text = "WORKING"
    color_plot = "bold blue"
elif status == 2:
    text = "BREAK"
    color_plot = "bold red"
    
content = "Content of the panel, to be done later with formatting"
title = "Flomo - " + text 


panel = Panel(content, expand=False, title=title,
              border_style=color_plot, title_align="left")


center_panel = Align.center(panel)

console.print(center_panel)

# with Live(make_layout())
