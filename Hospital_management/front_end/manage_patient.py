from tkinter import *
from tkinter import ttk
from model.model import*
from back_end.connection import*
from front_end import admin_panel
from tkinter import messagebox

class Patient:
    def __init__(self, root):
        self.wn = root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('1350x700+0+0')

#======================connection object==========
        self.dbconnect=dbconnection()

# ==========================================all variable====================================================
        self.patient_id = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.address = StringVar()
        self.problem = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

# ==========================================heading=========================================================
        heading = Label(self.wn, text=' MANAGE _ PATIENT', bg='green', fg="white", font=('arial', 20, 'bold'))
        heading.pack(side=TOP, fill=X)

# ==========================================frame in window================================================
        frame1 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame1.place(x=20, y=70, width=450, height=590)

        m_title = Label(frame1, text='Patient Details', font=('arial', 20, 'bold'), bg='light green')
        m_title.grid(row=0, columnspan=2, pady=20)

        frame2 = Frame(self.wn, bd=4, relief=RIDGE, bg='light green')
        frame2.place(x=480, y=70, width=840, height=590)

        btn_frame = Frame(frame1, bd=4, relief=RIDGE, bg='light green')
        btn_frame.place(x=10, y=500, width=420)

        table_frame = Frame(frame2, bd=4, relief=RIDGE, bg='light green')
        table_frame.place(x=15, y=70, width=800, height=490)

