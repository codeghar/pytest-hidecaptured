.PHONY: init
init:
	pipenv install

.PHONY: build
build:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel

.PHONY: test
test:
	pipenv run tox

.PHONY: release
release:
	pipenv run twine upload dist/*
