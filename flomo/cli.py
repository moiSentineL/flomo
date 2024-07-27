import datetime
import sys
from typing import Tuple

import click
import click_aliases

import flomo.config as conf
import flomo.errors as errors
import flomo.helpers as helpers
import flomo.tracker as tracker
import flomo.ui as ui


class OrderCommands(click.Group):
    def list_commands(self, ctx: click.Context) -> list[str]:
        return list(self.commands)


class MultiClass(click_aliases.ClickAliasedGroup, OrderCommands):
    pass


@click.group(cls=MultiClass)
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

    conf.Config(initializing=True).create_config()


default_tag, default_name = conf.get_default_session_data()


@flomo.command(aliases=["s"])
@click.option(
    "-t",
    "--tag",
    help="Session Tag",
    default=default_tag,
)
@click.option(
    "-n",
    "--name",
    help="Session Name",
    default=default_name,
)
def start(tag: str, name: str):
    """
    Start a Flowmodoro session.
    """
    try:
        tag = tag.lower()
        db = tracker.Tracker()
        db.create_table()
        session_id = db.create_session(tag, name, datetime.datetime.now())
        db.conn.close()
        ui.main(tag, name, session_id)
    except (
        errors.DBFileNotFoundError,
        errors.NoConfigError,
        errors.InvalidConfigKeyError,
        Exception,
    ) as e:
        helpers.error_log(f"{datetime.datetime.now()} - Error: {e}")
        print(e)
    finally:
        sys.exit()


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
        helpers.error_log(str(e))
        print(e)


@flomo.command(aliases=["d"])
@click.argument("session_ids", nargs=-1)
def delete(session_ids: Tuple):
    """
    Delete sessions.
    """
    click.confirm("Are you sure you want to delete the session(s)?", abort=True)
    try:
        db = tracker.Tracker()
        db.delete_session(session_ids)
        db.conn.close()
        print(f"Deleted session(s) {session_ids}")
    except (
        errors.DBFileNotFoundError,
        errors.NoSessionError,
    ) as e:
        helpers.error_log(str(e))
        print(e)

@flomo.command(aliases=["ch"])
@click.argument("session_id")
@click.option("-t", "--tag", help="Session Tag")
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
        helpers.error_log(str(e))
        print(e)

@flomo.command(aliases=["cf"])
@click.option("-n", "--notif", help="Set notification priority to 'off', 'normal', or 'high'.")
@click.option("-tc", "--tag-color", nargs=2, help="Set or delete tag colors.")
@click.option("-ds", "--default-session", nargs=2, help="Set default session data. (Tag, Name)")
def config(notif: str, tag_color: Tuple[str, str] | Tuple[str], default_session: Tuple[str, str]):
    """
    Change the config values or get the config file path.
    """
    try:
        print(f"File Path: {helpers.get_path("config.json", True)}")

        if notif and (notif := notif.lower()) in ["off", "normal", "high"]:
            conf.Config().set_config(conf.NOTIFICATION_PRIORITY, notif)
            print(f"Notification Priority set to {notif}")

        if tag_color and len(tag_color) == 2:
            conf.Config().set_config(conf.TAG_COLORS, dict(tag_name=tag_color[0], color=tag_color[1]))
            print(f"{tag_color[0]}'s Tag Color set to {tag_color[1]}")
        elif tag_color and len(tag_color) == 1:
            conf.Config().delete_tag_color(tag_color[0])
            print(f"Deleted Tag Color for {tag_color[0]}")

        if default_session and len(default_session) == 2:
            conf.Config().set_config(conf.DEFAULT_SESSION_DATA, dict(tag=default_session[0], name=default_session[1]))
            print(f"Default Session Data set to {default_session}")
    except errors.NoConfigError as e:
        helpers.error_log(str(e))
        print(e)


@flomo.command(aliases=["er"])
@click.option("-c", "--clear", is_flag=True, help="Clear the error log.")
def error(clear: bool):
    """
    Show the error log.
    """
    try:
        path = helpers.get_path("error.log", True)
        print(f"File Path: {path}")
        if clear:
            with open(path, "w") as f:
                f.write("")
            return print("Message log cleared.")

        with open(path, "r") as f:
            if not f.read():
                return print("No errors found till now.")
            print(f.read())
    except FileNotFoundError:
        print("No errors found till now.")


if __name__ == "__main__":
    flomo()
