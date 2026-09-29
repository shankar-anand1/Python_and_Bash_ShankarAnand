# Student Grades
# dictionary of names and grades

students = {
    "Amit": "B",
    "Priya": "A",
    "Rahul": "C"
}

print("1. Add student")
print("2. Update grade")
print("3. Show all grades")
choice = input("Enter choice (1/2/3): ")

if choice == "1":
    name = input("Student name: ")
    grade = input("Grade: ")
    students[name] = grade
    print("Added", name)
elif choice == "2":
    name = input("Student name: ")
    if name in students:
        grade = input("New grade: ")
        students[name] = grade
        print("Updated", name)
    else:
        print("Student not found")
elif choice == "3":
    print("All grades:")
    for name, grade in students.items():
        print(name, ":", grade)
else:
    print("Invalid choice")
