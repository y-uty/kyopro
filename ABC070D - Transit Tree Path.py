import sys
n = int(input())

import collections
tr = collections.defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tr[a].append([c, b])
    tr[b].append([c, a])

INF = 10**18
import heapq
def dijkstra_method(st):

    costs = [INF]*(n+1)
    costs[st] = 0
    vx = [[0, st]]
    heapq.heapify(vx)

    while vx:
        _, v_from = heapq.heappop(vx)

        for cv in tr[v_from]:
            c_transit, v_to = cv
 
            if costs[v_to] > costs[v_from] + c_transit:
                costs[v_to] = costs[v_from] + c_transit
                heapq.heappush(vx, [costs[v_to], v_to])
    
    return costs

q, k = map(int, sys.stdin.readline().split())
ans = dijkstra_method(k)
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(ans[x] + ans[y])