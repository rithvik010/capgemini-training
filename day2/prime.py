import math
def get_input():
    n=int(input("enter a number "))
    return n
def prime(n):
    c=1
    if n%2==1:
        for i in range(3,int(math.sqrt(n))):
            if n%i==1:
                c=c+1
        return c
    else:
        return 0
def display(data,n):
    if data==1:
        print(f"{n} is prime")
    else:
        print(f"{n} is  not prime")
def main():
    n=get_input()
    res=prime(n)
    display(res,n)
main()
    