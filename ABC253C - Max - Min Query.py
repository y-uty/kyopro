q = int(input())

min_ = 10**9+1
max_ = 0

import heapq
minq = []
maxq = []
heapq.heapify(minq)
heapq.heapify(maxq)

import collections
cnt = collections.defaultdict(int)
xset = set()

import sys
for _ in range(q):
    qry = list(map(int, sys.stdin.readline().split()))

    if qry[0]==1:
        x = qry[1]

        if cnt[x]==0:
            heapq.heappush(minq, x)
            heapq.heappush(maxq, -1*x)
        cnt[x] += 1
        xset.add(x)
    
    elif qry[0]==2:
        x = qry[1]
        c = qry[2]

        cnt[x] -= min([c, cnt[x]])
        if cnt[x]==0:
            xset.discard(x)

    else:
        min_ = heapq.heappop(minq)
        max_ = heapq.heappop(maxq)

        while min_ not in xset:
            min_ = heapq.heappop(minq)

        while -1*max_ not in xset:
            max_ = heapq.heappop(maxq)

        ansmax = max_*-1
        print(ansmax - min_)

        heapq.heappush(minq, min_)
        heapq.heappush(maxq, max_)
