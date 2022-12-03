import collections
import sys
N = int(input())
G = collections.defaultdict(list)
visited = collections.defaultdict(int)
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    G[A].append(B)
    G[B].append(A)
    visited[A] = 1
    visited[B] = 1

nx = collections.deque()
nx.append(1)
visited[1] = 0
ans = 0
while nx:
    v_from = nx.popleft()
    ans = max(ans, v_from)
    
    for v_to in G[v_from]:
        if visited[v_to]:
            visited[v_to] = 0
            nx.append(v_to)

print(ans)