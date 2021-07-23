MAKEFLAGS += --warn-undefined-variables
SHELL = /bin/bash -o pipefail
.PHONY: help install clean run

pyversionfile := .python-version
pyversion := $(shell cat ${pyversionfile})

venv := .venv
python := $(venv)/bin/python
pip := $(venv)/bin/pip
pip-compile := $(venv)/bin/pip-compile

# display this help message
help:
	@awk '/^##.*$$/,/^[~\/\.a-zA-Z_-]+:/' $(MAKEFILE_LIST) | awk '!(NR%2){print $$0p}{p=$$0}' | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' | sort

# install/upgrade requirements in the virtualenv
install: $(venv) install-hooks

# remove the virtualenv
clean:
	rm -rf $(venv)

# run main.py
run: $(venv)
	python {{cookiecutter.project_name}}/main.py

$(pip): $(pyversionfile)
	# create new virtualenv $(venv) containing pip
	$(if $(value VIRTUAL_ENV),$(error Cannot create a virtualenv when running in a virtualenv. Please deactivate the current virtual env $(VIRTUAL_ENV)),)
	pyenv install -s $(pyversion)
	python -m venv --clear $(venv)
	$(pip) install pip-tools

requirements.txt: requirements.in $(pip)
	$(pip-compile) --no-index requirements.in

requirements.dev.txt: requirements.dev.in $(pip)
	$(pip-compile) --no-index requirements.dev.in

$(venv): requirements.txt requirements.dev.txt $(pip)
	$(pip) install -e '.[dev]'
	touch $(venv)

install-hooks: $(venv)
	$(venv)/bin/pre-commit install

hooks: install-hooks
	$(venv)/bin/pre-commit run -a

