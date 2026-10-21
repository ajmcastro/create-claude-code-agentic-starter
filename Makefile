UV ?= uv
PYTHON_VERSION ?= 3.11
ARGS ?= data/sample_flight.csv

.PHONY: help setup test lint format check run

help:
	@printf '%s\n' \
		'Available targets:' \
		'  setup   Install Python and sync project dependencies' \
		'  test    Run the test suite' \
		'  lint    Check code with Ruff' \
		'  format  Format code with Ruff' \
		'  check   Run tests and lint' \
		'  run     Run missionlog (ARGS defaults to the sample flight)'

setup:
	$(UV) python install $(PYTHON_VERSION)
	$(UV) python pin $(PYTHON_VERSION)
	$(UV) sync --extra dev

test:
	$(UV) run --extra dev pytest -q

lint:
	$(UV) run --extra dev ruff check .

format:
	$(UV) run --extra dev ruff format .

check: test lint

run:
	$(UV) run python -m missionlog $(ARGS)
