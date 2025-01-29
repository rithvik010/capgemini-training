n=int(input("enter number of inputs in a list "))
list=[]
for i in range(0,n):
    number=int(input("enter a number : "))
    list.append(number)
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
b=list[-2]
print(f"{b} is second largest number")