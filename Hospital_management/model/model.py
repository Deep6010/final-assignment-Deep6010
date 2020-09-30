class user:
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

    def set_password(self,password):
        self.password=password
    def get_password(self):
        return self.password

class patient:
    def __init__(self,patient_id,name,age,gender,contact,address,problem):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.gender=gender
        self.contact=contact
        self.address=address
        self.problem=problem

    def set_patient_id(self,patient_id):
        self.patient_id=patient_id
    def get_patient_id(self):
        return self.patient_id

    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age
    def get_age(self):
        return self.age

    def set_gender(self, gender):
        self.gender = gender
    def get_gender(self):
        return self.gender

    def set_contact(self, contact):
        self.contact = contact
    def get_contact(self):
        return self.contact

    def set_address(self, address):
        self.address = address
    def get_address(self):
        return self.address

    def set_problem(self, problem):
        self.problem = problem
    def get_problem(self):
        return self.problem

class doctor:
    def __init__(self,doctor_id,name,time,specialties,qualification,contact,address):
        self.doctor_id=doctor_id
        self.name=name
        self.time=time
        self.specialties=specialties
        self.qualification = qualification
        self.contact=contact
        self.address=address

    def set_doctor_id(self,doctor_id):
        self.doctor_id=doctor_id
    def get_doctor_id(self):
        return self.doctor_id

    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name

    def set_time(self, time):
        self.time = time
    def get_time(self):
        return self.time

    def set_specialties(self, specialties):
        self.specialties = specialties
    def get_specialties(self):
        return self.specialties

    def set_qualification(self, qualification):
        self.qualification = qualification
    def get_qualification(self):
        return self.qualification

    def set_contact(self, contact):
        self.contact = contact
    def get_contact(self):
        return self.contact

    def set_address(self, address):
        self.address = address
    def get_address(self):
        return self.address

class appointment:
    def __init__(self,appointment_id,room_no,doctor_id,doctor_name,patient_id,patient_name,date,time):
        self.appointment_id=appointment_id
        self.room_no=room_no
        self.doctor_id=doctor_id
        self.doctor_name=doctor_name
        self.patient_id=patient_id
        self.patient_name=patient_name
        self.date=date
        self.time=time

    def set_appointment_id(self,appointment_id):
        self.appointment_id = appointment_id
    def get_appointment_id(self):
        return self.appointment_id

    def set_room_no(self,room_no):
        self.room_no = room_no
    def get_room_no(self):
        return self.room_no

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id
    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_name(self, doctor_name):
        self.doctor_name = doctor_name
    def get_doctor_name(self):
        return self.doctor_name

    def set_patient_id(self,patient_id):
        self.patient_id=patient_id
    def get_patient_id(self):
        return self.patient_id

    def set_patient_name(self, patient_name):
        self.patient_name = patient_name
    def get_patient_name(self):
        return self.patient_name

    def set_date(self, date):
        self.date = date
    def get_date(self):
        return self.date

    def set_time(self, time):
        self.time = time
    def get_time(self):
        return self.time
