from utils.file_handling import read_csv, write_csv

class HOD:
    def __init__(self, hod_data):
        self.id = hod_data["id"]
        self.name = hod_data["name"]
        self.department = hod_data["department"]
        self.email = hod_data["email"]
        self.password = hod_data["password"]
        self.teachers = []  # To store the teachers in the HOD's department
        self.students = []  # To store the students in the HOD's department

    def display_menu(self):
        while True:
            print(f"\nWelcome, {self.name}!")
            print("HOD Menu:")
            print("1. Add Teacher")
            print("2. Remove Teacher")
            print("3. View Student Data")
            print("4. View Teacher Data")
            print("5. Logout")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_teacher()
            elif choice == "2":
                self.remove_teacher()
            elif choice == "3":
                self.view_student_data()
            elif choice == "4":
                self.view_teacher_data()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_teacher(self):
        # Read the teacher data from the CSV file
        teachers = read_csv("data/teachers.csv")

        # Prompt the HOD to enter the teacher's details
        teacher_id = input("Enter the teacher ID: ")
        teacher_name = input("Enter the teacher name: ")
        teacher_department = input("Enter the teacher department: ")
        teacher_email = input("Enter the teacher email: ")
        teacher_password = input("Enter the teacher password: ")

        # Create a dictionary to store the teacher's details
        teacher = {
            "id": teacher_id,
            "name": teacher_name,
            "department": teacher_department,
            "email": teacher_email,
            "password": teacher_password
        }

        # Add the teacher to the list of teachers
        teachers.append(teacher)

        # Write the updated list of teachers back to the CSV file
        write_csv("data/teachers.csv", teachers)
        print(f"Teacher {teacher_name} added successfully.")
        self.teachers = teachers

    def remove_teacher(self):
        # Read the teacher data from the CSV file
        teachers = read_csv("data/teachers.csv")

        # Prompt the HOD to enter the teacher's ID
        teacher_id = input("Enter the teacher ID to remove: ")

        # Find the teacher with the given ID
        teacher_found = False
        for teacher in teachers:
            if teacher["id"] == teacher_id:
                teacher_found = True
                break

        if teacher_found:
            # Remove the teacher from the list of teachers
            teachers.remove(teacher)

            # Write the updated list of teachers back to the CSV file
            write_csv("data/teachers.csv", teachers)
            print(f"Teacher {teacher['name']} removed successfully.")
            self.teachers = teachers
        else:
            print("Teacher not found. Please enter a valid teacher ID.")
        


    def view_student_data(self):
        # Read the student data from the CSV file
        students = read_csv("data/students.csv")
        self.students = students

        print("\n--- Student Data ---\n")
        for student in self.students:
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Department:", student["department"])
            print("Attendance:", student["attendance"], "%")
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
            print()

    
    def view_teacher_data(self):
        # Read the teacher data from the CSV file
        teachers = read_csv("data/teachers.csv")

        print("\n--- Teacher Data ---\n")
        for teacher in teachers:
            print(f"ID: {teacher['id']}, Name: {teacher['name']}, Department: {teacher['department']}")
        print("\n")
