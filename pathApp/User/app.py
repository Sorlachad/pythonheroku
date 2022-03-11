from re import I
import main as m
from database import connect as con
from database.UserDatabase import userquery as uq
from fastapi import APIRouter, Body, Depends, Form, HTTPException,status,Request,WebSocket
import Model.UserModel.usermodel as umodel
from Model.UserModel import usermodel,creditcardmodel as um
import logging
import Logsetting as Log
import psycopg2





class UserRouter:
    router = APIRouter(
        prefix="/time/api",
        tags=["user"],
        responses={404: {"description": "Notfound"}}
    )

    @router.post('/getuser')
    def getusers(request:Request):
        jout = uq.queryUser.onGetUser(con.sqlDbconn)
        text=f' IP: {request.client.host}:{request.client.port} Method:getuser status:{status.HTTP_200_OK}'
        Log.writeLog(__name__,logging.INFO,'UserRouter',text)
        return {'data': jout}
    
    @router.post('/delete')
    def onDelete(request:Request,payload:dict=Body(...)):
        jout = uq.queryUser.onDelete(con.sqlDbconn,payload)
        text=f' IP: {request.client.host}:{request.client.port} Method:delete status:{status.HTTP_200_OK}'
        Log.writeLog(__name__,logging.INFO,'UserRouter',text)
        return {'data': jout}


    @router.post("/adduser")
    async def adduser(request:Request,response:umodel.UserModel):
        try:
            print(response)
            jsonout = uq.queryUser.onInsertJson(con.sqlDbconn,response)
            text=f' IP: {request.client.host}:{request.client.port} Method:adduser status:{status.HTTP_200_OK}'
            Log.writeLog(__name__,logging.DEBUG,'UserRouter',text)
            print(jsonout)
        except psycopg2.DatabaseError as ex:
            print(ex)
            text=f' IP: {request.client.host}:{request.client.port} Method:adduser status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'UserRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {'status':status.HTTP_200_OK,"data":None}
    
    @router.post('/authen')
    def getusers(request:Request,payload:dict=Body(...)):
        try:
            jout = uq.queryUser.onGetUser(con.sqlDbconn)
            text=f' IP: {request.client.host}:{request.client.port} Method:authen status:{status.HTTP_200_OK}'
        except psycopg2.DatabaseError as ex:
            print(ex)
            text=f' IP: {request.client.host}:{request.client.port} Method:authen status:{status.HTTP_404_NOT_FOUND} error:{ex}'
            Log.writeLog(__name__,logging.DEBUG,'UserRouter',text)
            return {"status":status.HTTP_404_NOT_FOUND,"data":str(ex).split('.')[3]}
        return {"status":status.HTTP_200_OK,'data': jout}
    
    
    @router.websocket("/ws/time/websocket")
    async def websocket_endpoint(websocket: WebSocket):
        print("webb")
        await websocket.accept()
        while True:
            try:
                data = await websocket.receive_text()
                await websocket.send_text(f"Message text was: {f'{data}'}")
            except:
                #await websocket.send_text(f"Message text was: {f'{data}'}")
                print('close')
                break
    @router.websocket("/ws/time/user")
    async def websocket_endpoint(websocket: WebSocket):
        print("webb")
        await websocket.accept()
        while True:
            try:
                data = await websocket.receive_text()
                await websocket.send_text(f"Message text was user: {f'{data}'}")
            except:
                #await websocket.send_text(f"Message text was: {f'{data}'}")
                print('close')
                break

    @router.post("/hook")
    async def webhook(request: Request,body:dict=Body(...)):
        print("webhook")
        print(f'data {body}')
       
