from pydantic import BaseModel

class PokemonCreateResponse(BaseModel):
    nombre: str
    tipo: str