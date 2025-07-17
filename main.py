import json
DB_FILE = "students.json"

def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None