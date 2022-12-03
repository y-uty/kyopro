n, q = map(int, input().split())
a = list(map(int, input().split()))

import itertools
a.sort()
acsum = list(itertools.accumulate(a))

import sys
import bisect
for _ in range(q):
    x = int(sys.stdin.readline())

    idx_l = bisect.bisect_left(a, x)
    idx_r = bisect.bisect_right(a, x)

    if idx_l==0 and idx_r==0:
        print(acsum[-1]-x*n)
        continue
    elif idx_l==n and idx_r==n:
        print(x*n-acsum[-1])
        continue

    ansl, ansr = 0, 0
    if idx_l > 0:
        ansl = abs(acsum[idx_l-1] - x*idx_l)
    else:
        ansl = 0
    
    if idx_r < n:
        ansr = acsum[-1] - acsum[idx_r-1] - x*(n-idx_r)
    else:
        ansr = 0

    print(ansl+ansr)