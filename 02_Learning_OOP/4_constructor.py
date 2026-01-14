# Constructor is a special type of method(__init__) used to initialize the
# Object attributes/parameter when the object is created.

class Student:
    name = "" 
    roll = "" 
    cgpa = ""
    def __init__(self,name,roll,cgpa): # this is a constructor
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
    def display(self): # this is a method
        print(f"The student name is: {self.name}\nroll = {self.roll}\ncgpa = {self.cgpa}")


shagor = Student("Abs Shagor",1,3.83) # by using constructor we can pass the attribute/parameter during the object creation
shagor.display()
print()


# We can pass method parameter after creating the object like below.
class person:
    def displayy(self, name):
        print(f'my name is {name}');

ss = person()
ss.displayy('Abs_Shagor56')