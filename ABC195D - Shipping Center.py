import sys
import bisect
import copy
n, m, q = map(int, input().split())
load = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    load.append([v, w])
load.sort(reverse=True) # 価値の高い順

x_given = list(map(int, input().split()))

for _ in range(q):
    ans = 0
    x = copy.deepcopy(x_given)

    l, r = map(int, sys.stdin.readline().split())
    l -= 1
    r -= 1
    boxes_available = [0] + x[:l] + x[r+1:]
    boxes_available.sort()

    for i in range(n):
        v, w = load[i]
        idx = bisect.bisect_left(boxes_available, w)
        if idx < len(boxes_available):
            ans += v
            boxes_available.pop(idx)

    print(ans)