from tkinter import *
import front_end.admin_panel

class aboutus:
    def __init__(self,root):
        self.wn=root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('665x500')

        heading = Label(self.wn, text=' About Us', bg='light green', font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

        developer = Label(self.wn, text=' Project of Introduction to Algorithms \n completed by:- Deep Raj Singh \n'
                                        ' Batch:- 27E \n CUID:- 10269648', font=('arial', 15, 'bold'))
        developer.place(x=150,y=150)

        self.btn_back = Button(self.wn, text='< BACK', font=('arial', 10, 'bold'), width=10, height=1, fg="white", bd=2,
                               bg='green', command=self.back)
        self.btn_back.place(x=20, y=40)

    def back(self):
        log_window = Tk()
        front_end.admin_panel.mainpage(log_window)
        self.wn.destroy()
