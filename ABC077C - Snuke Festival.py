N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

A.sort()
C.sort()

import bisect as bs
saidan = 0

for b in B:
    a_idx = bs.bisect_left(A, b)
    c_idx = bs.bisect_right(C, b)
    saidan += a_idx * (N - c_idx)

print(saidan)
