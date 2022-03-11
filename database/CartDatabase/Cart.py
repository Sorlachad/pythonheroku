from re import I
import psycopg2
from Model.CartModel.CartModel import CartModel
from database import connect as db



class CartQuery:
    def onAddItemsCart(items:CartModel):
        print("add")
        print(items)
        con=db.sqlDbconn_product
        cur=con.cursor()
        cur.execute('select idproduct from tb_cart where idproduct=%s and userid=%s',(items.idproduct,items.userid))
        if(cur.fetchall()==[]):
            cur.execute('insert into tb_cart (idproduct,userid) values(%s,%s)',(items.idproduct,items.userid))
            cur.execute('''
                insert into tb_cartdetails (userid,idproduct,price,amount,color,size) values(%s,%s,%s,%s,%s,%s)
                ''',(items.userid,items.idproduct,items.price,items.amount,items.color,items.size))
        else:
            cur.execute('''
                insert into tb_cartdetails (userid,idproduct,price,amount,color,size) values(%s,%s,%s,%s,%s,%s)
                ''',(items.userid,items.idproduct,items.price,items.amount,items.color,items.size))          
        # cur.execute('insert into tb_cart (idproduct,userid) values(%s,%s)',(items.idproduct,items.userid))
        # cur.execute('''
        # insert into tb_cartdetails (userid,idproduct,price,amount,color,size) values(%s,%s,%s,%s,%s,%s)
        # ''',(items.userid,items.idproduct,items.price,items.amount,items.color,items.size))
        con.commit()
        return 'success'
    def onDeleteItemCart(id):
        con=db.sqlDbconn_product
        cur=con.cursor()
        cur.execute('''
        delete from tb_cart where cartid = %s

        ''',(id))
        con.commit()
    def onUpdateItemsCart(items:CartModel):
        con=db.sqlDbconn_product
        cur=con.cursor()
        cur.execute('''
        update tb_cartdetails
        set price=price+%s,amount=amount+%s
        where idproduct = %s and
        color = %s and size=%s

        ''',(items.price,items.amount,items.idproduct,items.color,items.size))
        con.commit()
        return "success"
    
    def onGetItemsCart(items):
        print(items)
        con=db.sqlDbconn_product
        cur=con.cursor()
        cur.execute('''
            select json_agg(row_to_json(t))
            from (
                    select sum(price) as totalprice,sum(amount) as totalamount,
                    (
                    select array_to_json(array_agg(row_to_json(jt)))
                        from(     
                    select idproduct,(
                        select p.nameproduct 
                        from tb_product p 
                        where c.idproduct=p.idproduct
                    ),
                    (
                        select array_to_json(array_agg(row_to_json(js)))
                        from(
                            select color,size,amount,price
                            from tb_cartdetails cd
                            where cd.idproduct=c.idproduct
                        )js
                    ) as product,
                    (
                    select array_to_json(array_agg(row_to_json(js)))
                    from (
                        select image
                        from tb_headimage h
                        where h.idproduct=c.idproduct
                    ) js
                ) as images
                    from tb_cart c
                    ) jt
                    ) as cart
                    from tb_cartdetails
                )as t
        ''',([items['userid']]))
        for row in cur.fetchall():
            print(len(row[0]))
            return row[0]
        con.commit()
