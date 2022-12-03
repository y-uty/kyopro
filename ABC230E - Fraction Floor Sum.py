n = int(input())

i = 1
ans = 0
while i <= n//2:
    d, m = divmod(n, i)
    ans += d

    x = (n - (i*d))//d
    ans += x*d

    i += x + 1

import math
ans += math.ceil(n/2)

print(ans)