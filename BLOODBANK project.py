from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import mysql.connector
import time
from scrolling_area import *
import ttkcalendar
import tkSimpleDialog
con = mysql.connector.connect(host='localhost', user='root', database='bloodapp')  # password if there is password
cursor = con.cursor()

root = Tk()  # window creation
root.geometry("1366x768+0+0")
# menu=Menu(root)
# root.config(menu=menu)
root.title("BLOODBANK application")
root.resizable(0, 0)

class CalendarDialog(tkSimpleDialog.Dialog):
    def body(self,m):
        self.calendar = ttkcalendar.Calendar(m)
        self.calendar.pack()
    def apply(self):
        self.result = self.calendar.selection
"""
submenu=Menu(menu)
menu.add_cascade(label='file',menu=submenu)
"""


def home():
    toolbar = Frame(root, bg='dark red')
    b = Button(toolbar, text='HOME', width=37, command=lambda: home_return(toolbar, frame1))
    b.pack(side=LEFT, padx=2, pady=2)
    # b.place(x=0,y=20)
    b1 = Button(toolbar, text='About Us', width=37, command=lambda: about(frame1, root))
    b1.pack(side=LEFT, padx=2, pady=2)
    """about=StringVar()
    set1=OptionMenu(toolbar,about,"1","2","3")
    set1.configure(text='About',width=28,font=('Arial'))
    set1.pack(side=LEFT, padx=1, pady=1)
    """
    b = Button(toolbar, text='REGISTER', width=37, command=lambda: signup(frame1, root))
    b.pack(side=LEFT, padx=2, pady=2)
    b = Button(toolbar, text='SEARCH DONOR', width=37, command=lambda: search(frame1, root))
    b.pack(side=LEFT, padx=2, pady=2)

    b = Button(toolbar, text='EXIT', width=37, command=lambda: iexit())
    b.pack(side=LEFT, padx=2, pady=2)
    toolbar.pack(side=TOP, fill=X)

    frame1 = Frame(root, width=1366, height=768)
    frame1.pack()
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\blood.jpg'))
    Label(frame1, image=img, width='1366', height='768').place(x=0, y=0)
    Label(frame1, text='WELCOME', bg='light gray', fg='dark red', font=('Yu Gothic', 40, 'bold')).place(x=540, y=0)
    frame1.mainloop()


def home_return(toolbar, frame1):
    toolbar.destroy()
    frame1.destroy()
    home()


def about(frame1, root):
    frame1.destroy()
    frame2 = Frame(root, width=1366, height=668, bg='dark red')
    frame2.place(x=0, y=30)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\about.jpg'))
    Label(frame2, image=img, width='1366', height='668').place(x=0, y=0)
    Label(frame2, text='BLOOD', bg='light gray', fg='dark red', font=('Yu Gothic', 40, 'bold')).place(x=580, y=0)
    img1 = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\Desktop\\about1.jpg'))
    Label(frame2, image=img1, width='1000', height='800').place(x=100, y=0)

    frame2.mainloop()



