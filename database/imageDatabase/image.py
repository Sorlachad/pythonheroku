import imp
from re import I


import json as j
import itertools
import ast
class imageQuery:

    def onGetImageProductType(sqlDbconn) :
        print("Read")
        cursor = sqlDbconn.cursor()
        cursor.execute('''
        set bytea_output to 'escape';
            select json_agg(row_to_json(t))
            from (
                
                select type,image as image  from tb_typeimageproduct
            ) t
        ''')
        for row in cursor.fetchall():
            print(len(row[0]))
            return row[0]
        # for row in cursor:
        #     jout=(j.dumps(row[0]))
        #     jout=j.loads(jout)
        #     print(jout)      
        #     #jout=row
        #     return row[0]

    def onGetProduct(sqlDbconn) :
        print("Read")
        cursor = sqlDbconn.cursor()
        cursor.execute('''
            select json_agg(row_to_json(t))
            from (
                select idproduct,nameproduct,amount,details,material,
                (
                    select array_to_json(array_agg(row_to_json(js)))
                    from (
                        select image
                        from tb_headimage h
                        where h.idproduct=p.idproduct
                    ) js
                ) as images,    
                (
                    select array_to_json(array_agg(row_to_json(jd)))
                    from (
                        select colors as color,
                        (
                            select array_to_json(array_agg(row_to_json(je)))
                            from(
                                select size,price,amount
                                from tb_colors c
                                where c.idproduct=p.idproduct and b.colors=c.colors
                            ) je
                        ) as size
                        from tb_colors b
                        where b.idproduct=p.idproduct
                    ) jd
                ) as colors
                from tb_product p
            ) as t
        ''') 

        for row in cursor.fetchall():
            print(len(row[0]))
            return row[0]

    def onInsertFreeTypeImage(sqlDbconn, json):
        print(json)
        jsonString = j.dumps(json)
        print(jsonString)
        print('updete')
        cursor = sqlDbconn.cursor()
        # cursor.execute('''
        #     insert into [dbo].[User] ([username],[password]) values (?)
        #  ''',(jsonString))
        cursor.execute('''INSERT INTO tb_imagefreetype
        select image,name
        from openjson(?)
        with (
            image varchar(Max) '$.image',
            name varchar(50) '$.name'
        )AS json 
        ''', (jsonString))
        sqlDbconn.commit()