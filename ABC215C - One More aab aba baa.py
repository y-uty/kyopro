S, K = input().split()
K = int(K)

import itertools

slist = []
schan = itertools.permutations(S)
for s in schan:
    slist.append(s)
slist = set(slist)

print(''.join(sorted(slist)[K-1]))