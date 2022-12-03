x = int(input())

h = [0, 1]
a = 2
while a <= 10**5:
    h.append(h[-1]+a)
    a += 1

import bisect
idx = bisect.bisect_right(h, x)
print(idx)