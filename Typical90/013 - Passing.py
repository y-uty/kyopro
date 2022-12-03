import sys
import collections
import heapq
n, m = map(int, input().split())
roads = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    roads[a].append([c, b])
    roads[b].append([c, a])

# シンプルな重み付き最短経路はダイクストラで求めれば良い
# ダイクストラの結果は、始点から各点への最小コストとなっている
# 特定の点kを経由するときは、始点(1)からkの最小コストと、kから終点(N)の最小コストの和
# 「1からk」はダイクストラをすればわかるが、
# 「kから終点」は、単純に考えるとあらゆるkを始点にしたダイクストラが必要で、間に合わない

# 無向グラフではk->NとN->kが同じことであり、
# 終点が固定Nなら、Nを始点にしたダイクストラをすれば、N->kが求められる
# その結果、任意のkに対して1->kとk->Nがわかった


INF = 10**10
# 1から出発する各点への最短経路
costs_from_1 = [INF]*(n+1)
costs_from_1[1] = 0
nx = []
heapq.heappush(nx, [0, 1])
while nx:
    _, v_from = heapq.heappop(nx)

    for c_to, v_to in roads[v_from]:
        if costs_from_1[v_to] > costs_from_1[v_from] + c_to:
            costs_from_1[v_to] = costs_from_1[v_from] + c_to
            heapq.heappush(nx, [costs_from_1[v_to], v_to])

# Nから出発する各点への最短経路
costs_from_n = [INF]*(n+1)
costs_from_n[n] = 0
nx = []
heapq.heappush(nx, [0, n])
while nx:
    _, v_from = heapq.heappop(nx)

    for c_to, v_to in roads[v_from]:
        if costs_from_n[v_to] > costs_from_n[v_from] + c_to:
            costs_from_n[v_to] = costs_from_n[v_from] + c_to
            heapq.heappush(nx, [costs_from_n[v_to], v_to])

# 1->k->Nの最短経路コストは、1->k + N->k
for k in range(1, n+1):
    ans = costs_from_1[k]+costs_from_n[k]
    print(ans)