n=int(input())
a=list(map(int,input().split()))
b=a.copy()
b.sort()
if b[0]!=b[-1]:
    for i in range(len(a)):
        if a[i]==b[-1]:
            if i==n-1:
                print(1)
            else:
                print(2)
            break
else:
    print(0)