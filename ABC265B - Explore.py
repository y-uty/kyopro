import sys
import collections
n, m, t = map(int, input().split())
a = list(map(int, input().split()))
bonus = collections.defaultdict(int)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    bonus[x] = y

for i in range(n-1):
    t -= a[i]
    if t <= 0:
        print('No')
        exit()
    
    t += bonus[i+2]

print('Yes')