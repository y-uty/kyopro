import sys
import collections
import heapq
n, m = map(int, input().split())
h = [-1] + list(map(int, input().split()))

slopes = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    slopes[u].append(v)
    slopes[v].append(u)

enjoy = [-10**9]*(n+1)
enjoy[1] = 0
hills = []
heapq.heappush(hills, [0, 1])
while hills:
    _, v_from = heapq.heappop(hills)
    tmp = enjoy[v_from]

    for v_to in slopes[v_from]:
        height = h[v_from] - h[v_to]
        if height < 0: height *= 2

        # 同広場2回目以降の到達では、そこまでに得た楽しさが改善するなら、
        # 更新して再探索する
        if tmp+height > enjoy[v_to]:
            enjoy[v_to] = tmp+height
            # 周回数を減らすため、より低い広場を優先的に探索する
            heapq.heappush(hills, [-height, v_to])
        else:
            pass

print(max(enjoy))