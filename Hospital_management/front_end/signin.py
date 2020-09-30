from tkinter import *
import front_end.sign_up
try:
    import front_end.admin_panel
except ImportError:
    pass
from tkinter import messagebox
import back_end.connection


class login:
    def __init__(self,root):
        self.wn=root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('665x500')

        # ======================connection object==========
        self.dbconnect = back_end.connection.dbconnection()

        #==========heading=============
        heading = Label(self.wn,text=' Hospital Management System',bg='light green',font=('arial',20,'bold'))
        heading.pack(side=TOP,fill=X)

        #=========widgets=============
        lbl_uname = Label(self.wn,text='USER NAME', font=('arial', 20, 'bold'))
        lbl_uname.place(x=240,y=95)

        self.ent_uname = Entry(self.wn,bd=3)
        self.ent_uname.place(x=240,y=145,width=160,height=30)

        lbl_pass = Label(self.wn, text='PASSWORD', font=('arial', 20, 'bold'))
        lbl_pass.place(x=240, y=225)

        self.ent_pass = Entry(self.wn,bd=3,show='*')
        self.ent_pass.place(x=240, y=275, width=160, height=30)

        #==========button=========

        btn_login = Button(self.wn, text='LOGIN', font=('arial', 10, 'bold'),width= 12,height =2,bd=3,bg='light green',
                           command= self.login_click)
        btn_login.place(x=260, y=350)

    def login_click(self):
        if self.ent_uname.get() !='' and self.ent_pass.get()!='':
            query = "select * from login where name = %s and password = %s"
            val  = (self.ent_uname.get(),self.ent_pass.get(),)
            get = self.dbconnect.select1(query,val)
            value = []
            try:
                for i in get[0]:
                    value.append(i)
                if value[1] == self.ent_pass.get():
                    log_window = Tk()
                    front_end.admin_panel.mainpage(log_window)
                    self.wn.destroy()
            except:
                messagebox.showerror("error","Invalid username or password")

        else:
            messagebox.showerror("Empty","Value can not be empty")



def win():
    root = Tk()
    login(root)
    root.mainloop()


if __name__ == '__main__':
  win()