import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

conn=sqlite3.connect('sqlite_databases/first.db')
c=conn.cursor()
c.executescript('''
        insert into user_tb values(null,'武松','3444','male');
        insert into user_tb values(null,'林冲','44444','male');
        create table item_tb (
            _id integer primary key autoincrement,
            name,
            price
            );
''')
conn.commit()
c.close()
conn.close()