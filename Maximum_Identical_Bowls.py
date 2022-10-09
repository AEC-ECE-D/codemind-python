n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)
while n:
    if a%n==0:
        print(n)
        break
    n-=1