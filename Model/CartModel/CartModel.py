from pydantic import BaseModel


class CartModel(BaseModel):
    cartid:int=1
    userid:int
    idproduct:int
    czid:int=1
    price:int
    amount:int
    color:str
    size:str

    