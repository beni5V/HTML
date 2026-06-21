# Creating a class
class Student:

    # Constructor method (runs when object is created)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method inside the class
    def show_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

# Creating an object of the class
student1 = Student("Sarah", 11)

# Calling the method
student1.show_info()