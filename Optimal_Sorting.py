t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    b=arr.copy()
    b.sort()
    if arr!=b:
        print(b[-1]-b[0])
    else:
        print(0)