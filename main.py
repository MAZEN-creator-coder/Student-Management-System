import json

DB_FILE = "students.json"

# === File Operations ===
def load_students():
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open(DB_FILE, 'w') as file:
        json.dump(students, file, indent=4)

# === Functionalities ===
def add_student(students):
    try:
        student_id = int(input("Enter student ID: "))
        if any(s['id'] == student_id for s in students):
            print("❌ Student ID already exists.")
            return

        name = input("Enter student name: ")
        grade = float(input("Enter student grade (0-100): "))
        if not (0 <= grade <= 100):
            print("❌ Grade must be between 0 and 100.")
            return

        students.append({"id": student_id, "name": name, "grade": grade})
        save_students(students)
        print("✅ Student added successfully.")

    except ValueError:
        print("❌ Invalid input. ID and grade must be numeric.")

def view_all_students(students):
    if not students:
        print("📭 No students found.")
        return
    print("\n--- All Students ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Grade: {s['grade']}")

def find_student_by_id(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def update_student_grade(students):
    try:
        student_id = int(input("Enter student ID to update: "))
        student = find_student_by_id(students, student_id)
        if not student:
            print("❌ Student not found.")
            return

        new_grade = float(input("Enter new grade (0–100): "))
        if not (0 <= new_grade <= 100):
            print("❌ Grade must be between 0 and 100.")
            return

        student['grade'] = new_grade
        save_students(students)
        print(f"✅ Grade updated for {student['name']} to {new_grade}.")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

def delete_student(students):
    try:
        student_id = int(input("Enter student ID to delete: "))
        student = find_student_by_id(students, student_id)
        if not student:
            print("❌ Student not found.")
            return

        students.remove(student)
        save_students(students)
        print("✅ Student deleted.")

    except ValueError:
        print("❌ Invalid input. ID must be numeric.")

def calculate_average_grade(students):
    if not students:
        print("📭 No students to calculate.")
        return
    average = sum(s["grade"] for s in students) / len(students)
    print(f"📊 Average grade: {average:.2f}")

def find_top_student(students):
    if not students:
        print("📭 No students available.")
        return
    top = max(students, key=lambda s: s["grade"])
    print(f"🏆 Top student: {top['name']} (ID: {top['id']}), Grade: {top['grade']}")

# === Menu ===
def main():
    while True:
        students = load_students()  # always load fresh data from file
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
                    print(f"✅ Found: ID={student['id']}, Name={student['name']}, Grade={student['grade']}")
                else:
                    print("❌ Student not found.")
            except ValueError:
                print("❌ Invalid input. ID must be numeric.")
        elif choice == '4':
            update_student_grade(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            calculate_average_grade(students)
        elif choice == '7':
            find_top_student(students)
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 8.")

# === Run ===
if __name__ == "__main__":
    main()
