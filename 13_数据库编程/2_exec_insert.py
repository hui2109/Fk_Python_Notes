import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

conn=sqlite3.connect('sqlite_databases/first.db')
c=conn.cursor()
c.execute('insert into user_tb values (null,?,?,?)',
        ('孙悟空','123456','male'))
c.execute('insert into order_tb values (null,?,?,?,?)',
        ('鼠标','34.2','3',1))
conn.commit()
c.close()
conn.close()