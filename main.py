import json
DB_FILE = "students.json"

def add_student(students):
    name = input("Enter student name: ").strip()
    
    try:
        grade_input = input("Enter student grade (0–100): ").strip()
        grade = float(grade_input)
        
        if 0 <= grade <= 100:
            new_id = max([s["id"] for s in students], default=0) + 1
            students.append({"id": new_id, "name": name, "grade": grade})
            save_students(students)
            print("✅ Student added successfully.")
        else:
            print("❌ Grade must be between 0 and 100.")
    except ValueError:
        print("❌ Invalid grade. Please enter a numeric value.")

def load_students():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(DB_FILE, 'w') as file:
        json.dump(students, file, indent=4)

