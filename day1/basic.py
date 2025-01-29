#n=255
#ans=n/10*10
#ans1=float(int(n/10)*10)
#print(ans,ans1)
import math
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
root_1=(-b+math.sqrt((b*b)-(4*a*c)))/(2*a)
root_2=(-b-math.sqrt((b*b)-(4*a*c)))/(2*a)
print(root_1,root_2)



