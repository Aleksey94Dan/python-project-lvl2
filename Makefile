install:
	@poetry install
test:
	poetry run pytest --cov=gendif
lint:
	poetry run flake8 gendiff
check:
	poetry check
build:
	@poetry build
.PHONY: install test lint check build
