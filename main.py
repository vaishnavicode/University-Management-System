import os
from users.student import Student
from users.teacher import Teacher
from users.hod import HOD
from utils.file_handling import read_csv, write_csv

def main():
    # Display the main menu
    while True:
        print("Welcome to the University Management System!")
        print("Please select your role:")
        print("1. Student")
        print("2. Teacher")
        print("3. HOD")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            login_as_student()
        elif choice == "2":
            login_as_teacher()
        elif choice == "3":
            login_as_hod()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def login_as_student():
    # Implement student login and functionality
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Read student data from CSV file
    students = read_csv("data/students.csv")
    for student_data in students:
        if student_data["email"] == email and student_data["password"] == password:
            print(f"Welcome, {student_data['name']}!")
            student = Student(student_data)
            student.display_menu()
            return
    print("Invalid email or password. Please try again.")

def login_as_teacher():
    # Implement teacher login and functionality
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Read teacher data from CSV file
    teachers = read_csv("data/teachers.csv")
    for teacher_data in teachers:
        if teacher_data["email"] == email and teacher_data["password"] == password:
            print(f"Welcome, {teacher_data['name']}!")
            teacher = Teacher(teacher_data)
            teacher.display_menu()
            return
    print("Invalid email or password. Please try again.")

def login_as_hod():
    # Implement HOD login and functionality
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Read HOD data from CSV file
    hods = read_csv("data/hod.csv")
    for hod_data in hods:
        if hod_data["email"] == email and hod_data["password"] == password:
            print(f"Welcome, {hod_data['name']}!")
            hod = HOD(hod_data)
            hod.display_menu()
            return
    print("Invalid email or password. Please try again.")

if __name__ == "__main__":
    main()
