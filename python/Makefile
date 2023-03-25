lint:
	poetry run black --check ./src
	poetry run isort --check ./src

	poetry run flake8 ./src
	poetry run mypy ./src
.PHONY: lint

format:
	poetry run black ./src
	poetry run autopep8 ./src
	poetry run isort ./src
.PHONY: format
