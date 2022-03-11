from re import I
import main as m
from database import connect as con
from database.CartDatabase import Cart as cart
from fastapi import APIRouter, Body, Depends, Form, HTTPException,status,Request,WebSocket
import Model.UserModel.usermodel as umodel
from Model.CartModel import CartModel as cartmodel
import logging
import Logsetting as Log
import psycopg2


class cartRouter:
    router = APIRouter(
        prefix="/time/api",
        tags=["cart"],
        responses={404: {"description": "Notfound"}}
    )

    @router.post('/addcart')
    def CartRouter(request:Request,payload:cartmodel.CartModel):
        try:
            jout = cart.CartQuery.onAddItemsCart(payload)
            text=f' IP: {request.client.host}:{request.client.port} Method:addcart status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
        except psycopg2.DatabaseError as ex:
            text=f' IP: {request.client.host}:{request.client.port} Method:addcart status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,'data': jout}

    @router.post('/getcart')
    def getcart(request:Request,payload:dict=Body(...)):
        try:
            jout = cart.CartQuery.onGetItemsCart(payload)
            text=f' IP: {request.client.host}:{request.client.port} Method:getcart status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
        except psycopg2.DatabaseError as ex:
            text=f' IP: {request.client.host}:{request.client.port} Method:getcart status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,'data': jout}


    @router.post('/updatecart')
    def getcart(request:Request,payload:cartmodel.CartModel):
        try:
            jout = cart.CartQuery.onUpdateItemsCart(payload)
            text=f' IP: {request.client.host}:{request.client.port} Method:updatecart status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
        except psycopg2.DatabaseError as ex:
            text=f' IP: {request.client.host}:{request.client.port} Method:updatecart status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'CartRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,'data': jout}
