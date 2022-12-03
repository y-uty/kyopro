N = int(input())
import collections
A = list(map(int, input().split()))
A.sort()
A = collections.deque(A)
ans = 0
tmp = 0
cnt = 0

import bisect
l = list(range(N))
for i in l:
    now = A.popleft()
    ans += N - (i + 1)
    if now == tmp:
        cnt += 1
        ans -= cnt
    else:
        cnt = 0
    tmp = now

print(ans)