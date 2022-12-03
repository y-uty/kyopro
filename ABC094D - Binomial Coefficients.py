
n = int(input())
a = sorted(list(map(int, input().split())))

l = a[-1]
r = [0, 0]
for i in range(n-1):
    if a[i] < l-a[i]:
        tmp = [a[i], 0]
    else:
        tmp = [l-a[i], 1]
    
    if tmp[0] > r[0]:
        r = tmp

if r[1]==0:
    print(l, r[0])
else:
    print(l, l-r[0])
