from asyncio.windows_events import NULL
from re import I
import main as m
from database import connect as con
from database.imageDatabase import image as uq
from fastapi import APIRouter, Body, Depends, Form, HTTPException,status,Request,WebSocket
import Model.UserModel.usermodel as umodel
from Model.imageModel import freeTypeImageModel as imagemodel
import logging
import Logsetting as Log
import psycopg2


class ImageRouter:
    router = APIRouter(
        prefix="/time/api",
        tags=["image"],
        responses={404: {"description": "Notfound"}}
    )
    

    @router.post('/getfreetypeimage')
    def getImage(request:Request):
        try:
            jout = uq.imageQuery.onGetImageProductType(con.sqlDbconn_product)
            text=f' IP: {request.client.host}:{request.client.port} Method:getfreetypeimage status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
        except psycopg2.DatabaseError as ex:
            text=f' IP: {request.client.host}:{request.client.port} Method:getfreetypeimage status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,'data': jout}
    
    @router.post('/getproduct')
    def getImage(request:Request):
        try:
            jout = uq.imageQuery.onGetProduct(con.sqlDbconn_product)
            text=f' IP: {request.client.host}:{request.client.port} Method:getproduct status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
        except psycopg2.DatabaseError as ex:
            text=f' IP: {request.client.host}:{request.client.port} Method:getproduct status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,'data': jout}

    @router.post('/sendimage')
    def getusers(request:Request,payload:imagemodel.FreeTypeImageModel):
        try:
            jout = uq.imageQuery.onInsertFreeTypeImage(con.sqlDbconn_product,payload)
            text=f' IP: {request.client.host}:{request.client.port} Method:sendimagefreetype status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
        except psycopg2.DatabaseError as ex:
            print(ex)
            text=f' IP: {request.client.host}:{request.client.port} Method:sendimagefreetype status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'ImageRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {"status":status.HTTP_200_OK,'data': jout}