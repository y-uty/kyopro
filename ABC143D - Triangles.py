n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0

import bisect
for i in range(n-1):
    for j in range(i+1, n):
        
        idx_r = bisect.bisect_left(l, l[i]+l[j])
        ans += max([idx_r - (j+1), 0])

print(ans)