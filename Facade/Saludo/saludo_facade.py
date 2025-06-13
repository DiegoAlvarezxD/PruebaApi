from Service.Saludo.saludo_service import generar_saludo, generar_despedida
from Common.SaludoResponse.response_saludo import SaludoResponse

def obtener_saludo() -> SaludoResponse:
    mensaje = generar_saludo()
    return SaludoResponse(mensaje=mensaje)

def obtener_despedida() -> SaludoResponse:
    mensaje = generar_despedida()
    return SaludoResponse(mensaje=mensaje)