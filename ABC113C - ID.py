import heapq
import collections
import sys

N, M = map(int, input().split())

pref_year = collections.defaultdict(list)
city_pref = []

for _ in range(M):
    p, y = map(int, sys.stdin.readline().split())
    city_pref.append(p)
    pref_year[p].append(y)

for k in pref_year.keys():
    heapq.heapify(pref_year[k])

for k in pref_year.keys():
    for _ in range(len(pref_year[k])):
        print(heapq.heappop(pref_year[k]))