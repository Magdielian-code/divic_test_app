# # manage.py

# import os
# import click

# # Define a CLI command group using Click
# @click.group()
# def cli():
#     pass

# # Define a CLI command for creating a new model
# @cli.command("create-model")
# @click.argument("model_name")
# def create_model_command(model_name):
#     """
#     Create a new model in the database.

#     :param model_name: Name of the model to be created
#     """
#     # Create a directory path for the model
#     model_directory = os.path.join("models", model_name)
#     # Create the directory if it doesn't exist
#     os.makedirs(model_directory, exist_ok=True)

#     # Create User.py
#     with open(os.path.join(model_directory, f"{model_name}.py"), "w") as user_file:
#         # Write necessary import statements and define the class structure
#         user_file.write(f"from frappe import _dict, get_meta\n\n")
#         user_file.write(f"class {model_name}:\n")
#         user_file.write(f"    def __init__(self, data):\n")
#         user_file.write(f"        meta = get_meta('{model_name}')\n")
#         user_file.write(f"        self.doc = _dict(data)\n")
#         user_file.write(f"        self.doc.doctype = '{model_name}'\n")

#     # Create User.json (customize the model structure here)
#     with open(os.path.join(model_directory, f"{model_name}.json"), "w") as json_file:
#         # Write the JSON structure defining fields and their properties
#         json_file.write("{\n")
#         json_file.write("    \"fields\": [\n")
#         json_file.write("        {\n")
#         json_file.write("            \"fieldname\": \"field1\",\n")
#         json_file.write("            \"fieldtype\": \"Data\",\n")
#         json_file.write("            \"label\": \"Field 1\",\n")
#         json_file.write("            \"reqd\": 1\n")
#         json_file.write("        },\n")
#         json_file.write("        {\n")
#         json_file.write("            \"fieldname\": \"field2\",\n")
#         json_file.write("            \"fieldtype\": \"Int\",\n")
#         json_file.write("            \"label\": \"Field 2\",\n")
#         json_file.write("            \"reqd\": 1\n")
#         json_file.write("        }\n")
#         json_file.write("    ]\n")
#         json_file.write("}\n")

# # Entry point: Run the CLI if this script is executed directly
# if __name__ == "__main__":
#     cli()


# manage.py
from cli import create_model_command

if __name__ == "__main__":
    create_model_command()











