import datetime

import click
import click_aliases

import flomo.config as config
import flomo.errors as errors
import flomo.helpers as helpers
import flomo.tracker as tracker
import flomo.ui as ui

# TODO: Ability for users to see message.log file.
# TODO: Change Config data from a Command


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

    conf = config.Config(initializing=True)
    conf.create_config()


default_session_data = config.Config(get_default_session_data=True).get_config(
    "default_session_data"
)


@flomo.command(aliases=["s"])
@click.option(
    "-t",
    "--tag",
    help="Session tag name.",
    default=default_session_data["tag"],
)
@click.option(
    "-n",
    "--name",
    help="Session Name",
    default=default_session_data["name"],
)
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
    except (
        errors.DBFileNotFoundError,
        errors.NoConfigError,
        errors.InvalidConfigKeyError,
    ) as e:
        helpers.message_log(str(e))
        # TODO: print(e) isnt printing anything


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
        helpers.message_log(str(e))
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
    except (
        errors.DBFileNotFoundError,
        errors.NoSessionError,
    ) as e:
        helpers.message_log(str(e))
        print(e)


@flomo.command(aliases=["ch"])
@click.argument("session_id")
@click.option("-t", "--tag", help="Session tag name.")
@click.option("-n", "--name", help="Session Name")
def change(session_id: str, tag: str | None, name: str | None):
    """
    Change session data.
    """
    try:
        db = tracker.Tracker()
        db.update_session(int(session_id), tag, name)
        db.conn.close()
    except (
        errors.DBFileNotFoundError,
        errors.NoSessionError,
    ) as e:
        helpers.message_log(str(e))
        print(e)


if __name__ == "__main__":
    flomo()
