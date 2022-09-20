n=int(input())
m=list(map(int,input().strip().split()))[:n]
if n>1:
    for i in range(1,n//2+1):
        print(m[i-1],m[n-i],end=' ')
    if n%2:
        print(m[i],0)
else:
    print(m[0],0)