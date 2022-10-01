for _ in range(int(input())):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    for j in l2:
        l1.append(j)
    l1.sort()
    print(*l1)