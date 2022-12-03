N, X = map(int, input().split())

import itertools
from collections import deque
d = deque()

cnt = 0
a_list = []

for i in range(N):
    d = deque(list(map(int, input().split())))
    d.popleft()
    a_list.append(list(d))

p = itertools.product(*a_list)

for v in p:
    prod = 1
    for j in v:
        prod = prod*j
    if prod == X:
        cnt += 1

print(cnt)
