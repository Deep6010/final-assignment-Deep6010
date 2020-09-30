import unittest
from back_end.connection import *
class test_patient(unittest.TestCase):
    def setUp(self):
        self.dbconnect=dbconnection()
    def test_insert(self):
        query = 'insert into patient_detail values(%s,%s,%s,%s,%s,%s,%s);'
        values= (3,'Rahul','26','male','9819882545','Madan','Skin problem')
        self.dbconnect.insert(query,values)
        expect=[(3,'Rahul','26','male','9819882545','Madan','Skin problem')]
        actual=self.dbconnect.select('select * from patient_detail where patient_id=3')
        self.assertEqual(expect,actual)
    def test_update(self):
        query = "update patient_detail set name=%s,age=%s,gender=%s,contact=%s,address=%s,problem=%s where patient_id=%s;"
        values=('Rohit','25','male','9817640004','Janakpur','Apandix',1)
        self.dbconnect.update(query,values)
        expect=[(1,'Rohit','25','male','9817640004','Janakpur','Apandix')]
        actual=self.dbconnect.select('select * from patient_detail where Patient_id=1')
        self.assertEqual(expect,actual)
    def test_delete(self):
        query='delete from patient_detail where Patient_id=%s;'
        values=(3,)
        self.dbconnect.delete(query,values)
        expect = []
        actual = self.dbconnect.select('select * from patient_detail where patient_id=3')
        self.assertEqual(expect, actual)
if __name__=="__main__":
    unittest.main()