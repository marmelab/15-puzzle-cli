
PWD = $(shell pwd)
DOCKER := docker run -it --rm -v "${PWD}/src:/src" 15-puzzle-cli

help: ## Print all commands (default)
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## Install the dependencies and build the docker
	docker build -t 15-puzzle-cli .

run: ## Run the 15-puzzle game
	$(DOCKER) python3 index.py

test: ## Run all tests
	$(DOCKER) python3 -m unittest discover --v -b

lint: ## Run the pep8 linter
	$(DOCKER) pep8 .
