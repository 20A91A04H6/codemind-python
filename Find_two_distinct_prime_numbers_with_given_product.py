a=int(input())
l=[]
x=0
for i in range(1,a):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(i)
for k in l:
    if a%k==0:
        x=a//k
        break
if k*x==a:
    print(k,x,end=' ')
else:
    print('-1')

        