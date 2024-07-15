import datetime
import sqlite3

import click
import click_aliases

import flomo.tracker as tracker
import flomo.ui as ui

# TODO: "Memory Management" isnt working properly when sessions.db is present without any table


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
    # create_db_file = False
    # if not os.path.exists(helpers.get_path("sessions.db", True)):
    #     create_db_file = True

    db = tracker.Tracker()
    # if create_db_file:
    #     db.create_table()
    db.create_table()
    session_id = db.create_session(tag, name, datetime.datetime.now())
    db.conn.close()
    ui.main(tag.lower(), name, session_id)


@flomo.command(aliases=["t"])
def tracking():
    """
    Show the tracking history.
    """
    try:
        # if not os.path.exists(helpers.get_path("sessions.db", True)):
        #     raise sqlite3.OperationalError
        tracker.show_sessions()
    except sqlite3.OperationalError:
        print("No sessions were found.")


@flomo.command(aliases=["d"])
@click.argument("session_id")
def delete(session_id: str):
    """
    Delete a session.
    """
    try:
        # if not os.path.exists(helpers.get_path("sessions.db", True)):
        #     raise sqlite3.OperationalError
        db = tracker.Tracker()
        db.delete_session(float(session_id))
        db.conn.close()
    except sqlite3.OperationalError:
        print("No sessions were found.")


if __name__ == "__main__":
    flomo()
