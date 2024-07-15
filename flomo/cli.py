import datetime
import sqlite3

import click
import click_aliases

import flomo.tracker as tracker
import flomo.ui as ui
import flomo.errors as errors
import flomo.config as config


@click.group(cls=click_aliases.ClickAliasedGroup)
def flomo():
    """
    A Flowmodoro CLI for productivity enthusiasts.
    """
    pass


@flomo.command(aliases=["i"])
def init():
    """
    Initialize the required files for Flomo.
    """
    db = tracker.Tracker(initializing=True)
    db.create_table()
    db.conn.close()

    config.Config().create_config()


@flomo.command(aliases=["s"])
@click.option("-t", "--tag", default="Default", help="Session tag name.")
@click.option("-n", "--name", default="Work", help="Session Name")
def start(tag: str, name: str):
    """
    Start a Flowmodoro session.
    """
    try:
        db = tracker.Tracker()
        db.create_table()
        session_id = db.create_session(tag, name, datetime.datetime.now())
        db.conn.close()
        ui.main(tag.lower(), name, session_id)
    except errors.DBFileNotFoundError as e:
        print(e)


@flomo.command(aliases=["t"])
def tracking():
    """
    Show the tracking history.
    """
    try:
        tracker.show_sessions()
    except (
        errors.DBFileNotFoundError,
        errors.NoSessionsError,
        errors.NoSessionError,
    ) as e:
        print(e)


@flomo.command(aliases=["d"])
@click.argument("session_id")
def delete(session_id: str):
    """
    Delete a session.
    """
    try:
        db = tracker.Tracker()
        db.delete_session(int(session_id))
        db.conn.close()
    except (errors.DBFileNotFoundError, errors.NoSessionError) as e:
        print(e)


if __name__ == "__main__":
    flomo()
