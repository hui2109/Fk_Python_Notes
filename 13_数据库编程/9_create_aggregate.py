import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

class MinLen:
    def __init__(self):
        self.min_len=None
    def step(self,value):
        if self.min_len is None:
            self.min_len=value
            return
        if len(self.min_len)>len(value):
            self.min_len=value
    def finalize(self):
        return self.min_len

conn=sqlite3.connect('sqlite_databases/first.db')
conn.create_aggregate('min_len',1,MinLen)
c=conn.cursor()
c.execute('select min_len(pass) from user_tb')
print(c.fetchone()[0])
# print(c.description)
# print(c.fetchone())
conn.commit()
c.close()
conn.close()