n=int(input())
m=list(map(int,input().strip().split()))[:n]
a=[]
b=[]
c=[]
k=0
for i in range(len(m)):
    if m[i]%2==0:
        a.append(m[i])
    else:
        b.append(m[i])
d=min(len(a),len(b))
if len(a)>len(b):
    e=a
else:
    e=b
while k<len(e):
    if k<d:
        c.append(b[k])
        c.append(a[k])
    else:
        c.append(e[k])
    k+=1
if n%2:
    c.append(0)
print(*c)