n = int(input())
a = list(map(int, input().split()))

q = int(input())
import collections
d = collections.defaultdict(int)
for i in range(n):
    d[a[i]] += 1

ans = 0
for k, v in d.items():
    ans += k*v

import sys
for _ in range(q):
    b, c = map(int, sys.stdin.readline().split())
    if d[b] > 0:
        num = d[b]
        d[c] += num
        d[b] -= num
        ans += (c-b) * num
    print(ans)