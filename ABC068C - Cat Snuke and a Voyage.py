import sys
N, M = map(int, input().split())
import collections
routes = collections.defaultdict(list)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    routes[a].append(b)
    routes[b].append(a)

dest1 = routes[1]
for d in dest1:
    dest2 = set(routes[d])
    if N in dest2:
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')