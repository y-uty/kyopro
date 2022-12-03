import sys
import itertools
n = int(input())
itvl = [0]*(200001)

for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    itvl[l] += 1
    itvl[r] -= 1

csum = list(itertools.accumulate(itvl))
ans = []
al = False
for i in range(1, 200001):
    if not al and csum[i] > 0:
        ansl = i
        al = True

    if al and csum[i] == 0:
        ansr = i
        ans.append([ansl, ansr])
        al = False

for ax in ans:
    print(*ax)