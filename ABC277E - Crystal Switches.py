# Dijkstra -> 01BFS に書き換えて再提出
import sys
import collections
import heapq
N, M, K = map(int, input().split())

# 初期のaの値に応じてグラフを2つ(G1, G0)つくり、反転する度に、そのグラフを行き来する
# スイッチのある頂点には、G1とG0をコスト0で結ぶ辺があると考える
G = collections.defaultdict(list)
for _ in range(M):
    u, v, a = map(int, sys.stdin.readline().split())
    x, y = u+N, v+N

    if a:
        G[u].append((1, v))
        G[v].append((1, u))
    else:
        G[x].append((1, y))
        G[y].append((1, x))

S = list(map(int, input().split()))
for i in range(K):
    s = S[i]
    t = s+N
    G[s].append((0, t))
    G[t].append((0, s))


fixed = [False]*(2*N+1)
INF = 10**9
cost = [INF]*(2*N+1)

nx = collections.deque()
nx.append(1)
cost[1] = 0
while nx:
    v_from = nx.popleft()

    if fixed[v_from]: continue
    fixed[v_from] = True

    for c_to, v_to in G[v_from]:

        if cost[v_to] > cost[v_from]+c_to:
            cost[v_to] = cost[v_from]+c_to
            if c_to==0:
                nx.appendleft(v_to)
            else:
                nx.append(v_to)

ans = min(cost[N], cost[2*N])
if ans < INF:
    print(ans)
else:
    print(-1)