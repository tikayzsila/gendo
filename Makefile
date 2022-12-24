.PHONY:

test:
	poetry run python gendock gen

build:
	poetry build --format wheel && poetry export --format requirements.txt --output constraints.txt --without-hashes --without dev

install: build
	pip install dist/*.whl --constraint constraints.txt && chmod +x gendock && sudo cp gendock /usr/local/bin/gendo