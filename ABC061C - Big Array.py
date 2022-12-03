n, k = map(int, input().split())

import collections
cnt = collections.defaultdict(int)

import sys
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cnt[a] += b

x = sorted(list(cnt.items()))
for d, v in x:
    if k <= v:
        print(d)
        break
    else:
        k -= v