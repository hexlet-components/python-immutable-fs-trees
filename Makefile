export PYTHONPATH=src

install:
	@uv sync

build:
	@uv build

lint:
	@uv run ruff check src test

test:
	@uv run pytest test

check: test lint
	@echo Done!

.PHONY: install build lint test doctest check
