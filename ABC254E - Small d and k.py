n, m = map(int, input().split())
import sys
import collections
G = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

# 頂点vから距離eの頂点の番号の和: memo_d[e][v]
memo_d = [[-1]*(n+1) for _ in range(4)]

def bfs(st, k):
    seen = set()
    seen.add(st)
    vx = collections.deque()
    vx.append([st, 0])
    d = st
    step_prev = 0

    while vx:
        v_from, dt = vx.popleft()
        if dt > step_prev:
            memo_d[dt][st] = d
        step_prev = dt

        for v_to in G[v_from]:
            if not v_to in seen:
                seen.add(v_to)
                dt_tmp = dt+1
                d += v_to
                if dt_tmp < k:
                    vx.append([v_to, dt_tmp])  

    return d

q = int(input())
for _ in range(q):
    x, k = map(int, sys.stdin.readline().split())
    if memo_d[k][x] > 0:
        ans = memo_d[k][x]
    elif k==0:
        ans = x
    else:
        ans = bfs(x, k)
        memo_d[k][x] = ans
    print(ans)