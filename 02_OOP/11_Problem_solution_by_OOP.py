####    No.1 Banking Systme
# Design a banking system where users have accounts. Each BankAccount has a unique 
# ID and a balance, and supports operations like deposit and withdraw. Optional task:
#  implement multiple account types (savings, checking) and transfer  money between them.

class BankAccount:
    def __init__(self, accountID, balance=0):
        self.account_number = accountID
        self.balance = balance
    
    def deposit(self, amount):
        if( type(amount)!=int or amount<=0  ):
            print('Invalid amount!\n')
        else:
            self.balance += amount
            print(f'Deposited {amount} BDT in {self.account_number}\nNew Balance: {self.balance} BDT\n')
    
    def withdraw(self, amount):
        if( type(amount)!=int or amount>self.balance ):
            print('Invalid amount!\n')
        else:
            self.balance -= amount;
            print(f'Withdrawn {amount} BDT from {self.account_number}\nNew Balance: {self.balance} BDT\n')

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number

def transfer_money(user1, user2, amount):
    account1 = user1.get_account_number()
    account2 = user2.get_account_number()
    account1_balance = user1.get_balance()
    if( type(amount)!=int or amount>account1_balance ):
        print('Invalid amount!\n')
    else:
        user1.withdraw(amount)
        user2.deposit(amount)
        print(f'Message: {amount} BDT transfer from {account1} To {account2} successfully. ')
    


# Let's create user
user1 = BankAccount('acc1', 5000)
user2 = BankAccount('acc2', 10000)

# checking current balance
print(f'Account Number: {user1.get_account_number()}\nCurrent Balance: {user1.balance}\n')
print(f'Account Number: {user2.get_account_number()}\nCurrent Balance: {user2.balance}\n')

# Deposit and withdraw some amount from account 1
user1.deposit(150)
user1.withdraw(50)

# Trasfering 2000 BDT from user1 account to user2 account
transfer_money(user1, user2, 2000)