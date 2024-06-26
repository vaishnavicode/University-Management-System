from utils.file_handling import read_csv, write_csv
import re

class Teacher:
    def __init__(self, teacher_data):
        self.id = teacher_data["id"]
        self.name = teacher_data["name"]
        self.department = teacher_data["department"]
        self.email = teacher_data["email"]
        self.password = teacher_data["password"]
        self.students = read_csv("data/students.csv")

    def display_menu(self):
        while True:
            print(f"\nWelcome, {self.name}!")
            print("Teacher Menu:")
            print("1. View Students")
            print("2. Add Student")
            print("3. Remove Student")
            print("4. Add Attendance")
            print("5. Add Marks")
            print("6. Logout")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.view_students()
            elif choice == "2":
                self.add_student()
            elif choice == "3":
                self.remove_student()
            elif choice == "4":
                self.add_attendance()
            elif choice == "5":
                self.add_marks()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
    
    def view_students(self):
        print("\n------ Students ------\n")
        for student in self.students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Email:", student["email"])
            # Convert string of marks to list of dictionaries
            try:
                marks = eval(student["marks"])
            except:
                marks = []
            if(len(marks)==0):
                print("Marks: No marks found")
            else:
                print("-----Marks-----")
                for mark in marks:
                    print(f"{mark['subject']}: {mark['marks']}")
                print("---------------")
            print("Attendance:", student["attendance"])
            print()

    def add_student(self):
        # Read the student data from the CSV file
        students = read_csv("data/students.csv")

        # Prompt the teacher to enter the new student's detail
        student_id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        department = input("Enter the student department: ")
        while True:
            email = input("Enter the student email: ")
            if self.validate_email(email):
                break
            else:
                print("Invalid email. Please try again.")
        while True:
            password = input("Enter the student password: ")
            if self.validate_password(password):
                break
            else:
                print("Invalid password. Should be between 8 to 20 characters, atleast one uppercase, one lowercase, one digit and one special character. Please try again.")

        # Create a dictionary to represent the new student
        student_data = {"id": student_id, "name": name, "department": department, "email": email, "password": password}

        # Add the new student to the list of students
        write_csv("data/students.csv", students + [student_data])
        self.students = read_csv("data/students.csv")


    def remove_student(self):
        # Prompt the teacher to enter the student's ID
        student_id = input("Enter the student ID to remove: ")
        for student in self.students:
            if student["id"] == student_id:
                self.students.remove(student)
                print(f"{student['name']} has been removed.")
                break
        else:
            print("Student not found. Please try again.")
            return

        # Update the list of students in the CSV file
        write_csv("data/students.csv", self.students)
        self.students = read_csv("data/students.csv")

    def add_attendance(self):
        # Prompt the teacher to enter the student's ID and attendance status
        student_id = input("Enter the student ID: ")
        percentage = input("Enter his total attendance in percentage:")

        # Find the student in the teacher's list of students
        for student in self.students:
            if student["id"] == student_id:
                currentStudent = student
                currentStudent["attendance"] = percentage
                print(f"Attendance added for {student['name']}.")
                break
        else:
            print("Student not found. Please try again.")
            return

        # Update the student's attendance in the CSV file
        students = read_csv("data/students.csv")
        for student in students:
            if student["id"] == student_id:
                student["attendance"] = percentage
                break
        
        write_csv("data/students.csv", students)
        self.students = read_csv("data/students.csv")


        
    def add_marks(self):
        # Prompt the teacher to enter the student's ID
        student_id = input("Enter the student ID: ")

        # Find the student in the teacher's list of students
        for student in self.students:
            if student["id"] == student_id:
                currentStudent = student
                # Prompt the teacher to enter the subject and marks
                subject = input("Enter the subject: ")
                marks = input("Enter the marks: ")

                # Create a dictionary to represent the marks
                marks_data = {"subject": subject, "marks": marks}

                # If the student has no marks yet, initialize an empty list
                if not currentStudent["marks"]:
                    currentStudent["marks"] = "[]"

                # Convert the marks string to a list of dictionaries
                marks_list = eval(currentStudent["marks"])

                # Append the new marks to the student's list of marks
                marks_list.append(marks_data)

                # Convert the list of dictionaries back to a string representation
                currentStudent["marks"] = str(marks_list)
                print(f"Marks added for {student['name']}.")
                break
        else:
            print("Student not found. Please try again.")
            return

        # Update the student's marks in the CSV file
        students = read_csv("data/students.csv")
        for student in students:
            if student["id"] == student_id:
                student["marks"] = currentStudent["marks"]
                break

        write_csv("data/students.csv", students)
        self.students = read_csv("data/students.csv")
    
    def validate_email(email):
        """
        Check if the input string is a valid email address.

        Args:
        email (str): The email address to be validated.

        Returns:
        bool: True if the email address is valid, False otherwise.
        """
        # Regular expression pattern for validating email addresses
        pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        
        # Check if the email matches the pattern
        if re.match(pattern, email):
            return True
        else:
            return False
    
    def validate_password(password):
        """
        Check if the input string meets the password criteria.

        Args:
        password (str): The password to be validated.

        Returns:
        bool: True if the password meets the criteria, False otherwise.
        """
        # Check if the password length is between 8 and 20 characters
        if len(password) < 8 or len(password) > 20:
            return False
        
        # Check if the password contains at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            return False
        
        # Check if the password contains at least one lowercase letter
        if not re.search(r'[a-z]', password):
            return False
        
        # Check if the password contains at least one digit
        if not re.search(r'\d', password):
            return False
        
        # Check if the password contains at least one special character
        if not re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password):
            return False
        
        return True
            
        


               
        
