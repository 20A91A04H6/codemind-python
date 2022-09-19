a=int(input())
b=str(a)
s=0
for i in range(len(b)):
    c=int(b[i])**(i+1)
    s+=c
if a==s:
    print("True")
else:
    print("False")