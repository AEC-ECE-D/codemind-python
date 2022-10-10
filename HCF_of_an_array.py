n=int(input())
k=list(map(int,input().strip().split()))[:n]
m=min(k)
c=0
for i in range(1,m+1):
    f=True
    for j in k:
       if j%i!=0:
           f=False
           break
    if f==True and i>c:
        c=i
print(c)