N, M, X = map(int, input().split())
texts = []
for i in range(N):
    texts.append(list(map(int, input().split())))

import numpy as np

costs = []

# bit exhaustive search
for i in range(2**N):
    ustd = np.zeros(M+1)
    i_bin = format(i, '0'+str(N)+'b')
    for j in range(N):
        if i_bin[j] == '1':
            ustd += texts[j]
    if ustd[1:].min() >= X:
        costs.append(ustd[0])

if len(costs) == 0:
    print(-1)
else:
    print(int(min(costs)))