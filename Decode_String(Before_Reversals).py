n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    s=(input())
    k=''
    p=s[:b]
    q=s[b:]
    q=q[::-1]
    q=q+p[0]
    for i in range(1,b):
        k=p[::-1]
        q=q+k[0]
        p=k[:b-i]
    print(q[::-1])