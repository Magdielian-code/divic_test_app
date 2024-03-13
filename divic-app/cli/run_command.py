""" A module to take in commands from the user and run them. """

import click
from cli.commands import create_model_prompt, add_data_prompt


# python manage.py create-model <model_name>
@click.command()
@click.argument("model_name")
def create_model(model_name):
    """Create a new model."""
    create_model_prompt(model_name.capitalize())


# python manage.py add-data <model_name>
@click.command()
@click.argument("model_name")
def add_data(model_name):
    """Add data to a model."""
    add_data_prompt(model_name.capitalize())
