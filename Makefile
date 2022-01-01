export PYTHONPATH=src


.PHONY: install
install:
	@poetry install

.PHONY: build
build:
	@poetry build

.PHONY: lint
lint:
	@poetry run flake8 --statistics src test

.PHONY: test
test:
	@poetry run pytest test

.PHONY: doctest
doctest:
	@poetry run python -m doctest -v README.md

.PHONY: all
all: lint test doctest
	@echo Done!
