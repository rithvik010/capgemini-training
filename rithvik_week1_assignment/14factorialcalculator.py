def get_input():
    number=int(input("enter a number"))
    return abs(number)
def fact(number):
    if number==1 or number==0 :
        return 1
    else:
        return number*fact(number-1)
def main():
    number=get_input()
    factorial=fact(number)
    print(f"{factorial} is factorial of {number}")
main()