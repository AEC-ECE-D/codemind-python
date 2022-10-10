n=int(input())
m=int(input())
for i in range(n,m+1):
    a=i
    while a:
        r=a%10
        if r==0:
            f=False
            break
        if i%r==0:
            f=True
        else:
            f=False
            break
        a=a//10
    if f==True:
        print(i,end=' ')