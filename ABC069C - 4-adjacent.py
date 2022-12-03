N = int(input())
A = list(map(int, input().split()))
import math
mod4 = 0
mod2 = 0

for a in A:
    if a % 4 == 0:
        mod4 += 1
    elif a % 2 == 0:
        mod2 += 1
    else:
        pass

if mod4 >= math.ceil(N // 2):
    print('Yes')
else:
    N -= 2*mod4

    if mod2 == N:
        print('Yes')
    else:
        print('No')