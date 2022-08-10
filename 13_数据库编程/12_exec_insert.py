import mysql.connector as mc

conn=mc.connect(user='root',password='182182aA',
                host='localhost',port='3306',
                database='python',use_unicode=True)
c=conn.cursor()
c.execute('insert into user_tb values(null,%s,%s,%s)',
            ('孙悟空','123456','male'))
c.execute('insert into order_tb values(null,%s,%s,%s,%s)',
            ('鼠标','34.2','3','1'))
conn.commit()
c.close()
conn.close()