install:
	@poetry install
test:
	poetry run pytest --cov=gendif
lint:
	poetry run flake8 gendiff
check:
	@poetry check
.PHONY: install test lint check
