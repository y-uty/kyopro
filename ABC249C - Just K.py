import itertools
import collections
n, k = map(int, input().split())
strs = []
for _ in range(n):
    strs.append(str(input()))

ans = 0

for i in range(k, n+1):
    strcomb = itertools.combinations(strs, i)

    for st in strcomb:
        strcnt = collections.defaultdict(int)
        # p_rint(strcnt)

        for j in range(i):
            s = st[j]
            for c in s:
                strcnt[c] += 1
        tmp = 0
        
        for ky, v in strcnt.items():
            if v==k:
                tmp += 1
        
        if tmp > ans:
            ans = tmp

print(ans)