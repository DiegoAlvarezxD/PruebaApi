from pydantic import BaseModel
from typing import List

class PokemonResponse(BaseModel):
    nombre: str
    tipos: List[str]
    habilidades: List[str]
    peso: float
    altura: float