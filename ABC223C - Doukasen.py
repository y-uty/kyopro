N = int(input())

t_burnout = [0]
l_burnout = [0]
v = []

for i in range(N):
    a, b = map(int, input().split())
    t_burnout.append(t_burnout[i] + a/b)
    l_burnout.append(l_burnout[i] + a)
    v.append(b)

coll = t_burnout[-1] / 2

import bisect
idx = bisect.bisect_right(t_burnout, coll)

ans = (coll - t_burnout[idx-1]) * v[idx-1] + l_burnout[idx-1]

print(ans)