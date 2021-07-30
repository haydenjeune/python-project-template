[![CI](https://github.com/haydenjeune/python-project-template/actions/workflows/ci.yaml/badge.svg)](https://github.com/haydenjeune/python-project-template/actions/workflows/ci.yaml)

# Python Project Template

Welcome to my python project template.

## Requirements

To generate a project, you will need the following tools installed and accessible from the current shell:

- Git
- Make
- A Python installation
- Cookiecutter (A pip installable Python package. Consider using [pipx](https://github.com/pypa/pipx) to install globally)

## Usage

To create a new project from this template:

```
cookiecutter gh:haydenjeune/python-project-template
```

## Features

Right now this template has the below features, with more to come.

- Dependency management with `pip-compile`
- Formatting with `black`
- Type checking with `pyright`
- Linting with `flake8`
- Sorting of import statements with `isort`
- Checks running on `pre-commit` hooks
- Tests with `pytest` (with code coverage reports using `coverage`)
