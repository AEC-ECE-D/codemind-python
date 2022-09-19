n=int(input())
m=list(map(int,input().split()))
k=int(input())
a=[]
f=False
for i in m:
    if i not in a:
        a.append(i)
        b=m.count(i)
        if b==k:
            f=True
            print(i,end=' ')
if f==False:
    print(-1)