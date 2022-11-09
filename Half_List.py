n=int(input())
a=list(map(int,input().split()))
b=len(a)
c=[]
d=[]
e=[]
for i in range(0,(n//2)):
    c.append(a[i])
for j in range(n//2,n):
    d.append(a[j])
d=d[::-1]
e=d+c
print(*e)
