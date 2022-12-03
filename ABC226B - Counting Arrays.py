N = int(input())

import collections
arr = set()
ans = 0

for i in range(N):

    A = collections.deque(list(map(int, input().split())))
    L = A.popleft()
    A = str(A)

    if A in arr:
        pass
    else:
        arr.add(A)
        ans += 1

print(ans)