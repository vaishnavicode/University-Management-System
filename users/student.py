class Student:
    def __init__(self, student_data):
        self.id = student_data["id"]
        self.name = student_data["name"]
        self.department = student_data["department"]
        self.email = student_data["email"]
        self.password = student_data["password"]
        self.attendance = student_data["attendance"]  # To store the student's attendance records
        self.marks = student_data["marks"]  # To store the student's marks


    def display_menu(self):
        while True:
            print(f"\nWelcome, {self.name}!")
            print("Student Menu:")
            print("1. View Attendance")
            print("2. View Marks")
            print("3. Logout")

            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.view_attendance()
            elif choice == "2":
                self.view_marks()
            elif choice == "3":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_attendance(self):
        if not self.attendance:
            print("No attendance records found.")
        else:
            print("Total Attendance:{}%".format(self.attendance))
            
                

    def view_marks(self):
        if not self.marks:
            print("No marks found.")
        else:
            print("Your marks:")
            marks_array = eval(self.marks)
            for subject in marks_array:
                print(f"{subject['subject']}: {subject['marks']}")
           
