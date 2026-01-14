# A method is a function used inside a class.

class Student:
    name = "" 
    roll = "" 
    cgpa = ""
    def display(self): # this is a method
        print(f"The student name is: {self.name}\nroll = {self.roll}\ncgpa = {self.cgpa}")

shagor = Student()
shagor.name = "Abs shagor"
shagor.roll = 1
shagor.cgpa = 3.83
shagor.display()