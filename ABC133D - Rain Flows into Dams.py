import numpy as np
n = int(input())
a = np.array(list(map(int, input().split())))

ans = []
x1 = 0
for i in range(n):
    if i%2 == 0:
        x1 += a[i]
    else:
        x1 -= a[i]

ans.append(str(x1))

for i in range(n-1):
    x = 2 * a[i] - int(ans[-1])
    ans.append(str(x))

print(' '.join(ans))