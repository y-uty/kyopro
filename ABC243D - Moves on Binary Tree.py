n, x = map(int, input().split())
s = str(input())

import collections
moveq = collections.deque()
moveq.append(s[0])

to_child = set(['L', 'R'])

# LorR > U の動きはトレース不要なので相殺する
for i in range(1, n):
    nx = s[i]

    if moveq:
        pv = moveq.pop()

        if pv in to_child and nx == 'U':
            pass
        else:
            moveq.append(pv)
            moveq.append(nx)
    
    else:
        moveq.append(nx)

while moveq:
    m = moveq.popleft()

    if m=='L':
        x += x
    elif m=='R':
        x += x+1
    else:
        x //= 2

print(x)