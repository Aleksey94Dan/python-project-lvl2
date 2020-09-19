install:
	@poetry install
test:
	poetry run pytest --cov=gendiff
lint:
	poetry run flake8 gendiff tests
check:
	@poetry check
.PHONY: install test lint check
