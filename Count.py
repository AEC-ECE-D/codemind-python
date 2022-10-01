n=int(input())
l1=list(map(int,input().split()))
a=[]
b=[]
for i in l1:
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(len(a),len(b))