n,k = map(int, input().split())
a = list(map(int, input().split()))
aset = set(a)

xy = []
for _ in range(n):
    x, y = map(int , input().split())
    xy.append([x,y])

import math

ans = 0
for i in range(n):
    if i+1 in aset: continue
    tmp = 10**18

    for j in range(k):
        p = a[j]-1

        d = (xy[p][0]-xy[i][0])**2 + (xy[p][1]-xy[i][1])**2

        if d < tmp:
            tmp = d

    if tmp > ans:
        ans = tmp

print(math.sqrt(ans))