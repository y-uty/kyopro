n = int(input())
s = str(input()) + 'X'

import collections
lq = collections.deque()
rq = collections.deque()
wq = collections.deque()
wq.append('0')

for i in range(n):
    nowlr = s[i]
    nextlr = s[i+1]
    if nowlr == nextlr:
        wq.append(str(i+1))
    else:
        if nowlr == 'L':
            rq.extendleft(list(wq))      
        else:
            lq.extend(list(wq))
        wq.clear()
        wq.append(str(i+1))

anslist = list(lq) + list(wq) + list(rq)
ansstr = ' '.join(anslist).strip()
print(ansstr)
