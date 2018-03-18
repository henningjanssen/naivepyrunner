build: sdist wheel

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

publish:
	twine upload dist/*

all: build publish
