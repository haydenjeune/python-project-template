SHELL = /bin/bash -o pipefail

.PHONY: test

test:
	./tests/test_project_generation.sh
