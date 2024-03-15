"""A module to prompt the user for information about a new model."""

import os
import json
import click
from database.create_model import create_table

def create_model_prompt(model_name):
    """Prompt the user for information about a new model."""
    model_dir = f"models/{model_name}"

    if os.path.exists(model_dir):
        click.echo(f"Model '{model_name}' already exists.")
        return

    model = {"name": model_name, "fields": []}
    field_names = set()

    while True:
        field_name = click.prompt("Field name")
        field_name = field_name.lower().replace(" ", "_")

        if field_name in field_names:
            click.echo(f"Field '{field_name}' already exists.")
            continue

        field_type = click.prompt(
            "Field type", type=click.Choice(["string", "integer", "float", "boolean"])
        )
        required = click.prompt("Required? [y/n]", type=bool)
        unique = click.prompt("Unique? [y/n]", type=bool)
        model["fields"].append(
            {
                "field_name": field_name,
                "field_type": field_type,
                "required": required,
                "unique": unique,
            }
        )
        field_names.add(field_name)

        if not click.confirm("Add another field?"):
            break

    os.makedirs(model_dir)

    model_schema = os.path.join(model_dir, f"{model_name}.json")
    with open(model_schema, "w", encoding="utf-8") as f:
        json.dump(model, f, indent=2)

    model_py_file = os.path.join(model_dir, f"{model_name}.py")
    with open(model_py_file, "a", encoding="utf-8") as f:
        f.close()

    create_table(model)
    return


def add_data_prompt(model_name):
    """Prompt the user for data entry based on the schema."""
    model_schema = f"models/{model_name}/{model_name}.json"
    if not os.path.exists(model_schema):
        click.echo(f"Error: Schema not found for model {model_name}")
        return

    with open(model_schema, "r", encoding="utf-8") as f:
        schema = json.load(f)

    data = {}
    for field in schema["fields"]:
        field_name = field["field_name"]
        field_type = field["field_type"]
        prompt_text = f"Enter {field_name} ({field_type}): "
        if field_type == "string":
            data[field_name] = click.prompt(prompt_text, type=str)
        elif field_type == "integer":
            data[field_name] = click.prompt(prompt_text, type=int)
        elif field_type == "float":
            data[field_name] = click.prompt(prompt_text, type=float)
        elif field_type == "boolean":
            data[field_name] = click.prompt(prompt_text, type=bool)

    return data

def get_data_query(model_name, fields, filters = None):
    """ An endpoint to query the Database for the data in the model based on the ilters and fieds"""
    query = f"SELECT {', '.join(fields)} FROM {model_name}"
    if filters:
        query += " WHERE " + " AND ".join(filters)
