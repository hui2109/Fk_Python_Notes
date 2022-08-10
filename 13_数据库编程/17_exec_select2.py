import mysql.connector as mc

conn=mc.connect(user='root',password='182182aA',
                host='localhost',port='3306',
                database='python',use_unicode=True)
c=conn.cursor()
c.execute('select * from user_tb where user_id>%s',
            (2,))
for col in c.description:
    print(col[0],end='\t')

print('\n--------------------------------')

while True:
    rows=c.fetchmany(3)
    if not rows:
        break
    for i in rows:
        print(i)
# conn.commit()
c.close()
conn.close()