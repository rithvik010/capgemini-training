n=int(input("enter number of elements"))
list=[]
sum=0
for i in range(0,n):
    element=int(input("enter value "))
    list.append(element)
    sum=sum+element
print(list)
print(sum)
