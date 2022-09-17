def is_prime(n):
    a=n**0.5
    for i in range(2,int(a)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=0
for k in range(n,m+1):
    if k<=1:
        continue
    if is_prime(k):
        c+=1
print(c)