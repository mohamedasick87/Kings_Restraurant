import sqlite3

conn=sqlite3.connect("db/database1.db")
# conn.execute("create table history\
# (\
# order_no int primary key,\
# cust_id int,\
# item_nos varchar(200),\
# quantity varchar(200),\
# bill number\
# )")

conn.commit()

cursor=conn.execute("select * from history")
print(cursor.fetchall())
