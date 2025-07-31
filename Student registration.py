# Student Registration Program

students = []  # List to store student records

def register_student():
    print("\n--- Student Registration ---")
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    course = input("Enter course name: ")

    student = {
        'Name': name,
        'ID': student_id,
        'Course': course
    }

    students.append(student)
    print(f"\nStudent {name} has been registered successfully!\n")

def view_students():
    if not students:
        print("\nNo students registered yet.\n")
        return

    print("\n--- Registered Students ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['Name']}, ID: {student['ID']}, Course: {student['Course']}")

def main():
    while True:
        print("\n==== Student Registration System ====")
        print("1. Register a new student")
        print("2. View all registered students")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            register_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
