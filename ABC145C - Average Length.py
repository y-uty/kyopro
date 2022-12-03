N = int(input())
adrs = []
for i in range(N):
    adrs.append(list(map(int, input().split())))

import math
import itertools

p = list(itertools.permutations(list(range(N))))

dist_sum = 0

for j in p: # N! loops
    for k in range(len(j)-1): # (N-1) loops
        dist = math.sqrt((adrs[j[k]][0] - adrs[j[k+1]][0])**2 + (adrs[j[k]][1] - adrs[j[k+1]][1])**2)
        dist_sum += dist

print(dist_sum / len(p))

