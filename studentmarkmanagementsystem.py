# Student Marks Management System

def add_student(students):
    name = input("Enter student name: ")
    marks_str = input("Enter marks separated by space: ")
    try:
        marks = [int(m) for m in marks_str.split()]
        average = sum(marks) / len(marks) if marks else 0
        students.append({
            'name': name,
            'marks': marks,
            'average': round(average, 2)
        })
        print(f"Student {name} added successfully!\n")
    except ValueError:
        print("Invalid marks format.\n")


def display_students(students):
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student Records ---")
    for i, student in enumerate(students, 1):
        print(
            f"{i}. Name: {student['name']}, "
            f"Marks: {student['marks']}, Average: {student['average']}"
        )
    print("-----------------------\n")


def find_top_student(students):
    if not students:
        print("No students found.\n")
        return

    top = max(students, key=lambda student: student['average'])
    print(f"\nTop Student: {top['name']} with average {top['average']}\n")


def main():
    students = []
    while True:
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Top Student")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            find_top_student(students)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()