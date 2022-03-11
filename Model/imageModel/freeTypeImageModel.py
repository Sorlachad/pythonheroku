import fastapi
from pydantic import BaseModel

class FreeTypeImageModel(list[BaseModel]):
    image:str
    name:str
