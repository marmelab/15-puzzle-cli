build:
	docker build -t 15-puzzle-cli .

DOCKER := docker run -it --rm 15-puzzle-cli

run: build
	$(DOCKER) python3 index.py .

test: build
	$(DOCKER) python3 -m unittest discover --v .

linter: build
	$(DOCKER) pep8 .
