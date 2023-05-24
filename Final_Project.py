from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math,subprocess
import smtplib
import sqlite3



class MyProject:
    def __init__(self, master):
        self.tf = Frame(master, background='cyan', bd=14, relief=RIDGE)
        self.tf.pack(side=TOP, fill=BOTH, expand='true')
        self.logo = PhotoImage(file='img/logo2.png')
        self.history = PhotoImage(file='img/history2.png')
        self.place = PhotoImage(file='img/order.png')
        self.label = Label(self.tf, image=self.logo)
        self.label.place(x=10, y=10)
        self.label2 = Label(self.tf, text='Welcome to Kings Restaurant! ', font=(
            'Arial', 18, 'bold'), bg='cyan')
        self.label2.place(x=325, y=40)

        self.logo2 = PhotoImage(file='img/pic4.png')
        self.label3 = Label(self.tf, image=self.logo2)
        self.label3.place(x=10, y=120)
        self.logo3 = PhotoImage(file='img/pic2.png')
        self.label3 = Label(self.tf, image=self.logo3)
        self.label3.place(x=10, y=350)

        self.button = Button(self.tf, text=" Employee Login", font=(
            'Arial', 12, 'bold'), command=self.mLogin)
        self.button2 = Button(self.tf, text=" Register", font=(
            'Algerian', 12, 'bold'), command=self.mRegister)
        self.button.place(x=375, y=250)
        self.button2.place(x=610, y=250)

        self.label4 = Label(self.tf, text='''Punalkulam, near Thanjavur ''',
                            font=('Courier', 12), bg='cyan', anchor=W)
        self.label4.place(x=325, y=400)
        self.label5 = Label(self.tf, text="Address", font=(
            'Courier', 12), bg='cyan', anchor=NW)
        self.label5.place(x=325, y=375)
        self.l6 = Label(self.tf, text="Contact No\n9150510835",
                        font=('Courier', 12), bg='cyan', justify=LEFT)
        self.l6.place(x=325, y=460)

        self.p4 = PhotoImage(file='img/admin2.png')
        self.label7 = Label(self.tf, image=self.p4)
        self.label7.place(x=400, y=150)

        self.p5 = PhotoImage(file='img/register2.png')
        self.label8 = Label(self.tf, image=self.p5)
        self.label8.place(x=600, y=150)

        self.p6 = PhotoImage(file='img/home2.png')
        self.label9 = Label(self.tf, image=self.p6)
        self.label9.place(x=330, y=340)

        self.p7 = PhotoImage(file='img/phone2.png')
        self.label10 = Label(self.tf, image=self.p7)
        self.label10.place(x=330, y=435)


    def mLogin(self):
        root1 = Toplevel()
        root1.title("Management Login")
        root1.wm_geometry("700x500")
        login = MLogin(root1, self.logo, self.history, self.place)

    def mRegister(self):
        root1 = Toplevel()
        root1.title("Register")
        root1.wm_geometry("700x700")

        page = MyPage(root1, self.logo)




