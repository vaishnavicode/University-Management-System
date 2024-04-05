# The entrance for the program

# The main menu is displayed here
def main_menu():
    while True:
        print("\n======University Management System's Menu======")
        print("Enter 1 to open Student's Panel")
        print("Enter 2 to open Teacher's Panel")
        print("Enter 3 to open HOD's Panel")
        print("Enter 4 to open Principal's Panel")
        print("Enter 5 to open Staff's Panel")
        print("Enter 6 to open Parent's Panel")
        print("Enter 7 to open Admin's Panel")
        print("Enter 8 to exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            import Student
        elif choice == 2:
            import Teacher
        elif choice == 3:
            import HOD
        elif choice == 4:
            import Principal
        elif choice == 5:
            import Staff
        elif choice == 6:
            import Parent
        elif choice == 7:
            import Admin
        elif choice == 8:
            break

try: 
    main_menu()
except:
    print("An error occured, try again.")
    main_menu()
    