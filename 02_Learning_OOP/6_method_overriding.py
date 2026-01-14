# Method overriding occurs when a child class create/implement a method which
#  is already defined/created in its parent class.

class Teacher:
    def display(self):
        print("Hello, I am in Teacher or Parent class")

class Student(Teacher):
    def display(self): # overrides the display method of Teacher class
        print("Hello, I am in Student or Child class")
        # if we want to execute the display method of Teacher class
        # simply use: super().display()


shagor = Student()
shagor.display()