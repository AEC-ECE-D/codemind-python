n=int(input())
i=1
k=1
c=0
d=0
s=str(n)
s=s[::-1]
m=int(s)
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    while k<=m:
        if m%k==0:
            d+=1
        k+=1
    if d==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")
    