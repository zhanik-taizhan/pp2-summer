# Using lambda with sorted()

students = [
    {"name": "Alex", "grade": 88},
    {"name": "Emma", "grade": 95},
    {"name": "John", "grade": 81}
]

# Sort students by grade
sorted_students = sorted(students, key=lambda student: student["grade"])

for student in sorted_students:
    print(student)