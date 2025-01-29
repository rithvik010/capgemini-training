def get_input():
    n=int(input("enter  an number : "))
    choice=int(input("1.normal pattern\t 2.reverse patter"))
    return (n,choice)
def normal_pattern(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print("* ",end="")
        print("\n")
def reverse_pattern(n):
    for i in reversed(range(n+1)):
        for j in range (0,i):
            print("* ",end="")
        print("\n")
def main():
    (n,choice)=get_input()
    if choice==1:
        normal_pattern(n)
    elif choice==2:
        reverse_pattern(n)
main()

