n = int(input())
a = list(map(int, input().split()))

import collections
anum = collections.Counter(a)

import math
ans = 0
for v in anum.values():
    if v >= 2:
        ans += math.comb(v, 2)

for i in range(n):
    if anum[a[i]] >= 2:
        print(ans - math.comb(anum[a[i]], 2) + math.comb(anum[a[i]]-1, 2))
    else:
        print(ans)