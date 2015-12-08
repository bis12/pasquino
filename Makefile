all: test

test:
	tox

dev:
	tox -e dev

clean:
	rm -rf .tox *.egg-info .cache
