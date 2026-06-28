# Class variable example
class Student:

    university = "KBTU"   # Shared by all students

    def __init__(self, student_name):
        self.student_name = student_name   # Instance variable

# Create objects
student1 = Student("Alex")
student2 = Student("Emma")

# Print class and instance variables
print(student1.student_name)
print(student2.student_name)

print(student1.university)
print(student2.university)

# Change class variable
Student.university = "AITU"

print(student1.university)
print(student2.university)