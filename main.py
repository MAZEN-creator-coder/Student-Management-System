import json
DB_FILE = "students.json"
def view_all_students(students):
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Grade: {s['grade']}")