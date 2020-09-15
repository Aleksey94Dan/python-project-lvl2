install:
		@poetry install

test:
		poetry run pytest --cov=gendiff

lint:
		poetry run flake8 gendiff

selfcheck:
		poetry check

check:
		selfcheck test lint

build: check
		@poetry build

.PHONY: install test lint selfcheck build
