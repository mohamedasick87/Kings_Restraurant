import sqlite3

conn=sqlite3.connect('db/database1.db')
# conn.execute("create table emp_det\
# ( emp_id int primary key,\
# emp_name varchar(50) not null,\
# emp_no int not null,\
# emp_add varchar(100) not null,\
# emp_dob varchar(50),\
# emp_email varchar(50),\
# emp_password varchar(50)\
# )\
# ")



# cursor=conn.execute("select * from emp_det where emp_email='omkar661998@gmail.com'")
cursor=conn.execute("select * from emp_det")
print(cursor.fetchall())
conn.close()
