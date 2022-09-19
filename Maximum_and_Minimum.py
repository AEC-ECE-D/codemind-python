from collections import Counter
n=int(input())
a=list(map(int,input().strip().split()))[:n]
arr2=[]
b=Counter(a)
c=0
for i in b:
    if a.count(i)==i:
        arr2.append(i)
if len(arr2)==0:
    print(-1)
else:
    g=max(arr2)
    h=min(arr2)
    print(h,g)