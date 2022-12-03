N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

import collections
acnt = collections.defaultdict(int)
ccnt = collections.defaultdict(int)
ans = 0

for a in A:
    acnt[a] += 1

for c in C:
    c_replace = B[c-1]
    ccnt[c_replace] += 1

for i in acnt.keys():
    ans += acnt[i] * ccnt[i]

print(ans)
