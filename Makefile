all: test

test:
	python3 -m unittest discover -v -s tests -p 'test_*.py'

blinker:
	python3 main.py 3
