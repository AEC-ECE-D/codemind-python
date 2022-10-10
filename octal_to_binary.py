n=int(input())
s=str(n)
k=''
for i in s:
    a=int(i)
    if a>7:
        k=k+'1'
        a=a%7
    if a>=4:
        k=k+'1'
        a=a%4
    else:
        k=k+'0'
    if a>=2:
        k=k+'1'
        a=a%2
    else:
        k=k+'0'
    if a>=1:
        k=k+'1'
        a=a%1
    else:
        k=k+'0'
print(int(k))