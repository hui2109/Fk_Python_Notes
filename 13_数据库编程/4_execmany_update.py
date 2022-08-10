import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

conn=sqlite3.connect('sqlite_databases/first.db')
c=conn.cursor()
c.executemany('update user_tb set name=? where _id=?',
            [
                ('小孙',2),
                ('小白',3),
                ('小猪',4),
                ('小牛',5),
                ('小唐',6)
            ])
print('修改的记录数:',c.rowcount)
conn.commit()
c.close()
conn.close()