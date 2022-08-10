import mysql.connector as mc

conn=mc.connect(user='root',password='182182aA',
                host='localhost',port='3306',
                database='python',use_unicode=True)
c=conn.cursor()
c.executemany('insert into user_tb values(null,%s,%s,%s)',
            [
                ('sun','123456','male'),
                ('bai','123456','female'),
                ('zhu','123456','male'),
                ('niu','123456','male'),
                ('tang','123456','male')
            ])
conn.commit()
c.close()
conn.close()