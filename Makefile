.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

install: ## install dependencies
	pipenv install

install-dev: install ## install dev dependencies
	pipenv install --dev

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: ## check style with flake8
	pipenv run flake8 vo tests

test: ## run tests quickly with the default Python
	pipenv run pytest

test-all: ## run tests on every Python version with tox
	pipenv run tox --skip-missing-interpreters

coverage: ## check code coverage quickly with the default Python
	rm -rf htmlcov
	pipenv run coverage run --source vo -m pytest
	pipenv run coverage report -m
	pipenv run coverage html

docs: ## generate Sphinx HTML documentation, including API docs
	pipenv run $(MAKE) -C docs clean
	pipenv run $(MAKE) -C docs html

release: clean ## package and upload a release
	pipenv run python setup.py sdist upload
	pipenv run python setup.py bdist_wheel upload

sdist: clean ## package
	pipenv run python setup.py sdist
	ls -l dist
