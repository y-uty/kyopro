n = int(input())
a = list(map(int, input().split()))

import itertools
a_csum = list(itertools.accumulate(a))

ans = 2*(10**9)
for i in range(n-1):
    tmp = abs(a_csum[n-1] - a_csum[i] - a_csum[i])
    if tmp < ans:
        ans = tmp

print(ans)