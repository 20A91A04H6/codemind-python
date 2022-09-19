a=int(input())
b=int(str(a)[::-1])
c=a*a
d=b*b
e=int(str(d)[::-1])
if c==e:
    print("True")
else:
    print("False")