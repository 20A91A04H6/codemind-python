n=int(input())
a=list(map(int,input().split()))
c=int(input())
b=0
for i in a:
    if i==c:
        b+=1
print(b)
        