n=int(input())
a=n
if n>=3 and n<=100:
    for i in range(1,n*2):
        if i<=n:
            for j in range(1,i+1):
                print('*',end='')
        else:
            for k in range(1,a):
                print('*',end='')
            a-=1
        print()
else:
    print('The pattern is not possible')