.PHONY: install test lint

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

lint:
	flake8 .
	black --check .
	isort --check-only .
