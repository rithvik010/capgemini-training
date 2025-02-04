class BankAccount:
    def __init__(self,name, account_no, balance=0):
        self.name=name
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Account Holder Name:{self.name}")
        print(f"Deposited {amount} rupees \t Current Balance ={self.balance}")
    def withdraw(self,amount):
        print(f"Account Holder Name:{self.name}")
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"{amount} has been withdrawn\t Current Balance={self.balance}")
account1=BankAccount("Abdul","1212333333",10000)
account1.deposit(5000)
account1.withdraw(2000)