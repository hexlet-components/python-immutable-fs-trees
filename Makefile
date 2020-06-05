export PYTHONPATH=src


.PHONY: all
all: lint pytest doctest
	@echo Done!

.PHONY: pytest
pytest:
	@poetry run pytest test

.PHONY: doctest
doctest:
	@poetry run python -m doctest -v README.md

.PHONY: lint
lint:
	@poetry run flake8 --statistics src test

.PHONY: install
install:
	@poetry install
