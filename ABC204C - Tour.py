import sys
n, m = map(int, input().split())
ans = 0

import collections
G = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)

def bfs(rt):
    q = collections.deque()
    seen = [False]*(n+1)
    q.append(rt)
    cnt = 0
    while q:
        nx = q.popleft()
        if seen[nx]: continue

        seen[nx] = True
        cnt += 1
        for v in G[nx]:
            q.append(v)
    
    return cnt

for i in range(1, n+1):
    ans += bfs(i)

print(ans)