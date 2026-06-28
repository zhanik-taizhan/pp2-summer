# Parent class
class Animal:

    def make_sound(self):
        print("Animal makes a sound")

# Child class overrides the method
class Dog(Animal):

    def make_sound(self):
        print("Dog barks")

# Create objects
animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()