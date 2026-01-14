# Abstraction hides implementation details and shows only what is needed
# An Abstract class is a class which has at least one abstract method. 
# Here,abstract method is a function which is empty or not implemented yet. 
# The abstract class forces  all of its child class to implement this empty method.
# If the child class implement the abstract method they can use the abstract class.

from abc import ABC, abstractmethod     # abc = abstract base class

class LoginCondition(ABC):              # this is a abstract class
    @abstractmethod
    def login(self, email, password):   # this is a abstract method
        pass;
    
    name = "Abs_Shagor56"
    age = 26


class UserLogin(LoginCondition):
    def login(self, email, password):   # here, we implement the abstract method
        if(email=='siddik56u@gmail.com' and password=='1234'):
            print('Login successful.')
        else:
            print('Wrong email/pass.');
    def display(self):
        print('As we implemented the abstract method, now')
        print(' we can use the properties of the abstract class')
        print(f'Name: {LoginCondition.name} \nAge: {LoginCondition.age}')


User = UserLogin()
User.login('siddik56u@gmail.com', '1234')
User.display()