from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel

class UserModel(list[BaseModel]):
    username:str
    password:str

