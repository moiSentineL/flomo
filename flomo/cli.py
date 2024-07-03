import click
import click_aliases

import flomo.ui as ui


@click.group(cls=click_aliases.ClickAliasedGroup)
def flomo():
    """
    A Flowmodoro CLI for productivity enthusiasts.
    """
    pass


@flomo.command(aliases=["s"])
@click.option("-t", "--tag", default="Default", help="Session tag name.")
@click.option("-n", "--name", default="Work", help="Session Name")
def start(tag: str, name: str):
    """
    Start a Flowmodoro session.
    """
    ui.main(tag.lower(), name)


if __name__ == "__main__":
    flomo()
