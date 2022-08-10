import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

def reverse_ext(st):
    return '[' + st[::-1] +']'

conn=sqlite3.connect('sqlite_databases/first.db')
conn.create_function('enc',1,reverse_ext)
c=conn.cursor()
c.execute('insert into user_tb values(null,?,enc(?),?)',
        ['贾宝玉','123456','male'])
conn.commit()
c.close()
conn.close()
