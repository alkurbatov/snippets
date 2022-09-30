.PHONY: format lint

lint:
	poetry run black --check .
	poetry run isort --check .

	poetry run flake8 .
	poetry run mypy .

format:
	poetry run black .
	poetry run autopep8 .
	poetry run isort .
