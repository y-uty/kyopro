n, k = map(int, input().split())
tr = []
ans = 0

for _ in range(n):
    t_tmp = list(map(int, input().split()))
    tr.append(t_tmp)

city = list(range(1, n))

import itertools
rts = itertools.permutations(city)

for r in rts:
    tmp = 0
    fr = 0
    r = list(r) + [0]
    for c in r:
        tmp += tr[fr][c]
        fr = c
    
    if tmp == k:
        ans += 1

print(ans)