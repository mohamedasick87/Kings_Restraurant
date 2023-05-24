import sqlite3 
import smtplib  

conn = sqlite3.connect("db/database1.db")

cursor = conn.cursor()

email = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][2]

Name = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][1]

Bill = cursor.execute("""SELECT * FROM history """).fetchall()[-1][4]

Address = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][3]

customer_id = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][0]


item_no = cursor.execute("""SELECT * FROM history """).fetchall()[-1][2]

item_no_list = item_no.split()

item_Name = list()


for sitem_no in item_no_list:
	item_name = cursor.execute("""SELECT item_name FROM item_table WHERE item_id = %s """ % sitem_no).fetchall()[-1]
	item_Name.append(item_name)


Item_Name_single = [x for x in item_Name]
item1,item2,item3,*item4 = Item_Name_single


conn.commit()



def send_mail(FROM,TO,username,password,SUBJECT,TEXT,HOST,PORT):

	BODY = "\n".join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT," ",TEXT))
	print(BODY)
	server = smtplib.SMTP(HOST,PORT)
	server.starttls()
	server.login(username,password)
	server.sendmail(FROM,TO,BODY)
	server.quit()



username = "kumaresantylerdurden@gmail.com"
password = r"838fe644d513b5c7b877e788504d4974001d6ccd557beb3dabf555e649b1f1ca"
FROM = "kumaresantylerdurden@gmail.com"
HOST = "smtp.gmail.com"
PORT = 587
SUBJECT = "KINGS RESTAURANT"
TEXT = """
Customer details: \nName: %s
Address: %s\n
Your Id for order is: %s
Your Ordered Items are: 
%s
%s
%s 
%s 
\n\nYour Bill is %s
\nThanks for ordering from our KINGS RESTAURANT
\nPlease visit again""" % (Name ,Address,customer_id,*item1,*item2,*item3,item4,Bill) 




send_mail(HOST=HOST,PORT=PORT,SUBJECT=SUBJECT,username=username,password=password,FROM=FROM,TO=email,TEXT=TEXT)

print("Sent Successfully")