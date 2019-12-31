# Makefile
install:
	poetry install
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest
	pytest --cov=gendiff
