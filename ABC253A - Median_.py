a,b,c = map(int, input().split())
x = [a,b,c]
x.sort()

if x[1]==b:
    print('Yes')
else:
    print('No')
