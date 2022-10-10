n=int(input())
a=0
b=1
c=0
while True:
    a=b
    b=c
    c=a+b
    if c>n:
        break
d=abs(b-n)
e=abs(c-n)
if d==e:
    print(b,c)
elif d<e:
    print(b)
else:
    print(c)