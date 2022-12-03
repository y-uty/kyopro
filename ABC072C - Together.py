n = int(input())
a = list(map(int, input().split()))

import collections
a_cnt = collections.defaultdict(int)

for x in a:
    a_cnt[x] += 1
    a_cnt[x-1] += 1
    a_cnt[x+1] += 1

ans = 0
for i in range(1, 10**5+1):
    tmp = a_cnt[i]
    if tmp > ans:
        ans = tmp

print(ans)