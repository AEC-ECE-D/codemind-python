n=int(input())
m=list(map(int,input().strip().split()))[:n]
g=[]
h=0
for i in range(len(m)):
    c=abs(m[i])
    a=str(c)
    b=len(a)
    if b>h:
        h=b
for j in range(len(m)):
    c=abs(m[j])
    a=str(c)
    b=len(a)
    if b==h:
        print(m[j],end=' ')