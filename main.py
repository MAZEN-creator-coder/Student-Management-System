import json
DB_FILE = "students.json"


def update_student_grade():
    students = load_students()
    try:
        student_id = int(input("Enter student ID to update: "))
        new_grade = float(input("Enter new grade (0-100): "))
        if new_grade < 0 or new_grade > 100:
            print("Grade must be between 0 and 100.")
            return

        for student in students:
            if student['id'] == student_id:
                student['grade'] = new_grade
                save_students(students)
                print(f"Grade updated for {student['name']} to {new_grade}.")
                return

        print("Student ID not found.")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

def view_all_students(students):
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Grade: {s['grade']}")



def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def add_student():
    students = load_students()
    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        grade = float(input("Enter student grade (0-100): "))
        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")
            return
        for student in students:
            if student['id'] == student_id:
                print("Student ID already exists.")
                return
        students.append({"id": student_id, "name": name, "grade": grade})
        save_students(students)
        print("Student added successfully.")
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and grade.")

def load_students():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(DB_FILE, 'w') as file:
        json.dump(students, file, indent=4)


def calculate_average_grade(students):
    if not students:
        print("No students to calculate.")
        return
    average = sum(s["grade"] for s in students) / len(students)
    print(f"Average grade: {average:.2f}")

def find_top_student(students):
    if not students:
        print("No students available.")
        return
    top = max(students, key=lambda s: s["grade"])
    print(f"Top student: {top['name']} (ID: {top['id']}), Grade: {top['grade']}")

def main():
    students = load_students()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Find student by ID")
        print("4. Update student grade")
        print("5. Delete student")
        print("6. Calculate average grade")
        print("7. Find top student")
        print("8. Exit")
        choice = input("Enter choice (1–8): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            try:
                sid = int(input("Enter student ID: "))
                student = find_student_by_id(students, sid)
                if student:
                    print(student)
                else:
                    print("Student not found.")
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            update_student_grade(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            calculate_average_grade(students)
        elif choice == '7':
            find_top_student(students)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


