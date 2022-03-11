import imp
from re import I


import json as j


class queryUser:

    def onGetImageFreeType(sqlDbconn) :
        print("Read")
        cursor = sqlDbconn.cursor()
        cursor.execute('SELECT * FROM tb_user for json auto')
        for row in cursor:
            print('10')
            print(f'{row}')
            jout=(j.dumps(row[0]))
            jout=j.loads(jout)
            print(jout)        
            #jout=row
            return jout

    #TODO:insertJson
    def onInsertJson(sqlDbconn, json):
        print(json)
        jsonString = j.dumps(json)
        print(jsonString)
        print('updete')
        cursor = sqlDbconn.cursor()
        # cursor.execute('''
        #     insert into [dbo].[User] ([username],[password]) values (?)
        #  ''',(jsonString))
        cursor.execute('''INSERT INTO tb_user
        select username,password
        from openjson(?)
        with (
            username nvarchar(50) '$.username',
            password nvarchar(50) '$.password'
        )AS json 
        ''', (jsonString))
        sqlDbconn.commit()
    
    #TODO:Update
    def onUpdate(sqlDbconn):
        print('updete')
        cursor = sqlDbconn.cursor()
        cursor.execute('''
            update [dbo].[User] set username = ? where id = ?
        ''', ('sai', 5))
        sqlDbconn.commit()
    def insert(sqlDbconn):
        print("INSERT")
        cursor = sqlDbconn.cursor()
        cursor.execute('''
                    INSERT INTO [dbo].[User]([username],[password]) VALUES
                    (?,?)
                    ''',('time','1234'))
        sqlDbconn.commit()
    #TODO:DELETE

    def onDelete(sqlDbconn,payload):
        print('delete')
        cursor = sqlDbconn.cursor()
        cursor.execute('''
            delete from tb_user where username= ? 
        ''',(payload['username']))
        sqlDbconn.commit()

    def onAuthen(sqlDbconn,payload):
        print('delete')
        cursor = sqlDbconn.cursor()
        cursor.execute('''
            select id,username,password from tb_user where username= ? and password= ? for json auto
        ''',(payload['username'],payload['password']))
        for row in cursor:
            print(f'{row}')
            jout=(j.dumps(row[0]))
            jout=j.loads(jout)
            print(jout)        
            #jout=row
            return jout
        sqlDbconn.commit()

        #TODO:insertCreditcard   
        #  
    #TODO:insertcard
    def onInsertCard(sqlDbconn, json):
        print(json)
        jsonString = j.dumps(json)
        print(jsonString)
        print(f'updete {jsonString}')
        cursor = sqlDbconn.cursor()
        cursor.execute('''INSERT INTO CreditCard
        select number,name,endDate,cvc,zip,iduser
        from openjson(?)
        with (
            number nvarchar(50) '$.number',
            name nvarchar(50) '$.name',
            endDate nvarchar(50) '$.endDate',
            cvc nvarchar(50) '$.cvc',
            zip nvarchar(50) '$.zip',
            iduser nvarchar(50) '$.iduser'
        )AS json 
        ''', (jsonString))
        sqlDbconn.commit()
    def onGetCreditcard(sqlDbconn,iduser) :
        print("Read")
        cursor = sqlDbconn.cursor()
        cursor.execute('SELECT * FROM Creditcard where iduser=(?) for json auto',(iduser))
        for row in cursor:
            print('getcreditcard')
            print(f'{row}')
            jout=(j.dumps(row[0]))
            jout=j.loads(jout)
            print(jout)        
            #jout=row
            return jout