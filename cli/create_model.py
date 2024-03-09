# cli/create_model.py
import os
import click
import json

@click.group()
def create_model_command():
    pass

@create_model_command.command("create-model")
@click.argument("model_name")
def create_model(model_name):
    """
    Create a new model in the Frappe database.

    Example:
    python manage.py create-model User
    """
    model_directory = os.path.join("models", model_name)
    os.makedirs(model_directory, exist_ok=True)

    # Load existing JSON data if file already exists
    json_file_path = os.path.join(model_directory, f"{model_name}.json")
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as existing_json_file:
            existing_data = json.load(existing_json_file)
            existing_fields = existing_data.get("fields", [])
    else:
        existing_fields = []

    # Prompt user for additional fields
    click.echo("Enter the additional fields for the model (Press Enter when done):")
    fields = existing_fields.copy()
    while True:
        field_name = click.prompt("Field Name (Press Enter to finish)")
        if not field_name:
            break
        field_type = click.prompt("Field Type (e.g., Data, Int, ...)")
        label = click.prompt("Field Label")
        is_required = click.confirm("Is this field required?", default=True)
        is_all = click.prompt("Are these all your desired fields? (y/n). ")
        if is_all.lower() == "y":
            break

        fields.append({
            "fieldname": field_name,
            "fieldtype": field_type,
            "label": label,
            "reqd": int(is_required)
        })

    # Create User.py
    with open(os.path.join(model_directory, f"{model_name}.py"), "w") as user_file:
        user_file.write(f"from frappe import _dict, get_meta\n\n")
        user_file.write(f"class {model_name}:\n")
        user_file.write(f"    def __init__(self, data):\n")
        user_file.write(f"        meta = get_meta('{model_name}')\n")
        user_file.write(f"        self.doc = _dict(data)\n")
        user_file.write(f"        self.doc.doctype = '{model_name}'\n")

    # Update User.json with the merged list of fields
    json_data = {
        "fields": fields
    }

    with open(json_file_path, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
