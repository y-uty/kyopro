n, m = map(int, input().split())

import sys
import collections
cave = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    cave[a].append(b)
    cave[b].append(a)

steps = [0]*(n+1)
signs = [0]*(n+1)

bfs = collections.deque()
bfs.append(1)
cnt = 0
while bfs:
    f = bfs.popleft()
    cnt += 1  

    for t in cave[f]:
        if steps[t]==0:
            steps[t] = cnt
            signs[t] = f
            bfs.append(t)

print('Yes')
print(*signs[2:], sep='\n')