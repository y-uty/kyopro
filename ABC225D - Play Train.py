import sys
import collections
n, q = map(int, input().split())

isroot = [-1]*(n+1)
trchain = collections.defaultdict(int)

for _ in range(q):
    qry = list(map(int, sys.stdin.readline().split()))

    x = qry[1]
    if qry[0]==1:
        y = qry[2]
        isroot[y] = x
        trchain[x] = y
    
    elif qry[0]==2:
        y = qry[2]
        isroot[y] = -1
        del trchain[x]

    else:
        ans = collections.deque()
        parent = x
        cnt = 0
        while parent > 0:
            ans.appendleft(parent)
            cnt += 1
            prev_p = parent
            parent = isroot[prev_p]
        
        child = ans.pop()
        cnt -= 1
        while child > 0:
            ans.append(child)
            cnt += 1
            child = trchain[child]
        
        ans.appendleft(cnt)
        
        print(*ans)