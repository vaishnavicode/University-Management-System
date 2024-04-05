# Importing the required libraries
from datetime import datetime
from Database import Database
import csv
  
class Student:
    # Constructor to initialize the student
    def __init__(self, student_id, student_name, student_password, student_batch, student_year, student_semester, student_department):
        self.student_id = student_id
        self.student_name = student_name
        self.student_password = student_password
        self.student_batch = student_batch       
        self.student_year = student_year
        self.student_semester = student_semester
        self.student_department = student_department
        
        
        
    # Method to display the student details
    def __str__(self):
        return f'ID: {self.student_id}\nName: {self.student_name}\nBatch: {self.student_batch}\nYear: {self.student_year}\nSemester: {self.student_semester}\nDepartment: {self.student_department}'
    
    # Authenticating the student
    def authenticate(self, stud_id, stud_password):
        status = False
        from Entities.Student import Student
        with open('../all_data/students.csv', mode='r', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for lines in csv_file:
                try:
                    if lines[0] == stud_id and lines[2] == stud_password:
                        status = Student(lines[0], lines[1], lines[2], lines[3])
                        break
                except IndexError:
                    pass
                except Exception:
                    pass

        return status