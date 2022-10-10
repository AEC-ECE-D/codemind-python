n=int(input())
p=int(input())
for i in range(1,p+1):
    w,h=map(int,input().split())
    if w==h>=n:
        print('ACCEPTED')
        continue
    else:
        if w<n or h<n:
            print('UPLOAD ANOTHER')
            continue
        else:
            print('CROP IT')