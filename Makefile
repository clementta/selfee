.PHONY: dev migrate migrations populate shell

dev:
	uv run manage.py runserver

migrate:
	uv run manage.py migrate

migrations:
	uv run manage.py makemigrations

populate:
	uv run manage.py update_pokemons

shell:
	uv run manage.py shell

