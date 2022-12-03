n = int(input())
a = list(map(int, input().split()))
import collections
cnt = collections.defaultdict(int)

for i in range(n):
    m = a[i]%200
    cnt[m] += 1

ans = 0
import math
for v in cnt.values():
    if v >= 2:
        x = v-1
        ans += (1+x)*x // 2

print(ans)