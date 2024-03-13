""" A CLI for managing the application. """

import click
from cli.run_command import create_model, add_data


@click.group()
def cli():
    """
    Divic Test CLI.
    """


cli.add_command(create_model)
cli.add_command(add_data)


if __name__ == "__main__":
    cli()
