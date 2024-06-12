import click
import src.ui as ui


@click.group()
def flomo():
    pass


@flomo.command()
@click.option('-t', '--tag', default='Default', help='Session tag name.')
@click.option('-n', '--name', default='Work',
              help='Session Name')
def start(tag, name):
    workingUI = ui.UI(0, tag, name)
    workingUI.show_live_panel()

    # TODO: Implement the Break shit in a function in ui.py


if __name__ == '__main__':
    flomo()
