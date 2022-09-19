from collections import Counter
n=int(input())
a=list(map(int,input().strip().split()))[:n]
arr2=[]
b=Counter(a)
c=0
for i in b:
    if a.count(i)==i:
        c+=1
print(c)