def get_input():
    n=int(input("enter number of elements : "))
    list=[]
    for i in range(0,n):
        element=int(input("enter value "))
        list.append(element)
    return (n,list)
def min_max(n,list):
    min=list[0]
    max=list[0]
    for i in range(0,n):
        if list[i]>max:
            max=list[i]
        elif list[i]<min:
            min=list[i]
    return(min,max)

def main():
    (n,list)=get_input()
    (min,max)=min_max(n,list)

    print(list)
    print(f"smallest element is {min}\nlargest element is {max}")
main()
