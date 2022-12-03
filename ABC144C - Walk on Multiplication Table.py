n = int(input())
ans = 10**12

import math
for i in range(1, math.floor(math.sqrt(n))+1):
    if n % i == 0:
        diva = n // i
        tmp = diva + i - 2

        if tmp < ans:
            ans = tmp

print(ans)