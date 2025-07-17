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