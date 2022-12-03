import sys
import collections
import heapq
n, m = map(int, input().split())
G = collections.defaultdict(list)
used = [False]*(m+1)

# 全頂点支点とした最短経路木を作り一度も使われなかった辺が答え

# どの辺を選んだかも知りたいので辺番号と一緒に格納
for i in range(1, m+1):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((c, b, i))
    G[b].append((c, a, i))

def shortest(st):
    cost = [10**9]*(n+1)
    cost[st] = 0
    fixed = [False]*(n+1)
    fixed[st] = True
    nx = []
    heapq.heappush(nx, (0, st, 0))

    while nx:
        _, v_from, e_from = heapq.heappop(nx)
        # ダイクストラ法では、各頂点が初めてheapqから取り出されたとき、その頂点までの最短コストが確定
        # 逆に、2度目以降は最短経路ではないので、最短経路木の情報としては不要
        if not fixed[v_from]:
            fixed[v_from] = True
            used[e_from] = True

        for c_to, v_to, e_to in G[v_from]:
            if cost[v_to] > cost[v_from]+c_to:
                cost[v_to] = cost[v_from]+c_to
                heapq.heappush(nx, (cost[v_to], v_to, e_to))

# 全頂点始点ダイクストラ
for i in range(1, n+1):
    shortest(i)

print(m-sum(used[1:]))