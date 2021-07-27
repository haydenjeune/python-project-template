MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash -o pipefail
.PHONY: help install clean run hooks test

venv := .venv
python := $(venv)/bin/python
pip := $(venv)/bin/pip
pip-compile := $(venv)/bin/pip-compile

# install/upgrade requirements in the virtualenv
install: $(venv) .git/hooks/pre-commit

# remove the virtualenv
clean:
	rm -rf $(venv)

# run main.py
run: $(venv)
	python {{cookiecutter.project_name}}/main.py

# run tests
test: $(venv)
	$(venv)/bin/pytest -v --cov={{cookiecutter.project_name}} --cov-report term-missing ./tests

# run pre-commit hooks on all files
hooks: .git/hooks/pre-commit
	$(venv)/bin/pre-commit run -a

$(pip): $(pyversionfile)
	python -m venv --clear $(venv)
	$(pip) install --upgrade pip
	$(pip) install pip-tools

requirements.txt: requirements.in $(pip)
	$(venv)/bin/pip-compile --no-emit-index-url requirements.in

requirements.dev.txt: requirements.dev.in requirements.txt $(pip)
	$(venv)/bin/pip-compile --no-emit-index-url requirements.dev.in

$(venv): requirements.txt requirements.dev.txt $(pip)
	$(pip) install -e '.[dev]'
	touch $(venv)

.git/hooks/pre-commit: $(venv) .pre-commit-config.yaml
	$(venv)/bin/pre-commit install
