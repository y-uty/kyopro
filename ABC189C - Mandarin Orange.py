# Stackで、ヒストグラム内の最大面積長方形をO(N)で求める
n = int(input())
a = list(map(int, input().split()))

import collections
S = collections.deque()
L = [0]*n
R = [0]*n

for i in range(n):
    while S:
        j = S.pop()
        if a[j] < a[i]:
            S.append(j)
            break
    if S: L[i] = j+1
    else: L[i] = 0
    S.append(i)

S.clear()
for i in range(n-1, -1, -1):
    while S:
        j = S.pop()
        if a[j] < a[i]:
            S.append(j)
            break
    if S: R[i] = j
    else: R[i] = n
    S.append(i)

ans = 0
for i in range(n):
    ans = max(ans, a[i]*(R[i]-L[i]))

print(ans)