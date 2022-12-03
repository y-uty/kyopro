N = int(input())
A = list(map(int, input().split()))

from collections import deque
d = deque()
a = deque(A)

lencnt = 0

for _ in range(N):
    anow = a.popleft()

    if lencnt == 0:
        d.append([anow, 1])
        lencnt += 1

    else:
        tmp = d.pop()

        if tmp[0] == anow:
            tmp[1] += 1
            if tmp[1] == anow:
                lencnt += 1 - tmp[1]
            else:
                d.append(tmp)
                lencnt += 1
        else:
            d.append(tmp)
            d.append([anow, 1])
            lencnt += 1

    print(lencnt)