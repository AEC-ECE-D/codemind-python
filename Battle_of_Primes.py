n=int(input())
m=int(input())
a=n+m
b=a+1
i=1
c=0
while True:
    while i<=b:
        if b%i==0:
            c+=1
        i+=1
    if c==2:
        print(b-a)
        break
    b+=1
    c=0
    i=1
    