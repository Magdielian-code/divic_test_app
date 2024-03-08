### README.md:

```markdown
# Frappe Backend Application

This is a small backend application built using the Frappe framework in Python. The application includes a CLI tool to facilitate the creation of new models in the database.

## Getting Started

### Prerequisites

Ensure you have Python and pip installed on your machine.

```bash
# Install Frappe framework
pip install frappe
```

## Usage

### CLI for Model Creation

To create a new model in the database, use the following command:

```bash
python manage.py create-model <model_name>
```

Replace `<model_name>` with the desired name of the model. For example, to create a model named "User," run:

```bash
python manage.py create-model User
```

On execution, a new directory `models/User` will be created containing:

- `User.py`: A Python class representing the model and extending a base Document class.
- `User.json`: Model definition file, specifying field types and required fields.

Feel free to customize the structure of the model and its corresponding JSON file in the created directory.

## Contributing

Feel free to contribute to the development of this application by forking the repository and creating pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This structure separates concerns and improves code organization. Each file now has a specific purpose, making it easier to maintain and understand. Adjust the code and structure based on your specific needs.