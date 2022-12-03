N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

A.reverse()
C.reverse()

import numpy as np
pa = np.poly1d(A)
pc = np.poly1d(C)
pb = pc / pa

ans = ''
for b in reversed(pb[0].coef):
    ans = ans + str(int(b)) + ' '
 
print(ans.strip())