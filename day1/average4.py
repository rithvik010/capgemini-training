def get_input():
    a=int(input("enter first number "))
    b=int(input("enter second number "))
    c=int(input("enter third number "))
    d=int(input("enter fourth number "))
    return (a,b,c,d)
def add(a,b,c,d):
    return a+b+c+d
def cal(sum):
    return sum/4
def display(data):
    print(f"the avg of 4 numbers is {data}")

def main():
    (a,b,c,d)=get_input()
    sum=add(a,b,c,d)
    avg=cal(sum)
    display(avg)
main()
    