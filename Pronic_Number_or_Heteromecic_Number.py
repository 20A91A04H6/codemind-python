a=int(input())
temp=0
for i in range(1,a+1):
    if a==i*(i+1):
        temp=True
        break
if temp==True:
    print("YES")
else:
    print("NO")