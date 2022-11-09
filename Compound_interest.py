p,r,t=map(int,input().split())
c=1+(r/100)
d=p*(c**t)
print('{:.2f}'.format(d))