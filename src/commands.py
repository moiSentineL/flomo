import click



@click.command()
@click.option('-t', '--tag', default='Default', help='Session tag name.')
@click.option('-n', '--name', default='Work',
              help='Session Name')
def hello(t, n):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == '__main__':
    hello()
