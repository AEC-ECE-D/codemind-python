n=int(input())
i=1
k=2
c=0
a=0
b=0
for i in range(1,n+1):
    m=int(input())
    a=0
    b=0
    while True:
        a=b
        while i<=k:
            if k%i==0:
                c+=1
            i+=1
        if c==2:
            b=k
        c=0
        i=1
        if b>m:
            break
        k+=1
    k=1
    x=abs(a-m)
    y=abs(b-m)
    if x<y:
        print(a)
    elif x>y:
        print(b)
    else:
        print(a)