build:
	docker build -t 15-puzzle-cli .

PYTHON := docker run -it --rm 15-puzzle-cli python3

run: build
	$(PYTHON) index.py .

test: build
	$(PYTHON) -m unittest discover --v .
