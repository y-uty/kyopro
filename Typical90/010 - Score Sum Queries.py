import sys
import itertools
n = int(input())
class1 = [0]*n
class2 = [0]*n

for i in range(n):
    c, p = map(int, sys.stdin.readline().split())
    if c==1:
        class1[i] = p
    else:
        class2[i] = p

c1_csum = [0] + list(itertools.accumulate(class1))
c2_csum = [0] + list(itertools.accumulate(class2))

q = int(input())
for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())

    ans1 = c1_csum[r]-c1_csum[l-1]
    ans2 = c2_csum[r]-c2_csum[l-1]
    print(ans1, ans2)
