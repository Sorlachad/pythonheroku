import fastapi
from pydantic import BaseModel

class CreditCardModel(BaseModel):
    number:str
    name:str
    cvc:str
    endDate:str
    zip:str
    iduser:str