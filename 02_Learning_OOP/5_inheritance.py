# It is technique which allow a child class to use the property of the parent class.
# simply, to use a class property in another class is called inheritance

# Let, we have two class: teacher and student
# by using inheritance we use the property of tracher class in student class

class Teacher:
    name = ""
    age = ""
    id_no = ""
    def display(self):
        print(f"Name : {self.name}\nAge : {self.age}")

class Student(Teacher): # initializing inheritance
    roll = ""
    cgpa = ""
    def display2(self):
        print(f"Roll : {self.roll}\nCGPA : {self.cgpa}")

shagor = Teacher()
shagor.name = "Abs"
shagor.age = 25
shagor.display()

print("------------------")

joy = Student()
joy.name = "Md Joy"
joy.age = 24
joy.roll = 1
joy.cgpa = 3.8
joy.display()
joy.display2()

# to check whether the student is the child class of Teacher class or not
print(issubclass(Student,Teacher))