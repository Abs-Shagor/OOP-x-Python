#  Let's implement class, object, method, method overriding, constractor, 
#  Abstraction, Polymorphism, Inheritance, Encapsulation

class Father:               # class
    name = 'MD. Alam'
    occupation = 'Business';

class Mother:
    name = 'Ruma Akther'    # propertise
    occupation = 'House Wife'
    def displayMother(self):
        print('This is Mother display mehtod');

class Son(Father, Mother):  # Inheritance
    address = ' Raozan, Chittagong'

    def __init__(self, name, age, height):  # constarctor
        self.name = name
        self.age = age
        self.height = height

    def display(self):      # method
        print(f'Name: {self.name} \nAge: {self.age} \nHeight: {self.height}')
        print(f'Father Name: {Father.name} \nOccupation: {Father.occupation} ')
        print(f'Mother Name: {Mother.name} \nOccupation: {Mother.occupation} ')
        print(f'Address: {self.address} \n');

    def displayMother(self):    # method overriding
        print('This is method overriding bcz we implement the same displayMother method which is already defined in the Mother class.');

    def sum(self, x, y, z=0):   # Polymorphism or we can this is a polymorphic method
        return x+y+z;


Shagor = Son('Abs Shagor', 26, 5.7) # object
Joy = Son('Mohammad Joy', 24, 5.7)
Sami = Son('Sajia Sultana', 17, 5.5)
Shagor.display()
Joy.display()
Sami.display()
Sami.displayMother()
Sami.sum(3,6)
Sami.sum(4, 11, 7)


