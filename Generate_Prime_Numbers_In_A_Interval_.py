a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    x=0
    for j in range(1,i+1):
        if i%j==0:
            x+=1
    if x==2:
        print(i)
        