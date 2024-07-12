.PHONY: install
install:
	poetry env use 3.12
	poetry install

.PHONY: lint
lint:
	poetry run black --check ./src
	poetry run isort --check ./src

	poetry run flake8 ./src
	poetry run mypy ./src
	poetry run refurb ./src

.PHONY: format
format:
	poetry run black ./src
	poetry run isort ./src
