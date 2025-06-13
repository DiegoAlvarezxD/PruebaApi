from fastapi import FastAPI
from Api.saludoController.saludo_controller import router as saludo_router
from Api.PokeApi.poke_controller import router as pokemons_router

app = FastAPI(title="API de prueba")

app.include_router(saludo_router, prefix="/saludo", tags=["Saludo"])
app.include_router(pokemons_router, prefix="/pokemon", tags=["Pokemons"])