class MyPage:
    def __init__(self, master, logo):
        self.m = master
        self.frame1 = Frame(master, background='cyan', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')

        self.logo = PhotoImage(file='img/logo2.png')
        self.label = Label(self.frame1, image=logo)
        self.label.place(x=10, y=10)
        self.label2 = Label(self.frame1, text='Registration Form ', font=('Courier', 18, 'bold'),
                            bg='cyan')
        self.label2.place(x=200, y=40)
        self.label_1 = Label(self.frame1, text="Name",
                             font=('Courier', 14), bg='cyan')
        self.label_1.place(x=25, y=130)
        self.entry_1 = Entry(self.frame1, width=40)
        self.entry_1.place(x=250, y=130)
    
        self.label_2 = Label(self.frame1, text="Password",
                             font=('Courier', 14), bg='cyan')
        self.label_2.place(x=25, y=180)
        self.entry_2 = Entry(self.frame1, width=40, show='*')
        self.entry_2.place(x=250, y=180)

        self.label_3 = Label(self.frame1, text="Contact No.",
                             font=('Courier', 14), bg='cyan')
        self.label_3.place(x=25, y=230)
        self.entry_3 = Entry(self.frame1, width=40)
        self.entry_3.place(x=250, y=230)

        self.label_4 = Label(self.frame1, text="Email ID",
                             font=('Courier', 14), bg='cyan')
        self.label_4.place(x=25, y=280)
        self.entry_4 = Entry(self.frame1, width=40)
        self.entry_4.place(x=250, y=280)

        self.label_5 = Label(self.frame1, text="Date of birth",
                             font=('Courier', 14), bg='cyan')
        self.label_5.place(x=25, y=330)
        self.label_6 = Label(self.frame1, text="Address",
                             font=('Courier', 14), bg='cyan')
        self.label_6.place(x=25, y=380)
        self.entry_6 = Entry(self.frame1, width=40)
        self.entry_6.place(x=250, y=380)

        self.date = StringVar()
        self.s1 = Spinbox(self.frame1, from_=1, to=31,
                          textvariable=self.date, width=10)
        self.s1.place(x=250, y=330)

        self.month = StringVar()
        self.s2 = Spinbox(self.frame1, from_=1, to=12,
                          textvariable=self.month, width=10)
        self.s2.place(x=340, y=330)

        self.year = StringVar()
        self.s3 = Spinbox(self.frame1, from_=1950, to=2000,
                          textvariable=self.year, width=10)
        self.s3.place(x=440, y=330)

        self.b1 = Button(self.frame1, text=" Submit", font=(
            'Algerian', 12, 'bold'), command=self.submit)
        self.b1.place(x=100, y=500)

        self.b2 = Button(self.frame1, text=" Reset", font=(
            'Algerian', 12, 'bold'), command=self.reset)
        self.b2.place(x=250, y=500)

        self.b3 = Button(self.frame1, text=" Back", font=(
            'Algerian', 12, 'bold'), command=self.back)
        self.b3.place(x=400, y=500)

    def submit(self):
        if self.entry_1.get() == "" or self.entry_2.get() == "" or self.entry_3.get() == "" or self.entry_4.get() == "" or self.entry_6.get() == "":
            messagebox.showerror(
                parent=self.m, title="Error", message="Fill all fields")

        elif len(self.entry_3.get()) != 10:
            messagebox.showerror(parent=self.m, title="Error",
                                 message="Enter valid contact number")
        elif (str(self.entry_4.get()).endswith(".com") == False and str(self.entry_4.get()).endswith(".in") == False and str(self.entry_4.get()).endswith(".co.in") == False)\
                or str(self.entry_4.get()).rfind("@") == -1:
            messagebox.showerror(parent=self.m, title="Error",
                                 message="Enter valid email id")

        else:
            ans = messagebox.askyesno(
                parent=self.m, message="Do you want to submit?", title="Confirmation")
            if ans > 0:

                conn = sqlite3.connect("db/database1.db")

                # Generation of emp_id
                cursor = conn.execute("select * from emp_det")
                value = cursor.fetchall()
                leng = len(value)
                print(leng)
                emp_id = value[leng - 1][0] + 1
                name = self.entry_1.get()
                emp_no = int(self.entry_3.get())
                emp_add = self.entry_6.get()
                date = self.date.get()
                month = self.month.get()
                year = self.year.get()
                emp_dob = str(date)+"-"+str(month)+"-"+str(year)
                emp_email = self.entry_4.get()
                emp_password = self.entry_2.get()

                try:
                    cursor = conn.execute(
                        "select * from emp_det where emp_name='" + name + "' and emp_email='" + emp_email + "' and emp_dob='" + emp_dob + "'")
                    if len(cursor.fetchall()) != 0:
                        raise ExistingException()
                    conn.execute("insert into emp_det values(?,?,?,?,?,?,?)",
                                 (emp_id, name, emp_no, emp_add, emp_dob, emp_email, emp_password))
                    conn.commit()
                    messagebox.showinfo(parent=self.m, message="Successfully added\nEmployee ID is " + str(emp_id),
                                        title="Congratulation!!")

                except Exception as e:
                    print(e)
                    messagebox.showerror(
                        parent=self.m, message="User already exists. Goto login page", title="Error")

    def reset(self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)
        self.entry_3.delete(0, END)
        self.entry_4.delete(0, END)
        self.entry_6.delete(0, END)
        self.date.set("1")
        self.month.set("1")
        self.year.set("1950")

    def back(self):
        self.m.destroy()


class InvalidUserException(Exception):
    def __init__(self):
        print("Invalid user")


class ExistingException(Exception):
    def __init__(self):
        print("User already exists")


class MLogin:
    def __init__(self, master, logo, history, place):
        self.m = master
        self.history = history
        self.place = place
        self.frame1 = Frame(master, background='cyan', bd=14, relief=RIDGE)
        self.frame1.pack(side=TOP, fill=BOTH, expand='true')
        self.logo = PhotoImage(file='img/logo2.png')
        self.label = Label(self.frame1, image=logo)
        self.label.place(x=10, y=10)
        self.label2 = Label(self.frame1, text='Login Page ', font=('Courier', 18, 'bold'),
                            bg='cyan')
        self.label2.place(x=300, y=40)

        self.label_1 = Label(self.frame1, text="Employee Id: ",
                             font=('Courier', 14), bg='cyan')
        self.label_1.place(x=125, y=150)
        self.entry_1 = Entry(self.frame1, width=40)
        self.entry_1.place(x=260, y=150)
        self.label_2 = Label(self.frame1, text="Password:",
                             font=('Courier', 14), bg='cyan')
        self.label_2.place(x=125, y=210)
        self.entry_2 = Entry(self.frame1, width=40, show="*")
        self.entry_2.place(x=260, y=210)
        self.b1 = Button(self.frame1, text=" Login ", font=(
            'Courier', 12, 'bold'), command=self.success)
        self.b1.place(x=250, y=300)
        self.b2 = Button(self.frame1, text=" Reset ", font=(
            'Courier', 12, 'bold'), command=self.reset)
        self.b2.place(x=350, y=300)
        self.b3 = Button(self.frame1, text=" Back ", font=(
            'Courier', 12, 'bold'), command=self.exit)
        self.b3.place(x=450, y=300)

    def success(self):
        try:
            if (self.entry_1.get() == "" or self.entry_2.get() == ""):
                messagebox.showerror(
                    parent=self.m, message="Please fill all the details", title="Error")

            elif (type(int(self.entry_1.get())) != int):
                pass
            else:
                try:
                    conn = sqlite3.connect("db/database1.db")
                    cursor = conn.execute("select * from emp_det where emp_id='" +
                                          self.entry_1.get()+"' and emp_password='"+self.entry_2.get()+"'")
                    if len(cursor.fetchall()) == 0:
                        raise InvalidUserException
                    root2 = Toplevel()
                    root2.title("Management Services")
                    root2.wm_geometry("700x500")
                    login2 = MServices(
                        root2, self.logo, self.history, self.place)
                except InvalidUserException as e:
                    print(e)
                    messagebox.showerror(
                        parent=self.m, message="Invalid credentials", title="Error")

        except ValueError as e:
            messagebox.showerror(
                parent=self.m, message="Employee ID must be a number", title="Error")

        except Exception as e:
            messagebox.showerror(
                parent=self.m, message="Invalid credentials", title="Error")

    def reset(self):
        self.entry_1.delete(0, END)
        self.entry_2.delete(0, END)

    def exit(self):
        self.m.destroy()


class MServices:
    def __init__(self, master, logo, history, place):
        self.logo = logo
        self.frame1 = Frame(master, height=500, width=600, bd=14)
        self.frame1.config(background='cyan')
        self.frame1.pack(fill=BOTH, expand='true')
        self.label1 = Label(self.frame1, image=logo)
        self.label1.place(x=10, y=10)

        self.label0 = Label(self.frame1, text='Management Services', font=(
            'Courier', 20, 'bold'), bg='cyan')
        self.label0.place(x=200, y=30)
        #
        #
        self.label2 = Label(self.frame1, image=history)
        self.label2.place(x=75, y=180)

        self.label3 = Label(self.frame1, image=place)
        self.label3.place(x=330, y=170)

        self.button1 = Button(self.frame1, text='History', font=(
            'Courier', 14), command=self.history)
        self.button1.place(x=120, y=350)

        self.button2 = Button(self.frame1, text='Place Order', font=(
            'Courier', 14), command=self.place_order)
        self.button2.place(x=350, y=350)

    def place_order(self):
        root1 = Toplevel()
        root1.title("Place order")
        root1.wm_geometry("1200x700")
        po = PlaceOrder(root1, self.logo)

    def history(self):
        root1 = Toplevel()
        root1.title("History")
        root1.wm_geometry("1000x500")
        hi = History(root1, self.logo)


class PlaceOrder():
    def __init__(self, master, logo):
        self.m = master

        self.tf = Frame(master, height=100, width=900, bd=14, relief=RIDGE)
        self.tf.pack(fill=BOTH, expand='true', side=TOP)
        self.tf.config(background='cyan')

        self.lf = Frame(master, height=600, width=400, bd=14, relief=RIDGE)
        self.lf.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf.config(background='cyan')

        self.lf1 = Frame(master, height=600, width=400, bd=14, relief=RIDGE)
        self.lf1.pack(fill=BOTH, expand='true', side=LEFT)
        self.lf1.config(background='cyan')

        self.lf2 = Frame(self.lf1, height=250, width=400, bd=14, relief=RIDGE)
        self.lf2.pack(fill=BOTH, expand='true', side=TOP)
        self.lf2.config(background='cyan')

        self.lf3 = Frame(self.lf1, height=350, width=400, bd=14, relief=RIDGE)
        self.lf3.pack(fill=BOTH, expand='true', side=BOTTOM)
        self.lf3.config(background='cyan')

        self.rf = Frame(master, height=600, width=400, bd=14, relief=RIDGE)
        self.rf.pack(fill=BOTH, expand='true', side=RIGHT)
        self.rf.config(background='cyan')

        self.label = Label(self.tf, image=logo)
        self.label.grid(row=0, column=0, rowspan=2, sticky=NW)
        self.label2 = Label(self.tf, text='Order placement of Kings Restaurant', font=('Courier', 20, 'bold'),
                            bg='cyan', anchor=E)
        self.label2.grid(row=1, column=1, columnspan=5)
        # Labels of Meal

        self.m1 = Label(self.lf, text="Meals", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.m1.place(x=25, y=0)

        self.v1 = IntVar()
        self.c1 = Checkbutton(self.lf, text="Veg Kolhapuri", font=(
            'Courier', 11, 'bold'), bg='cyan', variable=self.v1)
        self.c1.place(x=10, y=50)

        self.v2 = IntVar()
        self.c2 = Checkbutton(self.lf, text="Veg Hydrabadi", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v2)
        self.c2.place(x=10, y=100)

        self.v3 = IntVar()
        self.c3 = Checkbutton(self.lf, text="Palak Paneer", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v3)
        self.c3.place(x=10, y=150)

        self.v4 = IntVar()
        self.c4 = Checkbutton(self.lf, text="Veg Kofta", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v4)
        self.c4.place(x=10, y=200)

        self.v5 = IntVar()
        self.c5 = Checkbutton(self.lf, text="Paneer Tikka", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v5)
        self.c5.place(x=10, y=250)

        self.v6 = IntVar()
        self.c6 = Checkbutton(self.lf, text="Butter Roti", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v6)
        self.c6.place(x=10, y=300)

        self.v7 = IntVar()
        self.c7 = Checkbutton(self.lf, text="Tandoori Roti", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v7)
        self.c7.place(x=10, y=350)

        self.v8 = IntVar()
        self.c8 = Checkbutton(self.lf, text="Daal Rice", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v8)
        self.c8.place(x=10, y=400)

        self.v9 = IntVar()
        self.c9 = Checkbutton(self.lf, text="Veg Pulav", font=('Courier', 11, 'bold'), bg='cyan',
                              variable=self.v9)
        self.c9.place(x=10, y=450)

        self.v10 = IntVar()
        self.c10 = Checkbutton(self.lf, text="Veg Biryani", font=('Courier', 11, 'bold'), bg='cyan',
                               variable=self.v10)
        self.c10.place(x=10, y=500)

        # Quantity of meals

        self.m2 = Label(self.lf, text="Quantity", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.m2.place(x=170, y=0)

        self.sv1 = StringVar()
        self.s1 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv1, width=4)
        self.s1.place(x=170, y=50)

        self.sv2 = StringVar()
        self.s2 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv2, width=4)
        self.s2.place(x=170, y=100)

        self.sv3 = StringVar()
        self.s3 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv3, width=4)
        self.s3.place(x=170, y=150)

        self.sv4 = StringVar()
        self.s4 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv4, width=4)
        self.s4.place(x=170, y=200)

        self.sv5 = StringVar()
        self.s5 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv5, width=4)
        self.s5.place(x=170, y=250)

        self.sv6 = StringVar()
        self.s6 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv6, width=4)
        self.s6.place(x=170, y=300)

        self.sv7 = StringVar()
        self.s7 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv7, width=4)
        self.s7.place(x=170, y=350)

        self.sv8 = StringVar()
        self.s8 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv8, width=4)
        self.s8.place(x=170, y=400)

        self.sv9 = StringVar()
        self.s9 = Spinbox(self.lf, from_=1, to=100,
                          textvariable=self.sv9, width=4)
        self.s9.place(x=170, y=450)

        self.sv10 = StringVar()
        self.s10 = Spinbox(self.lf, from_=1, to=100,
                           textvariable=self.sv10, width=4)
        self.s10.place(x=170, y=500)

        self.m3 = Label(self.lf, text="Price", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.m3.place(x=300, y=0)

        self.ml1 = Label(self.lf, text="180", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml1.place(x=300, y=50)

        self.ml2 = Label(self.lf, text="170", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml2.place(x=300, y=100)

        self.ml3 = Label(self.lf, text="140", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml3.place(x=300, y=150)

        self.ml4 = Label(self.lf, text="190", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml4.place(x=300, y=200)

        self.ml5 = Label(self.lf, text="210", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml5.place(x=300, y=250)

        self.ml6 = Label(self.lf, text="18", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml6.place(x=300, y=300)

        self.ml7 = Label(self.lf, text="12", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml7.place(x=300, y=350)

        self.ml8 = Label(self.lf, text="80", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml8.place(x=300, y=400)

        self.ml9 = Label(self.lf, text="140", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml9.place(x=300, y=450)

        self.ml10 = Label(self.lf, text="180", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.ml10.place(x=300, y=500)

        # ------------------------------------------------------------------------------------

        # Labels of Drink

        self.d1 = Label(self.lf1, text="Drinks", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d1.place(x=50, y=20)

        self.vd1 = IntVar()
        self.cd1 = Checkbutton(self.lf1, text="Tea", font=('Courier', 11, 'bold'), bg='cyan',
                               variable=self.vd1)
        self.cd1.place(x=20, y=50)

        self.vd2 = IntVar()
        self.cd2 = Checkbutton(self.lf1, text="Coffee", font=('Courier', 11, 'bold'), bg='cyan',
                               variable=self.vd2)
        self.cd2.place(x=20, y=100)

        self.vd3 = IntVar()
        self.cd3 = Checkbutton(self.lf1, text="Coca cola", font=('Courier', 11, 'bold'), bg='cyan',
                               variable=self.vd3)
        self.cd3.place(x=20, y=150)

        self.vd4 = IntVar()
        self.cd4 = Checkbutton(self.lf1, text="Slice", font=('Courier', 11, 'bold'), bg='cyan',
                               variable=self.vd4)
        self.cd4.place(x=20, y=200)

        # Quantity of drinks

        self.d2 = Label(self.lf1, text="Quantity", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d2.place(x=170, y=20)

        self.svd1 = StringVar()
        self.sd1 = Spinbox(self.lf1, from_=1, to=100,
                           textvariable=self.svd1, width=4)
        self.sd1.place(x=170, y=50)

        self.svd2 = StringVar()
        self.sd2 = Spinbox(self.lf1, from_=1, to=100,
                           textvariable=self.svd2, width=4)
        self.sd2.place(x=170, y=100)

        self.svd3 = StringVar()
        self.sd3 = Spinbox(self.lf1, from_=1, to=100,
                           textvariable=self.svd3, width=4)
        self.sd3.place(x=170, y=150)

        self.svd4 = StringVar()
        self.sd4 = Spinbox(self.lf1, from_=1, to=100,
                           textvariable=self.svd4, width=4)
        self.sd4.place(x=170, y=200)
        self.d3 = Label(self.lf1, text="Price", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d3.place(x=300, y=20)

        self.dl1 = Label(self.lf1, text="25", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.dl1.place(x=300, y=50)

        self.dl2 = Label(self.lf1, text="35", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.dl2.place(x=300, y=100)

        self.dl3 = Label(self.lf1, text="40", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.dl3.place(x=300, y=150)

        self.dl4 = Label(self.lf1, text="60", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.dl4.place(x=300, y=200)
        # ---------------------------------------------------------------------------

        # Labels of Dessert

        self.d_1 = Label(self.lf3, text="Dessert", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d_1.place(x=40, y=20)

        self.vd_1 = IntVar()
        self.cd_1 = Checkbutton(self.lf3, text="Vanilla Gelato", font=('Courier', 11, 'bold'), bg='cyan',
                                variable=self.vd_1)
        self.cd_1.place(x=10, y=50)

        self.vd_2 = IntVar()
        self.cd_2 = Checkbutton(self.lf3, text="Banana Split", font=('Courier', 11, 'bold'), bg='cyan',
                                variable=self.vd_2)
        self.cd_2.place(x=10, y=100)

        self.vd_3 = IntVar()
        self.cd_3 = Checkbutton(self.lf3, text="Apple pie", font=('Courier', 11, 'bold'), bg='cyan',
                                variable=self.vd_3)
        self.cd_3.place(x=10, y=150)

        self.vd_4 = IntVar()
        self.cd_4 = Checkbutton(self.lf3, text="Sundae", font=('Courier', 11, 'bold'), bg='cyan',
                                variable=self.vd_4)
        self.cd_4.place(x=10, y=200)

        # Quantity of dessert

        self.d_2 = Label(self.lf3, text="Quantity", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d_2.place(x=160, y=20)

        self.svd_1 = StringVar()
        self.sd_1 = Spinbox(self.lf3, from_=1, to=100,
                            textvariable=self.svd_1, width=4)
        self.sd_1.place(x=170, y=50)

        self.svd_2 = StringVar()
        self.sd_2 = Spinbox(self.lf3, from_=1, to=100,
                            textvariable=self.svd_2, width=4)
        self.sd_2.place(x=170, y=100)

        self.svd_3 = StringVar()
        self.sd_3 = Spinbox(self.lf3, from_=1, to=100,
                            textvariable=self.svd_3, width=4)
        self.sd_3.place(x=170, y=150)

        self.svd_4 = StringVar()
        self.sd_4 = Spinbox(self.lf3, from_=1, to=100,
                            textvariable=self.svd_4, width=4)
        self.sd_4.place(x=170, y=200)

        self.d_3 = Label(self.lf3, text="Price", font=(
            'Courier', 16, 'bold'), bg='cyan', justify="center")
        self.d_3.place(x=290, y=20)

        self.d_l1 = Label(self.lf3, text="100", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.d_l1.place(x=300, y=50)

        self.d_l2 = Label(self.lf3, text="80", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.d_l2.place(x=300, y=100)

        self.d_l3 = Label(self.lf3, text="120", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.d_l3.place(x=300, y=150)

        self.d_l4 = Label(self.lf3, text="100", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.d_l4.place(x=300, y=200)
        # Customer details
        self.cl1 = Label(self.rf, text="Customer details",
                         font=('Courier', 18, 'bold'), bg='cyan')
        self.cl1.place(x=50, y=10)
        self.cl2 = Label(self.rf, text="Name", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.cl2.place(x=10, y=40)
        self.ce1 = Entry(self.rf, width=35)
        self.ce1.place(x=110, y=40)

        self.cl3 = Label(self.rf, text="Address", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.cl3.place(x=10, y=90)
        self.ce2 = Text(self.rf, width=25, height=5)
        self.ce2.place(x=110, y=90)

        self.cl4 = Label(self.rf, text="Email Address.", font=(
            'Courier', 11, 'bold'), bg='cyan')
        self.cl4.place(x=10, y=190)
        self.ce3 = Entry(self.rf)
        self.ce3.place(x=110, y=190)

        self.b_cd = Button(self.rf, text="Calculate bill", font=(
            'Courier', 11, 'bold'), command=self.cal_bill)
        self.b_cd.place(x=10, y=250)

        self.b_cd1 = Button(self.rf, text="Submit", font=(
            'Courier', 11, 'bold'), command=self.submit)
        self.b_cd1.place(x=170, y=250)

        self.b_cd2 = Button(self.rf, text="Back", font=(
            'Courier', 11, 'bold'), command=self.back)
        self.b_cd2.place(x=270, y=250)


        def EmailSending(self):

            # self.withdraw()



            responce = messagebox.askquestion("EmailSending","Do You want the Bill to your email")

            if responce == 1:
                subprocess.call(["python",r"D:\Python\MiniProject\HotelManagemetn\hotel-management-system\SmtpLib.py"])
            else:
                subprocess.call(["python",r"D:\Python\MiniProject\HotelManagemetn\hotel-management-system\SmtpLib.py"])
    


        self.email = Button(self.rf,text = "Email",font=('Courier', 11, 'bold'),command = lambda:EmailSending(self))
        self.email.place(x=350,y=250)


    def cal_bill(self):
        price = 0.0
        gst = 0.0
        self.t1 = Text(self.rf, width=40, height=15)
        self.t1.place(x=10, y=290)
        # self.scrollbar = ttk.Scrollbar(self.t1, orient=VERTICAL, command=self.t1.yview)
        # self.t1.config(yscrollcommand=self.scrollbar.set)

        self.t1.insert(END, "Kings Restaurant\n")
        self.t1.insert(END, "Punalkulam near Thanjavur.\n")
        self.t1.insert(END, "Contact no:9150510835\n\n")
        self.t1.insert(END, "Customer details\n")
        self.t1.insert(END, self.ce1.get()+"\n")
        self.t1.insert(END, self.ce2.get('1.0', END))
        self.t1.insert(END, self.ce3.get()+"\n")

        self.t1.insert(END, "\t\tReceipt \n")
        self.t1.insert(END, " Item name\t\t Quantity\t\t Price\n")

        m_price = [180, 170, 140, 190, 210, 18, 12, 80, 140, 180]
        if(self.v1.get() == 1):
            self.t1.insert(END, ""+self.c1.cget("text")+"\t\t  " +
                           self.s1.get()+"\t\t  "+str(int(self.s1.get())*m_price[0])+"\n")
            price = price+int(self.s1.get()) * m_price[0]

        if (self.v2.get() == 1):
            self.t1.insert(END, "" + self.c2.cget("text") + "\t\t  " + self.s2.get() + "\t\t  " + str(
                int(self.s2.get()) * m_price[1])+"\n")
            price = price + int(self.s2.get()) * m_price[1]

        if (self.v3.get() == 1):
            self.t1.insert(END, "" + self.c3.cget("text") + "\t\t  " + self.s3.get() + "\t\t  " + str(
                int(self.s3.get()) * m_price[2])+"\n")
            price = price + int(self.s3.get()) * m_price[2]

        if (self.v4.get() == 1):
            self.t1.insert(END, "" + self.c4.cget("text") + "\t\t  " + self.s4.get() + "\t\t  " + str(
                int(self.s4.get()) * m_price[3])+"\n")
            price = price + int(self.s4.get()) * m_price[3]

        if (self.v5.get() == 1):
            self.t1.insert(END, "" + self.c5.cget("text") + "\t\t  " + self.s5.get() + "\t\t  " + str(
                int(self.s5.get()) * m_price[4])+"\n")
            price = price + int(self.s5.get()) * m_price[4]

        if (self.v6.get() == 1):
            self.t1.insert(END, "" + self.c6.cget("text") + "\t\t  " + self.s6.get() + "\t\t  " + str(
                int(self.s6.get()) * m_price[5])+"\n")
            price = price + int(self.s6.get()) * m_price[5]

        if (self.v7.get() == 1):
            self.t1.insert(END, "" + self.c7.cget("text") + "\t\t  " + self.s7.get() + "\t\t  " + str(
                int(self.s7.get()) * m_price[6])+"\n")
            price = price + int(self.s7.get()) * m_price[6]

        if (self.v8.get() == 1):
            self.t1.insert(END, "" + self.c8.cget("text") + "\t\t  " + self.s8.get() + "\t\t  " + str(
                int(self.s8.get()) * m_price[7])+"\n")
            price = price + int(self.s8.get()) * m_price[7]

        if (self.v9.get() == 1):
            self.t1.insert(END, "" + self.c9.cget("text") + "\t\t  " + self.s9.get() + "\t\t  " + str(
                int(self.s9.get()) * m_price[8])+"\n")
            price = price + int(self.s9.get()) * m_price[8]

        if (self.v10.get() == 1):
            self.t1.insert(END, "" + self.c10.cget("text") + "\t\t  " + self.s10.get() + "\t\t  " + str(
                int(self.s10.get()) * m_price[9])+"\n")
            price = price + int(self.s10.get()) * m_price[9]

        # Drinks
        d_price = [25, 35, 40, 60]
        if (self.vd1.get() == 1):
            self.t1.insert(END, "" + self.cd1.cget("text") + "\t\t  " + self.svd1.get() + "\t\t  " + str(
                int(self.svd1.get()) * d_price[0]) + "\n")
            price = price+int(self.svd1.get()) * d_price[0]

        if (self.vd2.get() == 1):
            self.t1.insert(END, "" + self.cd2.cget("text") + "\t\t  " + self.svd2.get() + "\t\t  " + str(
                int(self.svd2.get()) * d_price[1]) + "\n")
            price = price + int(self.svd2.get()) * d_price[1]

        if (self.vd3.get() == 1):
            self.t1.insert(END, "" + self.cd3.cget("text") + "\t\t  " + self.svd3.get() + "\t\t  " + str(
                int(self.svd3.get()) * d_price[2]) + "\n")
            price = price + int(self.svd3.get()) * d_price[2]

        if (self.vd4.get() == 1):
            self.t1.insert(END, "" + self.cd4.cget("text") + "\t\t  " + self.svd4.get() + "\t\t  " + str(
                int(self.svd4.get()) * d_price[3]) + "\n")
            price = price + int(self.svd3.get()) * d_price[3]

        # Desert
        de_price = [100, 80, 120, 100]
        if (self.vd_1.get() == 1):
            self.t1.insert(END, "" + self.cd_1.cget("text") + "\t\t  " + self.svd_1.get() + "\t\t  " + str(
                int(self.svd_1.get()) * de_price[0]) + "\n")
            price = price+int(self.svd_1.get()) * de_price[0]

        if (self.vd_2.get() == 1):
            self.t1.insert(END, "" + self.cd_2.cget("text") + "\t\t  " + self.svd_2.get() + "\t\t  " + str(
                int(self.svd_2.get()) * de_price[1]) + "\n")
            price = price + int(self.svd_2.get()) * de_price[3]

        if (self.vd_3.get() == 1):
            self.t1.insert(END, "" + self.cd_3.cget("text") + "\t\t  " + self.svd_3.get() + "\t\t  " + str(
                int(self.svd_3.get()) * de_price[2]) + "\n")
            price = price + int(self.svd_3.get()) * de_price[3]

        if (self.vd_4.get() == 1):
            self.t1.insert(END, "" + self.cd_4.cget("text") + "\t\t  " + self.svd_4.get() + "\t\t  " + str(
                int(self.svd_4.get()) * de_price[3]) + "\n")
            price = price + int(self.svd_4.get())*de_price[3]

        gst = gst+0.18*price
        self.total = gst+price
        self.t1.insert(
            END, "----------------------------------------\nAmount\t\t\t\t "+str(price)+"\n")
        self.t1.insert(END, "GST\t\t\t\t  "+str(round(gst, 2))+"\n")
        self.t1.insert(
            END, "----------------------------------------\nTotal bill\t\t\t\t "+str(price+gst)+"\n")
        self.t1.config(state="disabled")

    def submit(self):
        if self.ce1.get() == "" or self.ce2.get('1.0', END) == "" or self.ce3.get() == "":
            messagebox.showerror(parent=self.m, title="Error",
                                 message="Enter all fields")

        elif len(self.ce3.get()) == [1,2,3,4,5,6,7,8,9]:
            messagebox.showerror(parent=self.m, title="Error",
                                 message="Enter valid Email Address")
        else:
            ans = messagebox.askyesno(
                parent=self.m, message="Do you want to submit?", title="Confirmation")
            if ans > 0:
                conn = sqlite3.connect("db/database1.db")
                cursor = conn.execute("select * from cust_det")
                value = cursor.fetchall()
                leng = len(value)
                print(leng)
                # Calculation of customer id
                cust_id = value[leng - 1][0] + 1
                cust_name = self.ce1.get()
                cust_no = self.ce3.get()
                cust_add = self.ce2.get('1.0', END)
                conn.execute("insert into cust_det values(?,?,?,?)",
                             (cust_id, cust_name, cust_no, cust_add))
                conn.commit()

                # Calculation of order no
                cursor = conn.execute("select * from history")
                value = cursor.fetchall()
                leng = len(value)
                print(leng)
                order_no = value[leng - 1][0] + 1

                # Creation of item nos
                str1 = ""
                str2 = ""
                if self.v1.get() == 1:
                    str1 = str1 + "1001 "
                    str2 = str2+str(self.s1.get())+" "

                if self.v2.get() == 1:
                    str1 = str1 + "1002 "
                    str2 = str2+str(self.s2.get())+" "

                if self.v3.get() == 1:
                    str1 = str1 + "1003 "
                    str2 = str2+str(self.s3.get())+" "

                if self.v4.get() == 1:
                    str1 = str1 + "1004 "
                    str2 = str2+str(self.s4.get())+" "

                if self.v5.get() == 1:
                    str1 = str1 + "1005 "
                    str2 = str2+str(self.s5.get())+" "

                if self.v6.get() == 1:
                    str1 = str1 + "1006 "
                    str2 = str2+str(self.s6.get())+" "

                if self.v7.get() == 1:
                    str1 = str1 + "1007 "
                    str2 = str2+str(self.s7.get())+" "

                if self.v8.get() == 1:
                    str1 = str1 + "1008 "
                    str2 = str2+str(self.s8.get())+" "

                if self.v9.get() == 1:
                    str1 = str1 + "1009 "
                    str2 = str2+str(self.s9.get())+" "

                if self.v10.get() == 1:
                    str1 = str1 + "1010 "
                    str2 = str2+str(self.s10.get())+" "

                if self.vd1.get() == 1:
                    str1 = str1 + "1011 "
                    str2 = str2+str(self.svd1.get())+" "

                if self.vd2.get() == 1:
                    str1 = str1 + "1012 "
                    str2 = str2+str(self.svd2.get())+" "

                if self.vd3.get() == 1:
                    str1 = str1 + "1013 "
                    str2 = str2+str(self.svd3.get())+" "

                if self.vd4.get() == 1:
                    str1 = str1 + "1014 "
                    str2 = str2+str(self.svd4.get())+" "

                if self.vd_1.get() == 1:
                    str1 = str1 + "1015 "
                    str2 = str2+str(self.svd_1.get())+" "

                if self.vd_2.get() == 1:
                    str1 = str1 + "1016 "
                    str2 = str2+str(self.svd_2.get())+" "

                if self.vd_3.get() == 1:
                    str1 = str1 + "1017 "
                    str2 = str2+str(self.svd_3.get())+" "

                if self.vd_4.get() == 1:
                    str1 = str1 + "1018 "
                    str2 = str2+str(self.svd_4.get())+" "

                conn = sqlite3.connect("db/database1.db")
                conn.execute("insert into history values (?,?,?,?,?)",
                             (order_no, cust_id, str1, str2, self.total))
                conn.commit()
                messagebox.showinfo(parent=self.m, message="Order placed\n Customer ID:"+str(
                    cust_id), title="Kings Restaurant")
                self.reset()

    def back(self):
        self.m.destroy()

    def reset(self):
        self.v1.set(0)
        self.v2.set(0)
        self.v3.set(0)
        self.v4.set(0)
        self.v5.set(0)
        self.v6.set(0)
        self.v7.set(0)
        self.v8.set(0)
        self.v9.set(0)
        self.v10.set(0)
        self.sv1.set(1)
        self.sv2.set(1)
        self.sv3.set(1)
        self.sv4.set(1)
        self.sv5.set(1)
        self.sv6.set(1)
        self.sv7.set(1)
        self.sv8.set(1)
        self.sv9.set(1)
        self.sv10.set(1)
        self.vd1.set(0)
        self.vd2.set(0)
        self.vd3.set(0)
        self.vd4.set(0)
        self.svd1.set(1)
        self.svd2.set(1)
        self.svd3.set(1)
        self.svd4.set(1)
        self.vd_1.set(0)
        self.vd_2.set(0)
        self.vd_3.set(0)
        self.vd_4.set(0)
        self.svd_1.set(1)
        self.svd_2.set(1)
        self.svd_3.set(1)
        self.svd_4.set(1)
        self.ce1.delete(0, END)
        self.ce2.delete('1.0', END)
        self.ce3.delete(0, END)
        self.t1.config(state='normal')
        self.t1.delete('1.0', END)
        self.t1.config(state='disabled')


class History:
    def __init__(self, master, logo):
        self.m = master
        self.frame1 = Frame(master, height=135, width=600, relief=RIDGE, bd=14)
        self.frame1.config(background="cyan")
        self.frame1.pack(side=TOP, fill=BOTH)
        self.frame2 = Frame(master, height=400, width=600,
                            relief=RIDGE, bd=14, background="gray92")
        self.frame2.pack(side=BOTTOM, fill=BOTH, expand="true")
        self.label = Label(self.frame1, image=logo)
        self.label.place(x=10, y=10)
        self.label2 = Label(self.frame1, text='History ', font=('Courier', 18, 'bold'),
                            bg='cyan')
        self.label2.place(x=325, y=40)
        self.l3 = Label(self.frame2, text="Customer ID",
                        font=('Courier', 10, 'bold'), bg="gray92")
        self.l3.place(x=10, y=10)
        self.e1 = Entry(self.frame2)
        self.e1.place(x=120, y=10)
        self.b1 = Button(self.frame2, text="Submit", font=(
            'Courier', 10, 'bold'), command=self.submit)
        self.b1.place(x=250, y=10)

    def submit(self):

        try:
            conn = sqlite3.connect('db/database1.db')
            cursor = conn.execute(
                "select order_no from history where cust_id=" + str(int(self.e1.get())))
            self.t1 = Text(self.frame2, height=18,
                           width=118)

            for i in cursor.fetchone():
                self.t1.insert(END, "Order no" + "\t:" + str(i) + "\n\n")
            cursor = conn.execute(
                "select cust_name,cust_mno,cust_add from cust_det where cust_id=" + str(int(self.e1.get())))
            l1 = ['Customer name', 'Customer EmailAddress', 'Customer Address']
            j = 0
            for i in cursor.fetchone():
                self.t1.insert(END, l1[j] + "\t:" + str(i) + "\n\n")
                j = j + 1
            cursor = conn.execute(
                "select item_nos from history where cust_id=" + str(int(self.e1.get())))
            cursor2 = conn.execute(
                "select quantity from history where cust_id=" + str(int(self.e1.get())))

            self.t1.insert(END, "Items ordered" + "\n\nItem name\t\tQuantity")
            items = (cursor.fetchone())[0]
            q = (cursor2.fetchone())[0]
            j = 0
            for i in items.split():
                i_name = cursor.execute(
                    "select item_name from item_table where item_id=" + str(i))
                self.t1.insert(END, "\n" + str((i_name.fetchone())
                                               [0]) + "\t\t" + str((q.split())[j]))
                j = j + 1
            cursor = conn.execute(
                "select bill from history where cust_id=" + str(int(self.e1.get())))
            bill = (cursor.fetchone())[0]
            self.t1.insert(END, "\n--------------------------------------\n")
            self.t1.insert(END, " Total bill \t\t" + str(bill))
            self.t1.place(x=10, y=35)
            self.t1.config(state="disabled")
        except:
            messagebox.showerror(parent=self.m, title="Error!",
                                 message="Invalid customer ID ")





root = Tk()
root.title("Kings Restaurant")
root.wm_geometry("900x625")
myProject = MyProject(root)
root.mainloop()

