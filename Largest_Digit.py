a=int(input())
b=str(a)
c=b[0]
for i in b:
    if c<i:
        c=i
print(c)