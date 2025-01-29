def get_input():
    print("enter 1 to convert celsius to fahreinheit and kelvin \n")
    print("enter 2 to convert fahreinheit to celsius and kelvin \n")
    print("enter 3 to convert kelvin to celsius and fahreinheit \n")
    n=int(input())
    return n
def c_to_f_and_k(c):
    f=c*(9/5)+32
    k=c+273.15
    return(f,k)
def f_to_c_and_k(f):
    c=(f-32)*(5/9)
    k=c+273.15
    return(c,k)
def k_to_c_and_f(k):
    c=k-273.15
    f=c*(9/5)+32
    return (c,f)
def main():
    n=get_input()
    if n==1:
        c=float(input("enter value in celcius : "))
        (f,k)=c_to_f_and_k(c)
        print(f"{c}'c is {f}'F and {k}'k ")
    elif n==2:
        f=float(input("enter value in fahrenheit : "))
        (c,k)=f_to_c_and_k(f)
        print(f"{f}'F is {c}'c and {k}'k ")
    elif n==3:
        k=float(input("enter value in kelvin : "))
        (c,k)=k_to_c_and_f(k)
        print(f"{k}'k is {c}'c and {f}'F ")
main()
    
      

