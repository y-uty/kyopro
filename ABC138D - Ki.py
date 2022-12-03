n, q = map(int, input().split())

import collections
tr = collections.defaultdict(list)

import sys
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tr[a].append(b)
    tr[b].append(a)

cnt = [0]*(n+1)
ans = [0]*(n+1)

for _ in range(q):
    p, x = map(int, sys.stdin.readline().split())
    cnt[p] += x

f = 1
cnt_add = 0
ans[1] = cnt[1]

seen = [False]*(n+1)
sys.setrecursionlimit(10**9)
def dfs(from_point, cnt_add):

    seen[from_point] = True
    cnt_add = cnt[from_point]

    for to_point in tr[from_point]:

        if seen[to_point]==False:
            cnt[to_point] += cnt_add
            tmp = cnt_add
            ans[to_point] = cnt[to_point]
            dfs(to_point, cnt_add)
            cnt_add = tmp

dfs(f, cnt_add)

print(*ans[1:])
