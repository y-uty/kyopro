n, k = map(int, input().split())
a = list(map(int, input().split()))

import itertools
acsum = list(itertools.accumulate(a))

ans = 0
import bisect
for i in range(n):
    idx = bisect.bisect_left(acsum, k)
    ans += n-idx
    k += a[i]

print(ans)