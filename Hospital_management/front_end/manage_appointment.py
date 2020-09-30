from tkinter import *
from tkinter import ttk
from model.model import*
from back_end.connection import*
from front_end import admin_panel
from tkinter import messagebox

class Appointment:
    def __init__(self, root):
        self.wn = root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('1350x700+0+0')

# ==============================================connection object=======================================================
        self.dbconnect = dbconnection()

#================================================all variables==========================================================
        self.appointment_id=StringVar()
        self.doctor_id = StringVar()
        self.patient_id = StringVar()
        self.doctor_name = StringVar()
        self.patient_name = StringVar()
        self.date = StringVar()
        self.time = StringVar()
        self.room_no = StringVar()
        self.search_by = StringVar()
        self.search_text = StringVar()

# ==================================================heading=============================================================
        heading = Label(self.wn, text=' MANAGE  APPOINTMENT ', bg='green', fg="white", font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# =================================================frame in window======================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame1.place(x=20, y=70, width=450, height=590)

        m_title = Label(frame1, text='Appointment Details', font=('arial', 20, 'bold'), bg='light green')
        m_title.grid(row=0, columnspan=2, pady=20)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame2.place(x=480, y=70, width=840, height=590)

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg='light green')
        btn_frame.place(x=10, y=500, width=420)

        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='light green')
        table_frame.place(x=15, y=70, width=800, height=490)

