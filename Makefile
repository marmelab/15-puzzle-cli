build:
	docker build -t 15-puzzle-cli .

DOCKER := docker run -it --rm 15-puzzle-cli

run:
	$(DOCKER) python3 index.py

test:
	$(DOCKER) python3 -m unittest discover --v

lint:
	$(DOCKER) pep8 .
