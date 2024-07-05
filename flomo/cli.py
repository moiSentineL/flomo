import click
import click_aliases
import datetime

import flomo.ui as ui
import flomo.tracker as tracker


@click.group(cls=click_aliases.ClickAliasedGroup)
def flomo():
    """
    A Flowmodoro CLI for productivity enthusiasts.
    """
    pass


@flomo.command(aliases=["i"])
def init():
    """
    Initialize the database.
    """
    db = tracker.Tracker()
    db.create_table()
    db.conn.close()


@flomo.command(aliases=["s"])
@click.option("-t", "--tag", default="Default", help="Session tag name.")
@click.option("-n", "--name", default="Work", help="Session Name")
def start(tag: str, name: str):
    """
    Start a Flowmodoro session.
    """
    db = tracker.Tracker()
    db.create_table()
    session_id = db.create_session(tag, name, datetime.datetime.now())
    db.conn.close()
    ui.main(tag.lower(), name, session_id)


if __name__ == "__main__":
    flomo()
