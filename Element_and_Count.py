n=int(input())
m=list(map(int,input().strip().split()))[:n]
c=0
m.sort
a=[]

for i in range(n):
    if m[i] not in a:
        a.append(m[i])
for j in a:
    b=m.count(j)
    print(j,b,end=' ')