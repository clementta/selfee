from django.core.management.base import BaseCommand

from secure_poke_api.models import Pokemon, PokemonType
from secure_poke_api.services import PokeApi


class Command(BaseCommand):
    help = "Update pokemon types list"

    def handle(self, *args, **options):
        poke_api = PokeApi()
        for pokemon in poke_api.get_pokemons():
            pokemon_obj, _ = Pokemon.objects.get_or_create(
                name=pokemon["name"], pokeapi_id=pokemon["id"]
            )
            pokemon_obj.types.clear()
            for pokemon_type in pokemon["types"]:
                poke_type, _ = PokemonType.objects.get_or_create(
                    name=pokemon_type["type"]["name"]
                )
                pokemon_obj.types.add(poke_type)
