# Parent class
class Person:

    def __init__(self, name):
        self.name = name

# Child class using super()
class Student(Person):

    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def show_information(self):
        print("Name:", self.name)
        print("University:", self.university)

# Create object
student = Student("Emma", "KBTU")

student.show_information()