import sys
n = int(input())

import collections
subm = collections.defaultdict(list)

ans = 0
best = 0
for i in range(1,n+1):
    s, t = map(str, sys.stdin.readline().split())
    t = int(t)

    if len(subm[s])==0:
        subm[s] = [t, i]
    else:
        pass

for v in subm.values():
    if v[0] > best:
        best = v[0]
        ans = v[1]

print(ans)