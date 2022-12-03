import heapq
n, l = map(int, input().split())
a = list(map(int, input().split()))
rest = l-sum(a)
ans = 0

heapq.heapify(a)
if rest > 0:
    heapq.heappush(a, rest)

while True:
    x = heapq.heappop(a)
    if not a:
        break
    y = heapq.heappop(a)

    z = x+y
    ans += z

    heapq.heappush(a, z)

print(ans)