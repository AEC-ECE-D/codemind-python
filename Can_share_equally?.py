x,y=map(int,input().split())
if (x+2*y)%2==0:
    a=(x+2*y)//2
    if a%2 and x!=0:
        print('YES')
    elif a%2==0 :
        print('YES')
    else:
        print('NO')
else:
    print('NO')