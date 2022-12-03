import sys
import heapq
import collections
n, m = map(int, input().split())
arb = []
arb_bak = []
arb_dict = collections.defaultdict(list)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arb_dict[a].append(b)

ans = 0
for i in range(1, m+1):

    if len(arb_dict[i])>0:
        for b in arb_dict[i]:
            heapq.heappush(arb, [-b, i])

    while arb:
        reward, due = heapq.heappop(arb)
        if due <= i:
            ans += -reward
            break
        else:
            heapq.heappush(arb_bak, [reward, due])
        
    while arb_bak:
        bak = heapq.heappop(arb_bak)
        heapq.heappush(arb, bak)

print(ans)