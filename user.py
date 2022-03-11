
import json as j
import stripe



def onInsertJson(sqlDbconn,json):
    print(json)
    jsonString = j.dumps(json)
    print(jsonString)
    print('updete')
    cursor = sqlDbconn.cursor()
    # cursor.execute('''
    #     insert into [dbo].[User] ([username],[password]) values (?)
    #  ''',(jsonString))
    cursor.execute('''INSERT INTO tb_user3
    select username,password
	from openjson(?)
	with (
		username nvarchar(50) '$.username',
		password nvarchar(50) '$.password'
	)AS json 
    ''',(jsonString))
    sqlDbconn.commit()

#onDelete(sqlDbconn)
# getData(sqlDbconn)
