# Usage Instructions

## External Dependencies

To run this project, `pyenv` and `virtualenvwrapper` are required. Both can be
installed with Homebrew.

## Manage Dependencies

`make install` - Install all dependencies into a virtualenv.

`make clean` - Remove the virtualenv.

## Run Application

`make run` - Runs {{cookiecutter.project_name}}/main.py inside the virtualenv

## Formatting

`make hooks` - Runs the pre-commit hooks over all code
