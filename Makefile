.DEFAULT_GOAL := run

DOCKER_RUN := docker run -it --rm -v $(PWD):/src --workdir="/src" --entrypoint="" -u $(shell id -u):$(shell id -g) python:3.7.4-alpine3.10

run:
	$(DOCKER_RUN) python3 -i date-to-text.py

test:
	$(DOCKER_RUN) ./date-to-text.py --test
