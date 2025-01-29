import math;
def get_input():
    n=int(input("enter number of elements : "))
    list=[]
    for i in range(0,n):
        element=int(input("enter value "))
        list.append(element)
    return (n,list)
def is_prime(list,n):
    prime_list=[]
    for i in range(len(list)):
        c=0
        for j in range(2,int(math.sqrt(n))):
            if list[i]==2:
                prime_list.append(list[i])
            elif (list[i])%j==0:
                c+=1
        if c==0:
            prime_list.append(list[i])
    return prime_list
def main():
    (n,list)=get_input()
    print(list)
    prime_list=is_prime(list,n)
 

    print(prime_list)
   # print(f"smallest element is {min}\nlargest element is {max}")
main()