# =========================================widgets in frame1 ==============================================
        lbl_id = Label(frame1, text='PATIENT_ID: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_id.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.ent_id = Entry(frame1, textvariable=self.patient_id, font=('arial', 14, 'bold'), bd=3)
        self.ent_id.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lbl_name = Label(frame1, text='NAME: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_name.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.ent_name = Entry(frame1, textvariable=self.name, font=('arial', 14, 'bold'), bd=3)
        self.ent_name.grid(row=2, column=1, padx=10, pady=10, sticky='w')

        lbl_age = Label(frame1, text='AGE:', font=('arial', 14, 'bold'), bg='light green')
        lbl_age.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.ent_age = Entry(frame1, textvariable=self.age, font=('arial', 14, 'bold'), bd=3)
        self.ent_age.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        lbl_gender = Label(frame1, text='GENDER: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_gender.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.combo_gender = ttk.Combobox(frame1, font=('arial', 13, 'bold'), textvariable=self.gender,
                                      state='readonly')
        self.combo_gender['values'] = ("male", "female", "other")
        self.combo_gender.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        lbl_contact = Label(frame1, text='CONTACT:', font=('arial', 14, 'bold'), bg='light green')
        lbl_contact.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.ent_contact = Entry(frame1, textvariable=self.contact, font=('arial', 14, 'bold'), bd=3)
        self.ent_contact.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        lbl_address = Label(frame1, text='ADDRESS: ', font=('arial', 14, 'bold'), bg='light green')
        lbl_address.grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.ent_address = Entry(frame1, textvariable=self.address, font=('arial', 14, 'bold'), bd=3)
        self.ent_address.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        lbl_problem = Label(frame1, text='PROBLEM:', font=('arial', 14, 'bold'), bg='light green')
        lbl_problem.grid(row=7, column=0, padx=10, pady=10, sticky='w')
        self.ent_problem = Entry(frame1,textvariable = self.problem,font=('arial', 14, 'bold'),bd=3)
        self.ent_problem.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# ========================================button in button frame==========================================
        btn_add = Button(btn_frame, text='ADD', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white'
                         ,command=self.add)
        btn_add.grid(row=0, column=0, padx=10, pady=8)

        btn_update = Button(btn_frame, text='UPDATE', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white'
                            ,command=self.update)
        btn_update.grid(row=0, column=1, padx=10, pady=8)

        btn_reset = Button(btn_frame, text='RESET', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white'
                           ,command=self.reset)
        btn_reset.grid(row=0, column=2, padx=10, pady=8)

        btn_del = Button(btn_frame, text='DELETE', font=('arial', 10, 'bold'), width=9, bd=2, bg='green', fg='white'
                        , command=self.delete)
        btn_del.grid(row=0, column=3, padx=10, pady=8)

# =========================================wediget in frame2===============================================
        lbl_search = Label(frame2, text="Search By", font=('arial', 14, 'bold'), bg='light green')
        lbl_search.grid(row=0, column=0, padx=10, pady=10)
        self.combo_search = ttk.Combobox(frame2, textvariable=self.search_by, font=('arial', 11, 'bold'), width=11,
                                         state='readonly')
        self.combo_search['values'] = ("patient_id")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)

        self.ent_search = Entry(frame2, textvariable=self.search_text, font=('arial', 12, 'bold'), bd=3)
        self.ent_search.grid(row=0, column=2, padx=10, pady=10)
        btn_search = Button(frame2, text='SEARCH', font=('arial', 11, 'bold'), width=9, bd=2, bg='green', fg='white',
                            command=self.searching)
        btn_search.grid(row=0, column=3, padx=10, pady=10)

        btn_show_all = Button(frame2, text='SHOW ALL', font=('arial', 11, 'bold'), width=9, bd=2, bg='green',
                              fg='white',command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=10, pady=10)

# ======================back button============================================================================
        btn_back = Button(self.wn, text='< BACK', font=('arial', 10, 'bold'), width=10, height=1, fg="white", bd=2,
                          bg='green', command=self.btn_back)
        btn_back.place(x=20, y=40)

# ============================table in table_frame=========================================================
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.patient_table = ttk.Treeview(table_frame, columns=(
        "patient_id", "name", "age", "gender", "contact", "address", "problem"), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.patient_table.xview)
        scroll_y.config(command=self.patient_table.yview)
        self.patient_table.heading("patient_id", text="Patient_Id")
        self.patient_table.heading("name", text="Name")
        self.patient_table.heading("age", text="Age")
        self.patient_table.heading("gender", text="Gender")
        self.patient_table.heading("contact", text="Contact")
        self.patient_table.heading("address", text="Address")
        self.patient_table.heading("problem", text="Problem")
        self.patient_table['show'] = 'headings'
        self.patient_table.pack()
        self.patient_table.column("patient_id", width=60)
        self.patient_table.column("name", width=150)
        self.patient_table.column("age", width=50)
        self.patient_table.column("gender", width=75)
        self.patient_table.column("contact", width=110)
        self.patient_table.column("address", width=150)
        self.patient_table.column("problem", width=200)
        self.patient_table.pack(fill=BOTH, expand=1)
        self.patient_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add(self):
        if self.ent_id.get() == '' or self.ent_name.get() == '' or self.ent_age.get() == '' \
                or self.combo_gender.get() == '' or self.ent_contact.get() == '' or self.ent_address.get() == '' \
                or self.ent_address.get() == '' or self.ent_problem.get() == '':
            messagebox.showerror("Error","every entry must be filed")
        else:
            obj= patient(self.ent_id.get(),self.ent_name.get(),self.ent_age.get(),self.combo_gender.get(),
                         self.ent_contact.get(),self.ent_address.get(),
                         self.ent_problem.get())
            query='insert into patient_detail values (%s,%s,%s,%s,%s,%s,%s);'
            values=(obj.get_patient_id(),obj.get_name(),obj.get_age(),obj.get_gender(),obj.get_contact(),
                    obj.get_address(),obj.get_problem())
            self.dbconnect.insert(query,values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data inserted successfully")

    def update(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Invalid id for update")
        else:
            obj = patient(self.ent_id.get(), self.ent_name.get(), self.ent_age.get(), self.combo_gender.get(),
                          self.ent_contact.get(), self.ent_address.get(),self.ent_problem.get())
            query='update patient_detail set name=%s,age=%s,gender=%s,contact=%s,address=%s,problem=%s' \
                  ' where patient_id=%s;'
            values = (obj.get_name(), obj.get_age(), obj.get_gender(), obj.get_contact(),obj.get_address(),
                      obj.get_problem(),obj.get_patient_id())
            self.dbconnect.insert(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data updated successfully")

    def reset(self):
        if self.ent_id.get() == '' and self.ent_name.get() == '' and self.ent_age.get() == '' \
                and self.combo_gender.get() == '' and self.ent_contact.get() == '' and self.ent_address.get() == '' \
                and self.ent_address.get() == '' and self.ent_problem.get() == '':
            messagebox.showerror("Error","Nothing to reset here")
        else:
            self.patient_id.set("")
            self.name.set("")
            self.age.set("")
            self.gender.set("")
            self.contact.set("")
            self.address.set("")
            self.problem.set("")

    def delete(self):
        if self.ent_id.get() == '':
            messagebox.showerror("Error","Invalid id for delete")
        else:
            obj = patient(self.ent_id.get(), self.ent_name.get(), self.ent_age.get(), self.combo_gender.get(),
                          self.ent_contact.get(), self.ent_address.get(),
                          self.ent_problem.get())
            query = 'delete from patient_detail where patient_id=%s;'
            values = (obj.get_patient_id(),)
            self.dbconnect.delete(query, values)
            self.fetch_data()
            self.reset()
            messagebox.showinfo("success", "data deleted successfully")

    def searching(self):
        ent = self.ent_search.get() and self.combo_search.get()
        if ent != "":
            try:
                self.lis = []
                for i in self.patient_table.get_children():
                    a = self.patient_table.item(i)['values'][0]
                    self.lis.append(a)
                search = self.linearsearch(self.lis, self.ent_search.get())
                if search:
                    query = "select * from patient_detail where patient_id = %s"
                    values = (search,)
                    a = self.dbconnect.select1(query,values)
                    self.patient_table.delete(*self.patient_table.get_children())
                    for i in a:
                        self.patient_table.insert('', END, values=i)
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
        query='select * from patient_detail;'
        rows= self.dbconnect.select(query)
        self.search_text.set("")
        if rows!=0:
            self.patient_table.delete(*self.patient_table.get_children())
            for row in rows:
                self.patient_table.insert('', END, values=row)

    def get_cursor(self, eve):
        cursor_row = self.patient_table.focus()
        contents = self.patient_table.item(cursor_row)
        row = contents['values']
        self.patient_id.set(row[0])
        self.name.set(row[1])
        self.age.set(row[2])
        self.gender.set(row[3])
        self.contact.set(row[4])
        self.address.set(row[5])
        self.problem.set(row[6])

    def btn_back(self):
        abcd_window=Tk()
        admin_panel.mainpage(abcd_window)
        self.wn.destroy()

# root = Tk()
# Patient(root)
# root.mainloop()
