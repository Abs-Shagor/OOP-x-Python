# Before we learn Encapsulation, We should know one thing and that is
#			“Nothing is Strictly Private in Python”
# In other languages like Java, C/C++ the private properties/methods are not accessable.
# But in python its possible to access and modify the private value. To control
# access properly in python we use the getter and setter method.

# Encapsulation: Encapsulation is a technique to restrict direct access of data using public, protected and private modes. 
# It’s used to prevent misuse and control the data.

# public ⇒ we can use or modify them(properties, methods etc.).
# protected ⇒ we can also use or modify them if we want but it shows a warning to not to use them.
# private ⇒ we cannot use or modify them directly. But in python it is possible to access them.

class Atm:
    def __init__(self, Name, Pin):
        self.name = Name
        self.pin = Pin

    print('Account is created and You get 10,000 Taka as bonus. Enjoy! \n')
    
    bankName = 'Sonali Bank Ltd.'
    _branchName = 'Raozan Branch'   # protected 
    __balance = 10000           # Private
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, xyz):
        self.__balance = xyz

    def add_balance(self, xyz):
        self.__balance += xyz
    
    def get_branch_name(self):
        return self._branchName


p1 = Atm('Abs Shagor', 1234)

print(p1.bankName)
# It is prohivated to access the protected & private properties/methods
# print(p1.branch) or print(p1.balance) will return error
# print(p1._branch) # can be accessable
# print(p1.__balance) # access denied

print(p1.get_branch_name())

print(p1.get_balance())

p1.set_balance(5000)

print(p1.get_balance())

p1.add_balance(2000)

print(p1.get_balance())
