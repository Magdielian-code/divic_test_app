# cli/create_model.py
import os
import click

@click.group()
def create_model_command():
    pass

@create_model_command.command("create-model")
@click.argument("model_name")
def create_model(model_name):
    """
    Create a new model in the database.

    Example:
    python manage.py create-model User
    """
    model_directory = os.path.join("models", model_name)
    os.makedirs(model_directory, exist_ok=True)

    # Prompt user for fields
    click.echo("Enter the fields for the model (Press Enter when done):")
    fields = []
    while True:
        field_name = click.prompt("Field Name (Press Enter to finish)")
        if not field_name:
            break
        field_type = click.prompt("Field Type (e.g., Data, Int, ...)")
        label = click.prompt("Field Label")
        is_required = click.confirm("Is this field required?", default=True)
        
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

    # Create User.json
    with open(os.path.join(model_directory, f"{model_name}.json"), "w") as json_file:
        json_file.write("{\n")
        json_file.write("    \"fields\": [\n")
        json_file.write("        {\n")
        json_file.write("            \"fieldname\": \"field1\",\n")
        json_file.write("            \"fieldtype\": \"Data\",\n")
        json_file.write("            \"label\": \"Field 1\",\n")
        json_file.write("            \"reqd\": 1\n")
        json_file.write("        },\n")
        json_file.write("        {\n")
        json_file.write("            \"fieldname\": \"field2\",\n")
        json_file.write("            \"fieldtype\": \"Int\",\n")
        json_file.write("            \"label\": \"Field 2\",\n")
        json_file.write("            \"reqd\": 1\n")
        json_file.write("        }\n")
        json_file.write("    ]\n")
        json_file.write("}\n")
