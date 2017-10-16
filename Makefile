
PWD = $(shell pwd)
DOCKER := docker run -it --rm -v "${PWD}/src:/src" 15-puzzle-cli

install:
	docker build -t 15-puzzle-cli .

run:
	$(DOCKER) python3 index.py

test:
	$(DOCKER) python3 -m unittest discover --v -b

lint:
	$(DOCKER) pep8 .
