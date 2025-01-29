#balance check
def check_balance(balance):
    print(f"your balance: {balance}")
#deposit the money
def deposit(balance):
    print(" Enter the amount you want to deposit: ")
    amount=int(input())
    balance=balance+amount
    return balance
#withdraw money
def withdraw(balance): 
    print("Enter the amount you want to deposit: ")
    amount= int(input())
    if balance-amount<0:
        print("Insufficiant balance")
    else:
        balance=balance-amount
    return balance
    
def main():
    balance=0
    while True:
        print("1.check balance\t 2.deposit money\n3.withdraw money\t4.exit")
        n=int(input("enter input: "))
        if n==1:
            check_balance(balance)
        elif n==2:
            balance=deposit(balance)
        elif n==3:
            balance=withdraw(balance)
        elif n==4:
            break
main()

