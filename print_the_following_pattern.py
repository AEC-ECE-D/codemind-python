n=int(input())
if n>0:
    for i in range(1,n+1):
        a=0
        print(' '*(n-i),end='')
        for k in range(1,2*i):
            if k<i:
                print(i-k,end='')
            else:
                print(a,end='')
                a+=1
        print()