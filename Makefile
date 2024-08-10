
.PHONY: venv clean install freeze

.DEFAULT_GOAL := build

venv:
	@python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip

clean:
	@echo "Cleaning up ..."
	@rm -f .coverage

install:
	@pip install -r requirements.txt

freeze:
	@pip freeze > requirements.txt

build:
	@echo "Building the project ..."
