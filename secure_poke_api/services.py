import requests
from django.conf import settings


class PokeApi:
    def __init__(self):
        self.base_url = settings.POKE_API_BASE_URL

    def get_types(self):
        resp = requests.get(f"{self.base_url}type").json()
        while "There is pages":
            yield from resp["results"]
            if next_url := resp["next"]:
                resp = requests.get(next_url).json()
            else:
                break

    def get_pokemons(self):
        resp = requests.get(f"{self.base_url}pokemon", params={"limit": 200}).json()
        while "There is pages":
            for item in resp["results"]:
                pokemon_resp = requests.get(item["url"]).json()
                yield pokemon_resp

            if next_url := resp["next"]:
                resp = requests.get(next_url).json()
            else:
                break

    def get_pokemon(self, pokemon_name):
        return requests.get(f"{self.base_url}pokemon/{pokemon_name}").json()
