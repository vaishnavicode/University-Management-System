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
            print("4. Logout")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.add_teacher()
            elif choice == "2":
                self.remove_teacher()
            elif choice == "3":
                self.view_student_data()
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_teacher(self):
        # Read the teacher data from the CSV file
        teachers = read_csv("data/teachers.csv")

        # Prompt the HOD to enter the teacher's details
        teacher_id = input("Enter the teacher ID: ")
        for teacher in teachers:
            if teacher["id"] == teacher_id:
                # Add the teacher to the HOD's list of teachers
                self.teachers.append(teacher)
                print(f"Teacher {teacher['name']} added successfully.")
                return

        print("Teacher not found. Please try again.")

    def remove_teacher(self):
        # Prompt the HOD to enter the teacher's ID
        teacher_id = input("Enter the teacher ID to remove: ")
        for teacher in self.teachers:
            if teacher["id"] == teacher_id:
                self.teachers.remove(teacher)
                print(f"Teacher {teacher['name']} removed successfully.")
                return

        print("Teacher not found. Please try again.")

    def view_student_data(self):
        # Read the student data from the CSV file
        students = read_csv("data/students.csv")
        self.students = students

        print("Student Data:")
        for student in self.students:
            print(f"ID: {student['id']}, Name: {student['name']}, Department: {student['department']}")
            print(f"Attendance: {student['attendance']}")
            print(f"Marks: {student['marks']}")
            print()
