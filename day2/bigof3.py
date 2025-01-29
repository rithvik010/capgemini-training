import dis
def get_input():

    a=int(input("enter first number "))
    b=int(input("enter second number "))
    c=int(input("enter third number "))
    return (a,b,c)
def display(data):
    print(f"the biggest num is {data}")

def find(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>a:
        if b>c:
            return b
        else:
            return c
def main():
    (a,b,c)=get_input()
    big=find(a,b,c)
    display(big)
    dis.dis(find)
main()