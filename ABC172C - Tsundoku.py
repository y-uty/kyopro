n, m, k = map(int, input().split())
ans = 0

import itertools
import bisect
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_csum = [0] + list(itertools.accumulate(a))
b_csum = list(itertools.accumulate(b))

# aだけから読む時の最大数+1を調べる
a_max = bisect.bisect_right(a_csum, k)

# aから1冊も読めないときは、bだけを考える
# (この後のa_csumに対するループが空振るため)
if a_max == 1:
    b_max = bisect.bisect_right(b_csum, k)
    print(b_max)
    exit()

for a_num in range(a_max):
    margin = k - a_csum[a_num]
    b_num = bisect.bisect_right(b_csum, margin)
    if a_num + b_num > ans:
        ans = a_num + b_num

print(ans)