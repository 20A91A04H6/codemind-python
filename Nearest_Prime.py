t=int(input())
for i in range(t):
    a=int(input())
    y=w=n=v=0
    for j in range(a,0,-1):
        x=0
        for k in range(1,j+1):
            if j%k==0:
                x+=1
        if x==2:
            y=j
            break
    for l in range(a+1,a*a):
        z=0
        for m in range(1,l+1):
            if l%m==0:
                z+=1
        if z==2:
            w=l
            break
    n=a-y
    v=w-a
    if n==v:
        print(y)
    elif n<v:
        print(y)
    else:
        print(w)
                
            