# ==================================================widgets in frame1 ==================================================
        lbl_apid = Label(frame1, text='APP. ID: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_apid.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.ent_apid = Entry(frame1, textvariable=self.appointment_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_apid.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_room = Label(frame1, text='ROOM NO: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_room.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.ent_room = Entry(frame1, textvariable=self.room_no, font=('arial', 14, 'bold'), bd=3)
        self.ent_room.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_did = Label(frame1, text='DOCTOR ID: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_did.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.ent_did = Entry(frame1,textvariable=self.doctor_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_did.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_dname = Label(frame1, text='DOCTOR NAME: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_dname.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.ent_dname = Entry(frame1, textvariable=self.doctor_name, font=('arial', 14, 'bold'), bd=3)
        self.ent_dname.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_pid = Label(frame1, text='PATIENT ID: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_pid.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.ent_pid = Entry(frame1, textvariable=self.patient_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_pid.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_Pname = Label(frame1, text='PATIENT NAME: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_Pname.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.ent_Pname = Entry(frame1, textvariable=self.patient_name, font=('arial', 14, 'bold'), bd=3)
        self.ent_Pname.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_date = Label(frame1, text='APP. DATE(Y-M-D):', font=('arial', 13, 'bold'), bg='light green')
        lbl_date.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.ent_date = Entry(frame1, textvariable=self.date, font=('arial', 14, 'bold'), bd=3)
        self.ent_date.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        lbl_time = Label(frame1, text='APP. TIME::', font=('arial', 14, 'bold'), bg='light green')
        lbl_time.grid(row=8, column=0, padx=10, pady=10, sticky='w')
        self.ent_time = Entry(frame1, textvariable=self.time,font=('arial', 14, 'bold'), bd=3)
        self.ent_time.grid(row=8, column=1, padx=10, pady=10, sticky='w')

# ===============================================button in button frame=================================================
        btn_add = Button(btn_frame, text='ADD', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white',
                         command=self.add)
        btn_add.grid(row=0, column=0, padx=10, pady=8)

        btn_update = Button(btn_frame, text='UPDATE', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white',
                            command=self.update)
        btn_update.grid(row=0, column=1, padx=10, pady=8)

        btn_reset = Button(btn_frame, text='RESET', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white',
                           command=self.reset)
        btn_reset.grid(row=0, column=2, padx=10, pady=8)

        btn_del = Button(btn_frame, text='DELETE', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white',
                         command=self.delete)
        btn_del.grid(row=0, column=3, padx=10, pady=8)

# ==================================================widget in frame2====================================================
        lbl_search = Label(frame2, text="Search By", font=('arial', 14, 'bold'), bg='light green')
        lbl_search.grid(row=0, column=0, padx=10, pady=10)
        self.combo_search = ttk.Combobox(frame2, font=('arial', 11, 'bold'), width=11,
                                         state='readonly')
        self.combo_search['values'] = ("appointment_id")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.ent_search = Entry(frame2,textvariable=self.search_text, font=('arial', 12, 'bold'), bd=3)
        self.ent_search.grid(row=0, column=2, padx=10, pady=10)
        btn_search = Button(frame2, text='SEARCH', font=('arial', 11, 'bold'), width=9, bd=2, bg='green', fg='white',
                            command= self.searching)
        btn_search.grid(row=0, column=3, padx=10, pady=10)

        btn_show_all = Button(frame2, text='SHOW ALL', font=('arial', 11, 'bold'), width=9, bd=2, bg='green',fg='white',
                              command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=10, pady=10)

# ====================================================back button=======================================================
        btn_back = Button(self.wn, text='< BACK', font=('arial', 10, 'bold'), width=10, height=1, fg="white", bd=2,
                          bg='green', command=self.btn_back)
        btn_back.place(x=20, y=40)

# ================================================table in table_frame==================================================
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.appointment_table = ttk.Treeview(table_frame, columns=(
        "appointment_id","room_no","doctor_id", "doctor_name", "patient_id","patient_name","date","time" ),
                                              xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.appointment_table.xview)
        scroll_y.config(command=self.appointment_table.yview)
        self.appointment_table.heading("appointment_id", text="APP. ID")
        self.appointment_table.heading("room_no", text="ROOM NO.")
        self.appointment_table.heading("doctor_id", text="DOCTOR ID")
        self.appointment_table.heading("doctor_name", text="DOCTOR NAME")
        self.appointment_table.heading("patient_id", text="PATIENT ID")
        self.appointment_table.heading("patient_name", text="PATIENT NAME")
        self.appointment_table.heading("date", text="DATE")
        self.appointment_table.heading("time", text="TIME")
        self.appointment_table['show'] = 'headings'
        self.appointment_table.pack()
        self.appointment_table.column("appointment_id", width=60)
        self.appointment_table.column("room_no", width=90)
        self.appointment_table.column("doctor_id", width=75)
        self.appointment_table.column("doctor_name", width=150)
        self.appointment_table.column("patient_id", width=75)
        self.appointment_table.column("patient_name", width=150)
        self.appointment_table.column("date", width=75)
        self.appointment_table.column("time", width=75)
        self.appointment_table.pack(fill=BOTH, expand=1)
        self.appointment_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add(self):
        if self.ent_apid.get() == '' or self.ent_room.get() == '' or self.ent_did.get() == '' \
                or self.ent_dname.get() == '' or self.ent_pid.get() == '' or self.ent_Pname.get() == '' \
                or self.ent_date.get() == '' or self.ent_time.get() == '':
            messagebox.showerror("Error","every entry must be filed")
        else:
            obj= appointment(self.ent_apid.get(),self.ent_room.get(),self.ent_did.get(),self.ent_dname.get(),
                             self.ent_pid.get(),self.ent_Pname.get(),self.ent_date.get(),self.ent_time.get())
            query='insert into appointment_detail values (%s,%s,%s,%s,%s,%s,%s,%s);'
            values=(obj.get_appointment_id(),obj.get_room_no(),obj.get_doctor_id(),obj.get_doctor_name(),
                    obj.get_patient_id(),obj.get_patient_name(),obj.get_date(),obj.get_time())
            self.dbconnect.insert(query,values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data inserted successfully")

    def update(self):
        if self.ent_apid.get() == '':
            messagebox.showerror("Error","Invalid id for update here")
        else:
            obj = appointment(self.ent_apid.get(),self.ent_room.get(), self.ent_did.get(), self.ent_dname.get(),
                              self.ent_pid.get(),self.ent_Pname.get(),self.ent_date.get(), self.ent_time.get())
            query = 'update appointment_detail set room_no=%s, doctor_id=%s, doctor_name=%s, patient_id=%s, ' \
                    'patient_name=%s, date=%s,time=%s where appointment_id=%s;'
            values = (obj.get_room_no(), obj.get_doctor_id(), obj.get_doctor_name(), obj.get_patient_id(),
                      obj.get_patient_name(),obj.get_date(), obj.get_time(),obj.get_appointment_id())
            self.dbconnect.insert(query, values)
            if obj==values:
                print ('a')
            else:
                self.fetch_data()
                self.reset()
                messagebox.showinfo("success", "data updated successfully")

    def reset(self):
        if self.ent_apid.get() == '' and self.ent_room.get() == '' and self.ent_did.get() == '' \
                and self.ent_dname.get() == '' and self.ent_pid.get() == '' and self.ent_Pname.get() == '' \
                and self.ent_date.get() == '' and self.ent_time.get() == '':
            messagebox.showerror("Error","Nothing to reset here")
        else:
            self.appointment_id.set("")
            self.room_no.set("")
            self.doctor_id.set("")
            self.doctor_name.set("")
            self.patient_id.set("")
            self.patient_name.set("")
            self.date.set("")
            self.time.set("")

    def delete(self):
        if self.ent_apid.get() == '':
            messagebox.showerror("Error","Nothing to delete here")
        else:
            obj = appointment(self.ent_apid.get(),self.ent_room.get(), self.ent_did.get(), self.ent_dname.get(),
                              self.ent_pid.get(),self.ent_Pname.get(), self.ent_date.get(), self.ent_time.get())
            query = 'delete from appointment_detail where appointment_id=%s;'
            values = (obj.get_appointment_id(),)
            self.dbconnect.delete(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data deleted successfully")



    def searching(self):
        ent = self.ent_search.get() and self.combo_search.get()
        if ent != "":
            try:
                self.lis = []
                for i in self.appointment_table.get_children():
                    a = self.appointment_table.item(i)['values'][0]
                    self.lis.append(a)
                search = self.linearsearch(self.lis, self.ent_search.get())
                if search:
                    query = "select * from appointment_detail where appointment_id = %s"
                    values = (search,)
                    a = self.dbconnect.select1(query,values)
                    self.appointment_table.delete(*self.appointment_table.get_children())
                    for i in a:
                        self.appointment_table.insert('', END, values=i)
                    messagebox.showinfo("Success", "Found")

                else:
                    messagebox.showerror("failed", "Error, Not found")

            except BaseException as m:
                print(m)
                messagebox.showerror("Not Found", "Error, Not found")
        else:
            messagebox.showerror("Failed","'Search' and 'search by:' must by filled")

    def linearsearch(self, lis, x):
        for i in range(len(lis)):
            if int(lis[i]) == int(x):
                return lis[i]
        return False

    def fetch_data(self):
        query='select * from appointment_detail;'
        rows= self.dbconnect.select(query)
        self.search_text.set("")
        if rows!=0:
            self.appointment_table.delete(*self.appointment_table.get_children())
            for row in rows:
                self.appointment_table.insert('', END, values=row)

    def get_cursor(self, eve):
        cursor_row = self.appointment_table.focus()
        contents = self.appointment_table.item(cursor_row)
        row = contents['values']
        self.appointment_id.set(row[0])
        self.room_no.set(row[1])
        self.doctor_id.set(row[2])
        self.doctor_name.set(row[3])
        self.patient_id.set(row[4])
        self.patient_name.set(row[5])
        self.date.set(row[6])
        self.time.set(row[7])

    def btn_back(self):
        ab_window = Tk()
        admin_panel.mainpage(ab_window)
        self.wn.destroy()


# root = Tk()
# Appointment(root)
# root.mainloop()