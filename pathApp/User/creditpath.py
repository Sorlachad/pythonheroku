import imp
from re import I
import main as m
from database import connect as con
from database.UserDatabase import userquery as uq
from fastapi import APIRouter, Body, Depends, HTTPException,status
import Model.UserModel.usermodel as umodel
from Model.UserModel import usermodel,creditcardmodel as um
import psycopg2

class Credit:
    router = APIRouter(
            prefix="/time/api",
            tags=["credit"],
            responses={404: {"description": "Notfound"}}
        )

    @router.post("/addcreditcard")
    async def addcreditcard(response:um.CreditCardModel):
            print(response)
            try:
                jsonout = uq.queryUser.onInsertCard(con.sqlDbconn,response.dict())
            except:
                HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="maybe number repeat")
                return {"message":status.HTTP_404_NOT_FOUND}
            print(jsonout)
            return {    'message':status.HTTP_200_OK}


    @router.post('/getcreditcard')
    async def getcreditcard(payload: dict = Body(...)):
            try:
                json=uq.queryUser.onGetCreditcard(con.sqlDbconn,payload['iduser']) 
            except psycopg2.Error as ex:
                return {"status":status.HTTP_404_NOT_FOUND,"error":ex}
            return {
                "status":status.HTTP_200_OK,
                "data": json}