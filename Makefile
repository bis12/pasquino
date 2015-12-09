DB := DATABASE_URL=$$(heroku config:get DATABASE_URL)

all: test

test:
	tox

venv:
	tox -e venv

dev:
	$(DB) tox -e dev

init:
	$(DB) tox -e db -- init

migrate:
	$(DB) tox -e db -- migrate

upgrade:
	$(DB) tox -e db -- upgrade

clean:
	rm -rf .tox *.egg-info .cache
