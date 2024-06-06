import click
# from src.logic import Flow

# flow = Flow()

# flow.initialize_flow()
# print("Started flow!")

# print("Waiting for input..")
# input()

# flow.break_flow()
# print("Time elapsed: ", flow.time_elapsed, "s")
# print("Time for break: ", flow.time_for_break, "s")

# # Wait for flow.time_for_break
# flow.restart_flow()
# print("Restarted Flow!")

# # repeat cycle until stop_flow


@click.group()
def hello():
    click.echo("host group")


@hello.command()
@click.option('-t', '--tag', default='Default', help='Session tag name.')
@click.option('-n', '--name', default='Work',
              help='Session Name')
def start(tag, name):
    click.echo("started")
    click.echo(f"tag: {tag}")
    click.echo(f"name: {name}")


if __name__ == '__main__':
    hello()
