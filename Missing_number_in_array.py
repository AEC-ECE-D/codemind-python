for _ in range(int(input())):
    a=int(input())
    n=(a*(a+1))/2
    l1=list(map(int,input().split()))
    print(int(n-sum(l1)))