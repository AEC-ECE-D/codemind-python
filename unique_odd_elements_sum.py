n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=[]
s=0
for i in range(len(m)):
    if m[i] not in a:
        if m[i]%2:
            s=s+m[i]
        a.append(m[i])
print(s)