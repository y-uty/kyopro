N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

import bisect
for i in range(Q):
    x = int(input())
    idx_r = bisect.bisect_left(A, x)
    print(N-idx_r)