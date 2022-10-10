n=int(input())
while n:
    if n%2==0:
        n=n//2
    elif n%3==0:
        n=n//3
    elif n%5==0:
        n=n//5
    elif n==1:
        print('Ugly Number')
        break
    else:
        print('Not Ugly Number')
        break