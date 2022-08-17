all: test

test:
	python3 -m unittest discover -v -s tests -p 'test_*.py'
