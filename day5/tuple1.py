empty=()
print(empty)
t=(0,)
print(t)

o=5
t1=(0,'ni',1.2,3)
t11=o,'ni',1.2,3
print(t1)
print(t11)

t2=('abc',('def','ghi'))
print(t2)

print(t2[0])
print(t2[1][0])

t3=tuple('spam')
print(t3)
print(len(t3))