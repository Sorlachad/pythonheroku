import base64
import os
import json

from database import connect as db
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('D://เสื้อผ้า//เสื้อ') if isfile(join('D://เสื้อผ้า//เสื้อ', f))]
onlyfiles2 = [f for f in listdir('D://เสื้อผ้า//เสื้อ//imageproducttype') if isfile(join('D://เสื้อผ้า//เสื้อ//imageproducttype', f))]
print(onlyfiles2)
image=[]
price=500
amount=5
for x in onlyfiles:
    with open("D://เสื้อผ้า//เสื้อ//"+x, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        spl=x.split(".")
        image.append({"nameproduct":spl[0],"amount":amount,"price":price,"material":"เนื้อผ้า","detail":spl[0],"image":encoded_string,"colors":"black","size":"m"})
    price+=100
    amount+=2

# for x in onlyfiles2:
#     with open("D://เสื้อผ้า//เสื้อ//imageproducttype//"+x, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#         spl=x.split(".")
#         image.append({"image":encoded_string,"type":spl[0]})

def typetoDB(jsonString):
    sqlDbconn=db.conhero
    cursor = sqlDbconn.cursor()
    for items in jsonString:
        cursor.execute('''
            insert into tb_typeimageproduct
            (image,type)
            values
            (%s,%s)
        ''',(items['image'],items['type']))
    sqlDbconn.commit()

def toDB(jsonString):
    sqlDbconn=db.conhero
    cursor = sqlDbconn.cursor()
    for items in jsonString:
            # cursor.execute('''
            #     insert into [dbo].[User] ([username],[password]) values (?)
            #  ''',(jsonString))
        cursor.execute('''
            insert into tb_product
            (nameproduct,amount,material,details)
            values
            (%s,%s,%s,%s);

            insert into tb_headimage (idproduct,image) 
            values
            ((select currval(pg_get_serial_sequence('tb_product','idproduct'))),%s);

            insert into tb_colors (colors,idproduct,size,amount,price)
            values
            (%s,(select currval(pg_get_serial_sequence('tb_product','idproduct'))),%s,%s,%s)
            ''',
            (items['nameproduct'],items['amount'],str(items['material']),str(items['detail']),str(items['image']),items['colors'],items['size'],items['amount'],items['price']))
    sqlDbconn.commit()
    # '''insert into tblStaff values
    # (@name, @age, @address)

    # insert into tblRoleOfStuff values
    # (scope_identity(), @roleid)'''
# toDB(image)
#typetoDB(image)
#typetoDB(image)