import mysql.connector as mc

conn=mc.connect(user='root',password='182182aA',
                host='localhost',port='3306',
                database='python',use_unicode=True)
conn.autocommit=True
c=conn.cursor()
c.executemany('update user_tb set name=%s where user_id=%s',
            [
                ('小孙',2),
                ('小白',3),
                ('小猪',4),
                ('小牛',5),
                ('小唐',6)
            ])
# conn.commit()
c.close()
conn.close()