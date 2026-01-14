
class Person:      # This is a class
    name = "Abs Shagor" # This are some propertise of the class.
    age = 26
    def display(self): # This is a method
        print(f"The name of the Person is {self.name} and he is {self.age} years old.")


Shagor = Person()  # This is a object of the Student class
Shagor.display()
print()

# Now, Let's implement it with class, object, method, constractor
class Student:
    def __init__(self, name, age):  # Constractor
        self.name = name
        self.age = age

    def display(self):
        print(f"Student Name: {self.name} ")
        print(f"Age: {self.age}")
        print()

Shagor = Student("Abs Shagor", 26)
Joy = Student("Mohammad Joy", 24)
Sami = Student("Sajia sultana sami", 17)
Shagor.display()
Joy.display()
Sami.display()

# Inheritance: it is a technique to use the parents class propertise in the child class.
class Father:
    name = ""
    age = ""
    height = "";
class Mother:
    color = ""
    weight = "";
class Shagor(Father, Mother):
    def display(self):
        print(self.name);
    