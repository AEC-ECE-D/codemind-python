n=int(input())
m=list(map(int,input().strip().split()))[:n]
x,y=map(int,input().split())
a,b=min(x,y),max(x,y)
c=1000
for i in range(len(m)):
    if m[i]>=a and m[i]<=b:
        if m[i]<c:
            c=m[i]
if c==1000:
    print(-1)
else:
    print(c)