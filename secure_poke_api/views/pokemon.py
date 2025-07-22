from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from secure_poke_api.models import Pokemon
from secure_poke_api.services import PokeApi


@api_view(http_method_names=["GET"])
def get_pokemons(request):
    filters = Q()
    for type_name in request.user.pokemon_groups.values_list("name", flat=True):
        filters.add(Q(types__name=type_name), Q.OR)

    if not filters:
        return Response({"pokemon": []})

    pokemons = Pokemon.objects.filter(filters).values_list("name", flat=True)
    return Response({"pokemon": pokemons})


@api_view(http_method_names=["GET"])
def get_pokemon(request, pokemon_name_or_id):
    try:
        pokemon_id = int(pokemon_name_or_id)
        queryset = Pokemon.objects.filter(
            pokeapi_id=pokemon_id, types__in=request.user.pokemon_groups.all()
        )

    except ValueError:
        queryset = Pokemon.objects.filter(
            name=pokemon_name_or_id, types__in=request.user.pokemon_groups.all()
        )

    pokemon = get_object_or_404(queryset)
    poke_api = PokeApi()
    return Response(poke_api.get_pokemon(pokemon.name))
