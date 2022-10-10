n=int(input())
c=0
a=[]
f=False
for i in range(1,(n//2)+1):
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        a.append(i)
    c=0
for k in a:
    for m in a:
        if k*m==n:
            s=min(k,m)
            p=max(k,m)
            print(s,p)
            f=True
            break
    if f==True:
        break
if f==False:
    print(-1)