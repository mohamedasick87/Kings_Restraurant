import sqlite3
conn=sqlite3.connect('db/database1.db')
# conn.execute("create table item_table(item_id int primary key,item_name varchar(50),price int )")
# conn.execute("insert into item_table values(1001,'Veg Kolhapuri',180)")
# conn.commit()
#
# conn.execute("insert into item_table values(1002,'Veg Hydrabadi ',170)")
# conn.commit()
#
# conn.execute("insert into item_table values(1003,'Palak Panner',140)")
# conn.commit()
#
# conn.execute("insert into item_table values(1004,'Veg Kofta',190)")
# conn.commit()
#
# conn.execute("insert into item_table values(1005,'Paneer Tikka',210)")
# conn.commit()
#
# conn.execute("insert into item_table values(1006,'Butter Roti',18)")
# conn.commit()
#
# conn.execute("insert into item_table values(1007,'Tandoori Roti',12)")
# conn.commit()
#
# conn.execute("insert into item_table values(1008,'Daal Rice',80)")
# conn.commit()
#
# conn.execute("insert into item_table values(1009,'Veg Pulav',140)")
# conn.commit()
#
# conn.execute("insert into item_table values(1010,'Veg Biryani',180)")
# conn.commit()
#
# conn.execute("insert into item_table values(1011,'Tea',25)")
# conn.commit()
#
# conn.execute("insert into item_table values(1012,'Coffee',35)")
# conn.commit()
#
# conn.execute("insert into item_table values(1013,'Coca Cola',40)")
# conn.commit()
#
# conn.execute("insert into item_table values(1014,'Slice',60)")
# conn.commit()
#
# conn.execute("insert into item_table values(1015,'Vanilla Gelato',100)")
# conn.commit()
#
# conn.execute("insert into item_table values(1016,'Banana Split',80)")
# conn.commit()
#
# conn.execute("insert into item_table values(1017,'Apple Pie',120)")
# conn.commit()
#
# conn.execute("insert into item_table values(1018,'Sundae',100)")
# conn.commit()
cursor=conn.execute("select * from item_table")
print(cursor.fetchall())
conn.close()