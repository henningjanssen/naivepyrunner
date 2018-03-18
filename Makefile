all: sdist wheel

wheel:
	python setup.py bdist_wheel

sdist:
	python setup.py sdist

upload:
	twine upload dist/*
