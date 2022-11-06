x=int(input())
l=[]
a=0
b=1
l.append(a)
l.append(b)
for i in range(x):
    c=a+b
    a=b
    b=c
    l.append(c)
if x in l:
    print("True")
else:
    print("False")