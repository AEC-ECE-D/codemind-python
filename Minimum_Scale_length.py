n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=min(m)
b=a
f=True
for k in range(1,a+1):
    f=True
    for i in m:
        if i%b!=0:
            f=False
            break
    if f==False:
        b-=1
    else:
        print(b)
        break
    