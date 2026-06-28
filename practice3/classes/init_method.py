# Class with constructor
class Student:

    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

# Create objects
student1 = Student("Alex", 19)
student2 = Student("Emma", 20)

# Print object data
print(student1.student_name, student1.student_age)
print(student2.student_name, student2.student_age)