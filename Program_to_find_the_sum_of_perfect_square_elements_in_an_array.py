a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    b=int(i**(1/2))
    c=b*b
    if int(i)==c:
        s+=i
print(s)