def signup(frame1, root):
    frame1.destroy()
    frame3 = Frame(root, width=1366, height=668, bg='dark red')
    frame3.place(x=0, y=30)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\blood.jpg'))
    Label(frame3, image=img, width='1366', height='668').place(x=0, y=0)
    Label(frame3, text='REGISTRATION', bg='light gray', fg='dark red', font=('Yu Gothic', 40, 'bold')).place(x=480, y=0)

    name1 = StringVar()
    bloodgroup1 = StringVar()
    bloodgroup1.set('Select blood group')
    date1 = StringVar()
    dob1 = StringVar()
    ph_no1 = IntVar()
    ph_no1.set('')
    email1 = StringVar()
    zipcode1 = IntVar()
    zipcode1.set('')
    address1 = StringVar()

    Label(frame3, width='60', height='32', bg='grey').place(x=480, y=120)

    l1 = Label(frame3, text="Name : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=140)
    e1 = Entry(frame3, bd=5, width=30, text=name1).place(x=650, y=140)

    l2 = Label(frame3, text="Blood group : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=190)
    # e2 = Entry(frame3, bd=5, width=30,text=set1).place(x=650, y=190)
    set1 = OptionMenu(frame3, bloodgroup1, "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
    set1.configure(text='SELECT', width=17, height=1, font=('Arial'), bd=1)
    set1.place(x=650, y=190)
    l3 = Label(frame3, text="Date : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=240)
    e3 = Entry(frame3, bd=5, width=30, text=date1).place(x=650, y=240)
    b = Button(frame3, text='Select', width=8, height=1, command=lambda: getdate(frame3, date1))
    b.place(x=776, y=241)
    l4 = Label(frame3, text="DOB : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=290)
    e4 = Entry(frame3, bd=5, width=30, text=dob1).place(x=650, y=290)


    l5 = Label(frame3, text="Phone No. : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=340)
    e5 = Entry(frame3, bd=5, width=30, text=ph_no1).place(x=650, y=340)

    l6 = Label(frame3, text="E-Mail ID : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=390)
    e6 = Entry(frame3, bd=5, width=30, text=email1).place(x=650, y=390)

    l7 = Label(frame3, text="Zipcode : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=440)
    e7 = Entry(frame3, bd=5, width=30, text=zipcode1).place(x=650, y=440)

    l8 = Label(frame3, text="Address : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=490)
    e8 = Entry(frame3, bd=5, width=30, text=address1).place(x=650, y=490)

    b1 = Button(frame3, text='SUBMIT', bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: retrieve())
    b1.place(x=500, y=540)
    b2 = Button(frame3, text=' RESET ', bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: iresetSignup(frame3))
    b2.place(x=780, y=540)

    def retrieve():
        name = name1.get()
        bloodgroup = bloodgroup1.get()
        date = date1.get()
        dob = dob1.get()
        ph_no = ph_no1.get()
        email = email1.get()
        zipcode = zipcode1.get()
        address = address1.get()
        query = f'insert into data(name,bloodgroup,date,dob,ph_no,email,zipcode,address)values("{name}","{bloodgroup}","{date}","{dob}","{ph_no}","{email}","{zipcode}","{address}")'
        cursor.execute(query)
        query = f'commit'
        cursor.execute(query)

        # query2 = f'select *from details'
        # cursor.execute(query2)
        # records = cursor.fetchall()
        q = tkinter.messagebox.showinfo("REGISTERED", "Congratulation.You just Became a DONOR!")
        iresetSignup(frame3)

        """for row in records:
            if row[1] == name and row[3] == email:
                asd=row[0]
        text_area = Text(frame3, width=20, height=20)
        text_area.insert(INSERT, ("your account number is: ", asd))
        text_area.place(x=1000, y=200)
        """

    frame3.mainloop()


def search(frame1, root):
    frame1.destroy()
    frame4 = Frame(root, width=1366, height=768, bg='dark red')
    frame4.place(x=0, y=30)
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Akshay\\PycharmProjects\\Project1\\search1.jpg'))
    l7 = Label(frame4, image=img, width='1366', height='668').place(x=0, y=0)
    Label(frame4, text='SEARCH FOR DONOR', bg='light gray', fg='dark red', font=('Yu Gothic', 30, 'bold')).place(x=460,
                                                                                                                 y=0)

    bloodgroup1 = StringVar()
    bloodgroup1.set('Select blood group')
    zipcode1 = IntVar()
    zipcode1.set('')
    Label(frame4, width='80', height='12', bg='gray').place(x=400, y=220)
    l1 = Label(frame4, text="Blood group : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=230)
    set1 = OptionMenu(frame4, bloodgroup1, "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-")
    set1.configure(text='SELECT', width=17, height=1, font=('Arial'), bd=1)
    set1.place(x=650, y=230)
    l7 = Label(frame4, text="Zipcode : ", font=('arial', 14, 'bold'), bg='black', fg='white').place(x=500, y=290)
    e7 = Entry(frame4, bd=5, width=30, text=zipcode1).place(x=650, y=290)
    b1 = Button(frame4, text='SEARCH', bd=8, bg='black', fg='white', font=('arial', 10, 'bold'),
                command=lambda: searchfn(frame4))
    b1.place(x=650, y=360)

    def searchfn(frame4):
        bloodgroup = bloodgroup1.get()
        zipcode = zipcode1.get()
        query = f'select *from data where bloodgroup="{bloodgroup}" and zipcode="{zipcode}"'
        cursor.execute(query)
        records = cursor.fetchall()
        scrolling_area = Scrolling_Area(frame4, height=290, width=1366)
        scrolling_area.place(x=0, y=400)
        table = Table(scrolling_area.innerframe,["ID", "Name ", "Blood_Group ", "Date ", "Date Of Birth ", "Phone no.", "Email ", "Zipcode","Address "], column_minwidths=[50, 188, 188, 188, 188, 188, 188, 188])
        table.pack(expand=TRUE, fill=X)
        table.on_change_data(scrolling_area.update_viewport)
        for row in records:
            table.insert_row(row)


        """for row in records:
            text_area = Text(frame4, width=80, height=20)
            text_area.insert(INSERT, ("Potential Donors are", row))
            text_area.place(x=400, y=400)
            text_area.config(state=DISABLED)
        """
    frame4.mainloop()


def getdate(frame3,date1):
    cd = CalendarDialog(frame3)
    result = cd.result
    date1.set(result.strftime('%d-%m-%y'))
def iresetSignup(frame3):
    frame3.destroy()
    signup(frame3, root)


def iexit():
    qExit = tkinter.messagebox.askquestion("Quit system", "Do you want to quit?")
    if qExit:
        root.destroy()
        return


home()