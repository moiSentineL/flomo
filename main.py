import click
import src.ui as ui


@click.group()
def hello():
    click.echo("host group")


@hello.command()
@click.option('-t', '--tag', default='Default', help='Session tag name.')
@click.option('-n', '--name', default='Work',
              help='Session Name')
def start(tag, name):
    ui.main(f"#{tag}", name)


if __name__ == '__main__':
    hello()
