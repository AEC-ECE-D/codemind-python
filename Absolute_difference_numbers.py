n,m=map(int,input().split())
s=str(n)
k=len(s)
a=s[:m]
b=s[k-m:k]
z=abs(int(a)-int(b))
print(z)