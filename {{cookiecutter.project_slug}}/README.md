# Usage Instructions

## Manage Dependencies

`make install` - Install all dependencies into a virtualenv.

`make clean` - Remove the virtualenv.

## Run/Test Application

`make run` - Runs `{{cookiecutter.project_name}}/main.py` inside the virtual environment

`make test` - Runs tests inside the `/tests`

## Formatting

`make hooks` - Runs the pre-commit hooks over all code
