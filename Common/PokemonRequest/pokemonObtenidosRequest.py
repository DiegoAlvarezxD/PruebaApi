from pydantic import BaseModel

class PokemonCreateRquest(BaseModel):
    nombre: str
    tipo: str