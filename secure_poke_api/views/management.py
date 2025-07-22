from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status

from secure_poke_api.models import PokemonType


@api_view(http_method_names=["POST"])
def add_type_to_user(request, type_name):
    try:
        pokemon_type = PokemonType.objects.get(name=type_name)
    except PokemonType.DoesNotExist:
        return Response(f"Unknown type: {type_name}", status.HTTP_400_BAD_REQUEST)

    pokemon_type.users.add(request.user)
    return Response(f"Added {type_name}")


@api_view(http_method_names=["POST"])
def remove_type_to_user(request, type_name):
    try:
        pokemon_type = PokemonType.objects.get(name=type_name)
    except PokemonType.DoesNotExist:
        return Response(f"Unknown type: {type_name}", status.HTTP_400_BAD_REQUEST)

    pokemon_type.users.remove(request.user)
    return Response(f"Removed {type_name}")


@api_view(http_method_names=["GET"])
def get_user_info(request):
    user = request.user
    return Response(
        {
            "username": user.username,
            "email": user.email,
            "pokemon_types": user.pokemon_groups.values_list("name", flat=True),
        }
    )
