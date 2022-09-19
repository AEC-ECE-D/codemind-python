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
    s=sum(arr2)/len(arr2)
    print("{:.2f}".format(s))