n = int(input())
import collections
import itertools
cnt_march = collections.defaultdict(int)
inset = set(['M', 'A', 'R', 'C', 'H'])
ans = 0

for _ in range(n):
    s = str(input())
    inis = s[0]
    if inis in inset:
        cnt_march[inis] += 1

cho = itertools.combinations(cnt_march.values(), 3)
for c in cho:
    ans += c[0]*c[1]*c[2]

print(ans)