import json
DB_FILE = "students.json"


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


