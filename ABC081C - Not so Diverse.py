n, k = map(int, input().split())
a = list(map(int, input().split()))

import collections
a_cnt = collections.Counter(a)
a_var = len(a_cnt.keys())

ans = 0
if a_var <= k:
    print(ans)
    exit()

a_cnt = list(a_cnt.values())
a_cnt.sort()
for x in a_cnt:
    ans += x
    a_var -= 1
    if a_var==k: break

print(ans)