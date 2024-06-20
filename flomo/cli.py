import click
import flomo.ui as ui


@click.group()
def flomo():
    pass


@flomo.command()
@click.option('-t', '--tag', default='Default', help='Session tag name.')
@click.option('-n', '--name', default='Work',
              help='Session Name')
def start(tag: str, name: str):
    ui.main(tag.lower(), name)


if __name__ == '__main__':
    flomo()
