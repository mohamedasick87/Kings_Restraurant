import sqlite3 
import smtplib  

conn = sqlite3.connect("db/database1.db")

cursor = conn.cursor()

email = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][2]

Name = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][1]

Bill = cursor.execute("""SELECT * FROM history """).fetchall()[-1][4]

Address = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][3]

customer_id = cursor.execute("""SELECT * FROM cust_det """).fetchall()[-1][0]

conn.commit()



def send_mail(FROM,TO,username,password,SUBJECT,TEXT,HOST,PORT):

	BODY = "\r\n".join((
	"From: %s" % FROM,
	"To: %s" % TO,
	"Subject: %s" % SUBJECT," ",
	TEXT))
	print(BODY)
	server = smtplib.SMTP(HOST,PORT)
	server.starttls()
	server.login(username,password)
	server.sendmail(FROM,TO,BODY)
	server.quit()



username = "kumaresantylerdurden@gmail.com"
password = r"838fe644d513b5c7b877e788504d4974001d6ccd557beb3dabf555e649b1f1ca"
FROM = username
TO = email
HOST = "smtp.gmail.com"
PORT = 587
SUBJECT = "KINGS RESTAURANT"
TEXT = f"Customer details: \n Name: {Name}\nAddress: {Address}\nYour Id for order is: \n{customer_id}\nYour Bill is {Bill} Thanks for ordering from our RESTAURANT Please visit again"




send_mail(HOST=HOST,PORT=PORT,SUBJECT=SUBJECT,username=username,password=password,FROM=FROM,TO=TO,TEXT=TEXT)