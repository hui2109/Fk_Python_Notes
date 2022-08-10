import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

conn=sqlite3.connect('sqlite_databases/first.db')
c=conn.cursor()
c.execute('select * from user_tb where _id>?',(2,))
print('查询返回的记录数:',c.rowcount)
for col in c.description:
    print(col,end='\t')

print('\n--------------------------------')

while True:
    row=c.fetchone()
    if not row:
        break
    print(row)
    print(row[1]+'-->'+row[2])
c.close()
conn.close()
