s=(input())
stg=s.split(" ")
for i in range(len(stg)):
    if i%2==0:
        r=stg[i]
        k=r[::-1]
        print(k,end=' ')
    else:
        print(stg[i],end=' ')