import sys
import collections
n, q = map(int, input().split())
lists = collections.defaultdict(list)
for i in range(1, n+1):
    li = list(map(int, input().split()))
    lists[i] = li

for _ in range(q):
    s, t = map(int, sys.stdin.readline().split())
    ans = lists[s][t]
    print(ans)
