# 导入访问SQLite的模块
import sqlite3
import os

# 更改工作目录
os.chdir(os.path.dirname(__file__))

# ①打开或创建数据库
# 也可以使用特殊名称:memory:，代表创建内存中的数据库
conn=sqlite3.connect('sqlite_databases/first.db')

# ②获取游标
c=conn.cursor()

# ③执行DDL语句创建数据表
c.execute('''
        create table user_tb (
            _id integer primary key autoincrement,
            name text,
            pass text,
            gender text
        )
        ''')
# 执行DDL语句创建数据表
c.execute('''
        create table order_tb (
            _id integer primary key autoincrement,
            item_name text,
            item_price text,
            item_number text,
            user_id integer,
            foreign key (user_id) references user_tb(_id)  
        )
        ''')

# ④关闭游标
c.close()

# ⑤关闭连接
conn.close()
