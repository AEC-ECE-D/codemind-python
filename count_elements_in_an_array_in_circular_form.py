n=int(input())
m=list(map(int,input().split()))
c=0
m=m+m
for i in range(n):
    if (m[i]%2 and m[i+2]%2==0) or (m[i]%2==0 and m[i+2]%2):
        c+=1
print(c)