N = int(input())
ans = 0
import sys
import collections
sdict = collections.defaultdict(int)

for i in range(N):
    s = ''.join(sorted(list(str(sys.stdin.readline()))))
    sdict[s] += 1
    v = sdict[s]
    if v >= 2:
        ans += v - 1

print(ans)