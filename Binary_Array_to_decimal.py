a=int(input())
b=list(map(int,input().split()))
s=0
c=len(b)
for j in range (len(b)):
    s+=(2**c)*b[j]
    c-=1
print(s//2)