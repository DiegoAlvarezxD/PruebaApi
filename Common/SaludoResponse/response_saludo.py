from pydantic import BaseModel

class SaludoResponse(BaseModel):
    mensaje: str
