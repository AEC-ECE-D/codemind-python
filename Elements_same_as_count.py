n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=[]
f=False
for i in m:
    if i not in a:
        a.append(i)
        b=m.count(i)
        if b==i:
            print(i,end=' ')
            f=True
if f==False:
    print(-1)