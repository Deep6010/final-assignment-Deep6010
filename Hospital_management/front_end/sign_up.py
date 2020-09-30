from tkinter import *
from model.model import*
from back_end.connection import*
import front_end.admin_panel
from tkinter import messagebox

class signup:
    def __init__(self,root):
        self.wn=root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('665x500')

        # ======================connection object==========
        self.dbconnect = dbconnection()

        self.name=StringVar
        self.password=StringVar

        #==========heading=============
        heading = Label(self.wn,text=' Sign Up For New User',bg='light green',font=('arial',20,'bold'))
        heading.pack(side=TOP,fill=X)

        #=========widgets=============
        lbl_uname = Label(self.wn,text='USER NAME', font=('arial', 20, 'bold'))
        lbl_uname.place(x=240,y=95)
        self.ent_uname = Entry(self.wn,bd=3,textvariable=self.name)
        self.ent_uname.place(x=240,y=145,width=160,height=30)

        lbl_upass = Label(self.wn, text='PASSWORD', font=('arial', 20, 'bold'))
        lbl_upass.place(x=240, y=225)
        self.ent_upass = Entry(self.wn,bd=3,textvariable=self.password)
        self.ent_upass.place(x=240, y=275, width=160, height=30)

        #==========button=========
        btn_sign_up = Button(self.wn, text='SAVE', font=('arial', 10, 'bold'),width= 12,height =2,bd=3,bg='light green',
                             command=self.conform_btn)
        btn_sign_up.place(x=170, y=350)

        btn_exit = Button(self.wn, text=' EXIT ', font=('arial', 10, 'bold'), width=12, height=2, bd=3,bg='light green',
                          command=self.exit_btn)
        btn_exit.place(x=370, y=350)

        self.btn_back = Button(self.wn, text='< BACK', font=('arial', 10, 'bold'), width=10, height=1, fg="white", bd=2,
                          bg='green',command = self.back)
        self.btn_back.place(x=20, y=40)

    def back(self):
        log_window = Tk()
        front_end.admin_panel.mainpage(log_window)
        self.wn.destroy()

    def exit_btn(self):
        self.wn.destroy()

    def conform_btn(self):
        if self.ent_uname.get() == '' or self.ent_upass.get() == '':
            messagebox.showerror("Error", "User_Name and Password must be needed")
        else:
            obj = user(self.ent_uname.get(), self.ent_upass.get())
            query = 'insert into login values (%s,%s);'
            values = (obj.get_name(), obj.get_password())
            self.dbconnect.insert(query, values)
            messagebox.showinfo("success","new user are added successfully")





