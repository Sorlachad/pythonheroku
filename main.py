from email.mime import image
from optparse import Option
from typing import Optional
from fastapi import FastAPI, Form, requests,status,HTTPException,Request
from fastapi.params import Body
from pydantic import BaseModel
import json
import logging
import uvicorn
from pathApp.User import app as userApp
from pathApp.User import creditpath as creditpath
from pathApp.GoogleMap import googlemap
from pathApp.image import pathimage
from pathApp.cart import cartRouter


#uvicorn main:app --host 0.0.0.0 --reload --proxy-headers --forwarded-allow-ips="*"

app = FastAPI()

app.include_router(userApp.UserRouter.router)
app.include_router(creditpath.Credit.router)
app.include_router(googlemap.router)
app.include_router(pathimage.ImageRouter.router)
app.include_router(cartRouter.cartRouter.router)
@app.get("/")
def root():
    return {"message":"hello world my api"}



# @app.get("/post")
# def get_post():
#     return {'data':"yes"}

# @app.post("/getuser")
# def getusers():
#         jout=u.getData(u.sqlDbconn)
#         return {'data':jout}

# @app.post("/adduser")
# async def getusers(response:Post):
#     print(response)
#     jsonout = u.onInsertJson(u.sqlDbconn,response)
#     print(jsonout)
#     return {'message':"success"}

# @app.post("/createpost")
# async def create_post(payload:Post):
#     print(payload)
#     # print(payload[0].json())
#     # #print(json.dumps(json.encoder(payload)))
#     # jsonen=payload[0].json()
#     # print(jsonen)
#     u.onInsertJson(u.sqlDbconn,json.dumps(payload))
#     jsonOut=await u.getData(u.sqlDbconn)
#     print('jsonout')
#     return {'data':jsonOut}




# @app.post('/createCard')
# async def createCard():
#     await u.crateCreditCard()


# @app.post('/payment')
# async def createCard():
#     await u.payment()
