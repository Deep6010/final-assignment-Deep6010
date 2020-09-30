from tkinter import *
from front_end import manage_doctor, manage_patient, manage_appointment, sign_up, about_us

class mainpage:
    def __init__(self,root):
        self.wn=root
        self.wn.title('HOSPITAL MANAGEMENT SYSTEM')
        self.wn.geometry('665x500+0+0')

        #==========heading=============
        heading = Label(self.wn,text=' ADMIN PANEL',bg='light green',font=('arial',20,'bold'))
        heading.pack(side=TOP,fill=X)

        #=========button===============

        btn_sign_up = Button(self.wn, text='ADD NEW USER', font=('arial', 10, 'bold'), width=16, height=2, bd=4,
                             bg='light green', command=self.sign_up)
        btn_sign_up.place(x=510, y=50)

        btn_log_out = Button(self.wn, text='LOG OUT', font=('arial', 10, 'bold'), width=16, height=2, bd=4,
                             bg='light green', command=self.logout)
        btn_log_out.place(x=50, y=50)

        btn_doctor = Button(self.wn, text='DOCTOR', font=('arial', 10, 'bold'), width=15, height=3, bd=3, bg='light green',
                            command=self.man_doctor)
        btn_doctor.place(x=120, y=150)

        btn_patient = Button(self.wn, text='PATIENT', font=('arial', 10, 'bold'), width=15, height=3, bd=3,bg='light green',
                             command=self.man_patient)
        btn_patient.place(x=400, y=150)

        btn_app = Button(self.wn, text='APPOINTMENT', font=('arial', 10, 'bold'), width=15, height=3, bd=3,bg='light green',
                         command=self.man_appointment)
        btn_app.place(x=120, y=330)

        btn_aus = Button(self.wn, text='ABOUT US', font=('arial', 10, 'bold'), width=15, height=3, bd=3,bg='light green',
                         command=self.aboutus)
        btn_aus.place(x=400, y=330)

    def man_doctor(self):
        doctor_window=Tk()
        manage_doctor.Doctor(doctor_window)
        self.wn.destroy()

    def man_patient(self):
        patient_window=Tk()
        manage_patient.Patient(patient_window)
        self.wn.destroy()

    def man_appointment(self):
        app_window = Tk()
        manage_appointment.Appointment(app_window)
        self.wn.destroy()

    def sign_up(self):
        signup_window=Tk()
        sign_up.signup(signup_window)
        self.wn.destroy()
    def aboutus(self):
        about_window=Tk()
        about_us.aboutus(about_window)
        self.wn.destroy()
    def logout(self):
        log_window=Tk()
        import front_end.signin
        front_end.signin.login(log_window)
        self.wn.destroy()

