from fastapi import APIRouter, Depends
from Facade.Saludo.saludo_facade import obtener_saludo, obtener_despedida
from Common.SaludoResponse.response_saludo import SaludoResponse
from Service.Token.token import verificar_token

router = APIRouter()

@router.get("/", response_model=SaludoResponse, dependencies=[Depends(verificar_token)])
def saludar():
    return obtener_saludo()

@router.get("/despedida", response_model=SaludoResponse, dependencies=[Depends(verificar_token)])
def despedida():
    return obtener_despedida()