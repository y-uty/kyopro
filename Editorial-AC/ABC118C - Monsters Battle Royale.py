n = int(input())
a = list(map(int, input().split()))
ans = 0

import math
for i in range(n):
    ans = math.gcd(ans, a[i])

print(ans)