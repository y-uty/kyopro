import sys
import collections
n, m, q, k = map(int, input().split())
a = list(map(int, input().split()))

roads = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    roads[u].append(v)
    roads[v].append(u)

# ガソリンスタンドの数が少ない(<=20)ことから、Aiから各街への最短距離を求めたあと、
# クエリには max(dist[s][Ai]+dist[t][Ai]) で答えればよい
INF = 10**9
mincost = [[INF]*(n+1) for _ in range(k)]

def shortest_path(i):
    v_stt = a[i]
    nx = collections.deque()
    nx.append(v_stt)
    mincost[i][v_stt] = 0

    while nx:
        v_from = nx.popleft()

        for v_to in roads[v_from]:
            if mincost[i][v_to] < INF:
                continue
            
            mincost[i][v_to] = mincost[i][v_from] + 1
            nx.append(v_to)

## ガソリンスタンドAiからの最短距離計算 ##
for i in range(k):
    shortest_path(i)

## クエリへの回答 ##
for _ in range(q):
    s, t = map(int, sys.stdin.readline().split())

    ans = INF
    for i in range(k):
        tmp = mincost[i][s]+mincost[i][t]
        ans = min(ans, tmp)

    print(ans)
