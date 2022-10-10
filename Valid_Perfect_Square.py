from math import sqrt
n=int(input())
p=1
for i in range(1,n+1):
    m=int(input())
    k=int(sqrt(m))
    while p<=k:
        c=p*p
        if c==m:
            print(True)
            break
        p+=1
    if c!=m:
        print(False)
    p=1