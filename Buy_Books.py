n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=0
d=0
for i in range(n):
    s=s+a[i]
for i in range(n):
    d=d+b[i]
if(s>d):
    print("0")
else:
    print(d-s)