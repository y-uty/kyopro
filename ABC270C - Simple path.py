import sys
import collections
n, x, y = map(int, input().split())
T = collections.defaultdict(list)
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    T[u].append(v)
    T[v].append(u)

nx = collections.deque()
nx.append(x) # 始点はX
steps = [-1]*(n+1)
steps[x] = 0

while nx:
    v_from = nx.popleft()

    for v_to in T[v_from]:
        if steps[v_to] < 0:
            steps[v_to] = steps[v_from] + 1
            nx.append(v_to)


ans = []
v_from = y
while True:
    ans.append(v_from)

    if v_from==x: break

    for v_to in T[v_from]:
        if steps[v_to]==steps[v_from]-1:
            v_from = v_to
            break

print(*ans[::-1])
