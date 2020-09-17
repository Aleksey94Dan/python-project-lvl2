install:
	@poetry install

test:
	poetry run pytest --cov=gendif

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check:
	selfcheck test lint

build:
	@poetry build

.PHONY: install test lint selfcheck build
