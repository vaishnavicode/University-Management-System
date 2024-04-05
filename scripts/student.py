# Importing the required libraries
from datetime import datetime
from database import Database
import csv


class Student:
    # Constructor to initialize the student
    def __init__(self):
        self.id = id
        self.name = ""
        self.department = ""
        self.email = ""
        self.password = ""
        self.loggedIn = False
        self.db = Database()
    
    def login(self, id, password):
        print(self.db.student_login(id,password))
    

   
student = Student()
student.login()
