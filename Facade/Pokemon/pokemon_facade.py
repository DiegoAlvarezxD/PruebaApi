from Common.PokemonResponse.PokemonObtenidosResponse import PokemonCreateResponse
from Service.Pokemon.pokemon_service import obtener_info_pokemon, crear_pokemon_service
from Common.PokemonResponse.response_pokemon import PokemonResponse
from Common.PokemonRequest.pokemonObtenidosRequest import PokemonCreateRquest

def info_pokemon(nombre_pokemon: str) -> PokemonResponse:
    return obtener_info_pokemon(nombre_pokemon)

def poke_obtenidos(pokemon: PokemonCreateRquest) -> PokemonCreateResponse:
    return crear_pokemon_service(pokemon)