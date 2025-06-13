from fastapi import APIRouter, Depends
from Facade.Pokemon.pokemon_facade import info_pokemon, poke_obtenidos
from Common.PokemonResponse.response_pokemon import PokemonResponse
from Common.PokemonResponse.PokemonObtenidosResponse import PokemonCreateResponse
from Service.Token.token import verificar_token
from Common.PokemonRequest.pokemonObtenidosRequest import PokemonCreateRquest

router = APIRouter()

@router.get("/{pokemon}", response_model=PokemonResponse, dependencies=[Depends(verificar_token)])
def pokemons(pokemon: str):
    return info_pokemon(pokemon)

@router.post("/obtenidos",response_model=PokemonCreateResponse, dependencies=[Depends(verificar_token)])
def pokemons(pokemon: PokemonCreateRquest):
    return poke_obtenidos(pokemon)