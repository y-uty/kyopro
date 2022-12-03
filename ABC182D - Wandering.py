n = int(input())
a = list(map(int, input().split()))

import itertools
acsum = list(itertools.accumulate(a))
finished = acsum[-1]

ans = max([0, acsum[0]])
tmp = acsum[0]
fix_csum = max([0, acsum[0]])
for i in range(1, n):

    fix_csum = max([fix_csum, acsum[i]])
    ans = max([tmp+fix_csum, ans])

    tmp += acsum[i]

print(ans)