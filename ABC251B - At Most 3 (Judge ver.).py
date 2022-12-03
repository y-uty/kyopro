n, w = map(int, input().split())
a = list(map(int, input().split()))
ansset = set()

import itertools
for i in range(1, 4):
    c = itertools.combinations(a, i)
    for j in c:
        s = sum(j)
        if s <= w:
            ansset.add(s)

print(len(ansset))