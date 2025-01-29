import dis
def get_input():
    max=0
    a=int(input("enter first number "))
    if a>max:
        max=a
        var="a"
    b=int(input("enter second number ")) 
    if b>max:
        max=b
        var="b"
    c=int(input("enter third number "))
    if c>max:
        max=c
        var="c"
    d=int(input("enter fourth number "))
    if d>max:
        max=d
        var="d"
    return (max,var)
def display(max,var):
    print(f"the bigeet variable is {var} with value {max}")
def main():
    var="no"
    
    (a,b,c,d)=get_input()
    display(max,var)
    dis.dis(get_input)
main()