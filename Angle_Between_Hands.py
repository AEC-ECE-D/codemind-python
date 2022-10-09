s=(input())
h=int(s[:2])
m=int(s[3:])
a=abs(30*h-5.5*m)
if a>180:
    a=360-a
print(a)