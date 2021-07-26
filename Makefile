SHELL = /bin/bash -o pipefail

.PHONY: test install clean hooks

venv := .venv
python := $(venv)/bin/python
pip := $(venv)/bin/pip
pip-compile := $(venv)/bin/pip-compile

# install/upgrade requirements in the virtualenv
install: $(venv) .git/hooks/pre-commit

# remove the virtualenv
clean:
	rm -rf $(venv)

# tests that a project can be generated
test:
	./tests/test_project_generation.sh

# run pre-commit hooks on all files
hooks: .git/hooks/pre-commit
	$(venv)/bin/pre-commit run -a

$(venv):
	python -m venv --clear $(venv)
	$(pip) install --upgrade pip
	$(pip) install pre-commit

.git/hooks/pre-commit: $(venv) .pre-commit-config.yaml
	$(venv)/bin/pre-commit install
