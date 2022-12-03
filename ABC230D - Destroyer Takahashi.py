n, d = map(int, input().split())

import sys
import heapq
walls = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    heapq.heappush(walls, [r, l])

ans = 0

while walls:
    st_r, st_l = heapq.heappop(walls)
    ans += 1

    reachable = st_r + d - 1

    while walls:
        ed_r, ed_l = heapq.heappop(walls)

        if ed_l <= reachable:
            pass
        else:
            heapq.heappush(walls, [ed_r, ed_l])
            break

print(ans)