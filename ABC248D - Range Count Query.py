import sys
import collections
import bisect
n = int(input())
a = list(map(int ,input().split()))
cnt = collections.defaultdict(list)

for i in range(n):
    a_tmp = a[i]
    cnt[a_tmp].append(i+1)

q = int(input())

for _ in range(q):
    l, r, x = map(int, sys.stdin.readline().split())

    l_idx = bisect.bisect_left(cnt[x], l)
    r_idx = bisect.bisect_right(cnt[x], r)
    print(r_idx - l_idx)