from tkinter import *
from tkinter import ttk
from model.model import*
from back_end.connection import*
from front_end import admin_panel
from tkinter import messagebox


class Doctor:
    def __init__(self, root):
        self.wn = root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('1350x700+0+0')

        # ======================connection object==========
        self.dbconnect = dbconnection()

        self.doctor_id = StringVar()
        self.name = StringVar()
        self.time = StringVar()
        self.specialties = StringVar()
        self.qualification = StringVar()
        self.contact = StringVar()
        self.address = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

# ==========================================heading=========================================================
        heading = Label(self.wn, text=' MANAGE  DOCTOR', bg='green', fg="white", font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# ==========================================frame in window================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame1.place(x=20, y=70, width=450, height=590)

        m_title = Label(frame1, text='Doctor Details', font=('arial', 20, 'bold'), bg='light green')
        m_title.grid(row=0, columnspan=2, pady=20)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame2.place(x=480, y=70, width=840, height=590)

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg='light green')
        btn_frame.place(x=10, y=500, width=420)

        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='light green')
        table_frame.place(x=15, y=70, width=800, height=490)

# =========================================widgets in frame1 ==============================================
        lbl_id = Label(frame1, text='DOCTOR_ID: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_id.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.ent_id = Entry(frame1,textvariable=self.doctor_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_id.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_name = Label(frame1, text='NAME: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_name.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.ent_name = Entry(frame1,textvariable=self.name, font=('arial', 14, 'bold'), bd=3)
        self.ent_name.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_time = Label(frame1, text='AVAILABLE TIME:', font=('arial', 14, 'bold'), bg='light green')
        lbl_time.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.ent_time = Entry(frame1, textvariable=self.time,font=('arial', 14, 'bold'), bd=3)
        self.ent_time.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_spec = Label(frame1, text='SPECIALTIES: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_spec.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.ent_spec = Entry(frame1,textvariable=self.specialties, font=('arial', 14, 'bold'), bd=3)
        self.ent_spec.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_quali = Label(frame1, text='QUALIFICATION:', font=('arial', 14, 'bold'), bg='light green')
        lbl_quali.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.ent_quali =Entry(frame1,textvariable=self.qualification,font=('arial', 14, 'bold'),bd=3)
        self.ent_quali.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_contact = Label(frame1, text='CONTACT:', font=('arial', 14, 'bold'), bg='light green')
        lbl_contact.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.ent_contact = Entry(frame1, textvariable=self.contact,font=('arial', 14, 'bold'), bd=3)
        self.ent_contact.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_address = Label(frame1, text='ADDRESS: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_address.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.ent_address = Entry(frame1, textvariable=self.address,font=('arial', 14, 'bold'), bd=3)
        self.ent_address.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# ========================================button in button frame==========================================
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

# =========================================wediget in frame2===============================================
        lbl_search = Label(frame2, text="Search By", font=('arial', 14, 'bold'), bg='light green')
        lbl_search.grid(row=0, column=0, padx=10, pady=10)
        self.combo_search = ttk.Combobox(frame2, font=('arial', 11, 'bold'), width=11,
                                         state='readonly')
        self.combo_search['values'] = ("doctor_id")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.ent_search = Entry(frame2, textvariable=self.search_text, font=('arial', 12, 'bold'), bd=3)
        self.ent_search.grid(row=0, column=2, padx=10, pady=10)
        btn_search = Button(frame2, text='SEARCH', font=('arial', 11, 'bold'), width=9, bd=2, bg='green', fg='white',
                            command = self.searching)
        btn_search.grid(row=0, column=3, padx=10, pady=10)

        btn_show_all = Button(frame2, text='SHOW ALL', font=('arial', 11, 'bold'), width=9, bd=2, bg='green',fg='white',
                              command = self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=10, pady=10)

# ======================back button============================================================================
        btn_back = Button(self.wn, text='< BACK', font=('arial', 10, 'bold'), width=10, height=1, fg="white", bd=2,
                          bg='green', command=self.btn_back)
        btn_back.place(x=20, y=40)

# ============================table in table_frame=========================================================
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.doctor_table = ttk.Treeview(table_frame, columns=(
        "doctor_id", "name", "time","specialties","qualification","contact", "address", ), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.doctor_table.xview)
        scroll_y.config(command=self.doctor_table.yview)
        self.doctor_table.heading("doctor_id", text="Doctor_Id")
        self.doctor_table.heading("name", text="Name")
        self.doctor_table.heading("time", text="Available Time")
        self.doctor_table.heading("specialties", text="Specialties")
        self.doctor_table.heading("qualification", text="Qualification")
        self.doctor_table.heading("contact", text="Contact")
        self.doctor_table.heading("address", text="Address")
        self.doctor_table['show'] = 'headings'
        self.doctor_table.pack()
        self.doctor_table.column("doctor_id", width=60)
        self.doctor_table.column("name", width=150)
        self.doctor_table.column("time", width=100)
        self.doctor_table.column("specialties", width=125)
        self.doctor_table.column("qualification", width=110)
        self.doctor_table.column("contact", width=110)
        self.doctor_table.column("address", width=140)
        self.doctor_table.pack(fill=BOTH, expand=1)
        self.doctor_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add(self):
        if self.ent_id.get() == '' or self.ent_name.get() == '' or self.ent_time.get() == '' \
                or self.ent_spec.get() == '' or self.ent_quali.get() == '' or self.ent_contact.get() == '' \
                or self.ent_address.get() == '' or self.ent_time.get() == '':
            messagebox.showerror("Error","every entry must be filed")
        else:
            obj= doctor(self.ent_id.get(),self.ent_name.get(),self.ent_time.get(),self.ent_spec.get(),
                        self.ent_quali.get(),self.ent_contact.get(),self.ent_address.get())
            query='insert into doctor_detail values (%s,%s,%s,%s,%s,%s,%s);'
            values=(obj.get_doctor_id(),obj.get_name(),obj.get_time(),obj.get_specialties(),obj.get_qualification(),
                    obj.get_contact(),obj.get_address())
            self.dbconnect.insert(query,values)
            self.fetch_data()
            self.reset()
            messagebox.show("success", "data inserted successfully")

    def update(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Invalid id for update")
        else:
            obj = doctor(self.ent_id.get(),self.ent_name.get(),self.ent_time.get(),self.ent_spec.get(),
                         self.ent_quali.get(),self.ent_contact.get(),self.ent_address.get())
            query = 'update doctor_detail set name=%s,time=%s,specialties=%s,qualification=%s,contact=%s,address=%s' \
                    ' where doctor_id=%s;'
            values = (obj.get_name(),obj.get_time(),obj.get_specialties(),obj.get_qualification(),
                      obj.get_contact(),obj.get_address(),obj.get_doctor_id())
            self.dbconnect.insert(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data updated successfully")

    def reset(self):
        if self.ent_id.get() == '' and self.ent_name.get() == '' and self.ent_time.get() == '' \
                and self.ent_spec.get() == '' and self.ent_quali.get() == '' and self.ent_contact.get() == '' \
                and self.ent_address.get() == '' and self.ent_time.get() == '':
            messagebox.showerror("Error","Nothing to reset here")
        else:
            self.doctor_id.set("")
            self.name.set("")
            self.time.set("")
            self.specialties.set("")
            self.qualification.set("")
            self.contact.set("")
            self.address.set("")

    def delete(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Not avilable in list")
        else:
            obj = doctor(self.ent_id.get(), self.ent_name.get(), self.ent_time.get(), self.ent_spec.get(),
                         self.ent_quali.get(),self.ent_contact.get(), self.ent_address.get())
            query = 'delete from doctor_detail where doctor_id=%s;'
            values = (obj.get_doctor_id(),)
            self.dbconnect.delete(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data deleted successfully")

    def searching(self):
        ent = self.ent_search.get() and self.combo_search.get()
        if ent != "":
            try:
                self.lis = []
                for i in self.doctor_table.get_children():
                    a = self.doctor_table.item(i)['values'][0]
                    self.lis.append(a)
                search = self.linearsearch(self.lis, self.ent_search.get())
                if search:
                    query = "select * from doctor_detail where doctor_id = %s"
                    values = (search,)
                    a = self.dbconnect.select1(query,values)
                    self.doctor_table.delete(*self.doctor_table.get_children())
                    for i in a:
                        self.doctor_table.insert('', END, values=i)
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
        query='select * from doctor_detail;'
        rows= self.dbconnect.select(query)
        self.search_text.set("")
        if rows!=0:
            self.doctor_table.delete(*self.doctor_table.get_children())
            for row in rows:
                self.doctor_table.insert('', END, values=row)

    def get_cursor(self, eve):
        cursor_row = self.doctor_table.focus()
        contents = self.doctor_table.item(cursor_row)
        row = contents['values']
        self.doctor_id.set(row[0])
        self.name.set(row[1])
        self.time.set(row[2])
        self.specialties.set(row[3])
        self.qualification.set(row[4])
        self.contact.set(row[5])
        self.address.set(row[6])

    def btn_back(self):
        abc_window = Tk()
        admin_panel.mainpage(abc_window)
        self.wn.destroy()


# root = Tk()
# # Doctor(root)
# # root.mainloop()