import requests
from Common.PokemonResponse.response_pokemon import PokemonResponse
from Common.PokemonResponse.PokemonObtenidosResponse import PokemonCreateResponse
from Common.Constants.PokemonConstants import POKEAPI_BASE_URL
from Common.PokemonRequest.pokemonObtenidosRequest import PokemonCreateRquest

pokemon_db = []

def obtener_info_pokemon(nombre_pokemon: str) -> PokemonResponse:
    url = f"{POKEAPI_BASE_URL}/pokemon/{nombre_pokemon.lower()}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"No existe informacion del Pokemon: {nombre_pokemon}")
    
    data = response.json()

    nombre = data["name"]
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    habilidades = [habilidad["ability"]["name"] for habilidad in data["abilities"]]
    peso = data["weight"] / 10.0
    altura = data["height"] / 10.0
    
    return PokemonResponse(nombre=nombre,tipos=tipos,habilidades=habilidades,peso=peso,altura=altura)

def crear_pokemon_service(pokemon: PokemonCreateRquest) -> PokemonCreateResponse:
    nuevo = {"nombre": pokemon.nombre, "tipo": pokemon.tipo}
    pokemon_db.append(nuevo)
    return PokemonCreateResponse(**nuevo)