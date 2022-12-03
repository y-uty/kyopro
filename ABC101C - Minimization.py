n, k = map(int, input().split())

import math
if n==k:
    print(1)
else:
    print(math.ceil((n-1)/(k-1)))