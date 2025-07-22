from django.contrib.auth.models import User
from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users = models.ManyToManyField(User, related_name="pokemon_groups")


class Pokemon(models.Model):
    pokeapi_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50, unique=True)
    types = models.ManyToManyField(PokemonType, related_name="pokemons")
