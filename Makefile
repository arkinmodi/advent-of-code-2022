AOC_DAYS := $(shell find . -maxdepth 1 -type d -name 'day_*')
PYTHON := ./venv/bin/python3

.PHONY: all
all: $(AOC_DAYS)

.PHONY: $(AOC_DAYS)
$(AOC_DAYS): virtualenv
	$(PYTHON) $@/$@.py

.PHONY: test
test: virtualenv
	$(PYTHON) -m pytest -s

.PHONY: virtualenv
virtualenv:
ifeq (,$(wildcard ./venv))
	virtualenv venv
	./venv/bin/pip install -r ./requirements.txt
endif

.PHONY: lint
lint: pre-commit

.PHONY: pre-commit
pre-commit:
	pre-commit run --all-files
