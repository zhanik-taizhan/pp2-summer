# Parent class
class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

# Child class
class Student(Person):

    def study(self):
        print(self.name, "is studying Python")

# Create object
student = Student("Alex")

# Call methods
student.introduce()
student.study()