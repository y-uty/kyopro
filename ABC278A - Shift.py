N, K = map(int, input().split())
A = list(map(int, input().split()))

import collections
A = collections.deque(A)

for i in range(K):
    A.popleft()
    A.append(0)

print(*A)