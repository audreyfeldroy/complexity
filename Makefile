.PHONY: clean-pyc clean-build docs

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 complexity tests

test:
	python setup.py test

test-all:
	tox

coverage:
	coverage run --source complexity setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm docs/complexity.rst
	rm docs/modules.rst
	sphinx-apidoc -o docs/ complexity
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html
