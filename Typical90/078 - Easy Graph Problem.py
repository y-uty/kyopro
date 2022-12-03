import sys
import collections
n, m = map(int, input().split())

G = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for k, vlist in G.items():
    cnt = 0
    for v in vlist:
        if v < k: cnt += 1
    if cnt==1:
        ans += 1

print(ans)