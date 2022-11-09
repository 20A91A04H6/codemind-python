a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i==0:
        c.append(i)
    else:
        d.append(i)
e=c+d
print(*e)