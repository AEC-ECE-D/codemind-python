s=(input())
s.casefold()
m=s.split(' ')
v='aeiou'
c=0
a=100
for i in m:
    for k in i:
        if k in v:
            c+=1
    if c<a and c!=0:
        a=c
    c=0
print(a)