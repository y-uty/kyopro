n, k = map(int, input().split())
p = list(map(int, input().split()))

import itertools
p_csum = [0] + list(itertools.accumulate(p))

ans = 0
for i in range(n-k+1):
    tmp = (p_csum[i+k] - p_csum[i] + k) / 2
    if tmp > ans:
        ans = tmp

print(ans)