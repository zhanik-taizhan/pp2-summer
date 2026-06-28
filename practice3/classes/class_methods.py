# Class with methods
class Student:

    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

    # Display student information
    def show_information(self):
        print("Name:", self.student_name)
        print("Age:", self.student_age)

    # Update student's age
    def birthday(self):
        self.student_age += 1
        print(self.student_name, "is now", self.student_age)

# Create an object
student = Student("Alex", 19)

# Call methods
student.show_information()
student.birthday()