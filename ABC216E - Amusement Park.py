n, k = map(int, input().split())
a = list(map(int, input().split()))

import collections
cnt = collections.defaultdict(int)
for i in range(n):
    cnt[a[i]] += 1

ams = collections.deque()
for l, v in sorted(cnt.items(), reverse=True):
    ams.append([l, v])

ans = 0
while k > 0:
    if ams: x = ams.popleft()
    else: break
   
    if ams: y = ams.popleft()
    else:   y = [0, 0]

    if (x[0] - y[0]) * x[1] <= k:
        ans += ((x[0] + y[0]+1)*(x[0] - y[0])//2) * x[1]
        ams.appendleft([y[0], y[1]+x[1]])
        k -= (x[0] - y[0]) * x[1]
    
    else:
        d, m = divmod(k, x[1])
        ans += ((x[0] + x[0]-d+1)*d//2) * x[1]
        ans += (x[0] - d)*m
        k = 0

    if x[0]==0: break
    
print(ans)
