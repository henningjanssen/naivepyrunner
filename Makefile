build: sdist wheel

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

publish:
	twine upload dist/*

clean:
	python setup.py clean
	rm -rf build/ dist/ *.egg*/ .eggs
	find . -type f -name '*.pyc' -delete
	find . -name __pycache__ -delete

all: build publish
