Q = int(input())
import sys
import collections
c = collections.deque()

for i in range(Q):
    inq = list(map(int, sys.stdin.readline().split()))

    if inq[0] == 1: # append
        c.append([inq[1], inq[2]])
        # print(c)

    else: # popleft
        popnum = inq[1]
        q2sum = 0

        while popnum > 0:
            tmp = c.popleft()
            nownum = tmp[1]

            if popnum < tmp[1]:
                q2sum += popnum * tmp[0]
                tmp[1] -= popnum
                popnum = 0
                c.appendleft(tmp)
                
            else:
                q2sum += tmp[0] * tmp[1]
                popnum -= nownum
            
        print(q2sum)