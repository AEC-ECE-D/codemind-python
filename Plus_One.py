n=int(input())
a=list(map(int,input().split()))
s=""
for i in a:
    s=s+str(i)
t=int(s)+1
l=[]
while(t>0):
    k=t%10
    l.append(k)
    t=t//10
l.reverse()
for i in l:
    print(i,end=" ")
