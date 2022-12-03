n, m = map(int, input().split())
a = list(map(int, input().split()))

import heapq
b = [[-x, x, 0] for x in a]
heapq.heapify(b)

for _ in range(m):
    dcnt = heapq.heappop(b)

    dcnt[0] /= 2
    dcnt[2] += 1

    heapq.heappush(b, dcnt)

b = list(b)
ans = 0
for x in b:
    ans += x[1] // (2**x[2])

print(ans)