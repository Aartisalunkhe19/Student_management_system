from database import create_table
import student

def menu():
    print("""
 Student Management System
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")

def main():
    create_table()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            roll = int(input("Roll No: "))
            name = input("Name: ")
            age = int(input("Age: "))
            course = input("Course: ")
            student.add_student(roll, name, age, course)

        elif choice == "2":
            student.view_students()

        elif choice == "3":
            roll = int(input("Enter roll number: "))
            student.search_student(roll)

        elif choice == "4":
            roll = int(input("Roll No to update: "))
            name = input("New Name: ")
            age = int(input("New Age: "))
            course = input("New Course: ")
            student.update_student(roll, name, age, course)

        elif choice == "5":
            roll = int(input("Roll No to delete: "))
            student.delete_student(roll)

        elif choice == "6":
            print(" Exiting program")
            break

        else:
            print(" Invalid choice")

if __name__ == "__main__":
    main()
