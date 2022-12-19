lint:
	poetry run black --check .
	poetry run isort --check .

	poetry run flake8 .
	poetry run mypy .
.PHONY: lint

format:
	poetry run black .
	poetry run autopep8 .
	poetry run isort .
.PHONY: format
