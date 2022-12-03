a, b = map(int, input().split())

if abs(a-b)==1:
    print('Yes')
else:
    if (a==1 and b==10) or (a==10 and b==1):
        print('Yes')
    else:
        print('No')