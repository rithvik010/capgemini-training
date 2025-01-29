n=int(input("enter number of numbers to be taken into list"))
list=[]
for i in range(0,n):
     number=int(input("enter a number : "))
     list.append(number)
even=[]
odd=[]
for j in range(0,n):
     if list[j]%2==1:
          odd.append(list[j])
     else:
          even.append(list[j])
print(f"{even} even list")
print(f"{odd} odd list")
     
