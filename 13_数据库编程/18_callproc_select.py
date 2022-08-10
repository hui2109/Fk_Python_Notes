import mysql.connector as mc

conn=mc.connect(user='root',password='182182aA',
                host='localhost',port='3306',
                database='python',use_unicode=True)
c=conn.cursor()
result_args=c.callproc('add_pro',(5,6,0))
print(result_args)
print(result_args[2])
c.close()
conn.close()