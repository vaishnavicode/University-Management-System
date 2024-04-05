# Importing the required libraries
  
class Teacher:
    # Constructor to initialize the student
    def __init__(self, teacher_id, teacher_name, teacher_password, teacher_department):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_password = teacher_password
        self.teacher_department = teacher_department
        
        
        
        
    # Method to display the student details
    def __str__(self):
        return f'ID: {self.student_id}\nName: {self.student_name}\nBatch: {self.student_batch}\nYear: {self.student_year}\nSemester: {self.student_semester}\nDepartment: {self.student_department}'
    