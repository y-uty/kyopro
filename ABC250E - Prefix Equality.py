import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# (num, min, max, sum) がすべて同じであるか
info_a = []
info_b = []

amin, amax = 10**9, 1
bmin, bmax = 10**9, 1
asum, bsum = 0, 0

aset, bset = set(), set()

for i in range(n):
    ai, bi = a[i], b[i]

    if ai not in aset:
        aset.add(ai)
        amin = min(amin, ai)
        amax = max(amax, ai)
        asum += ai
    info_a.append((len(aset), amin, amax, asum))

    if bi not in bset:
        bset.add(bi)
        bmin = min(bmin, bi)
        bmax = max(bmax, bi)
        bsum += bi  
    info_b.append((len(bset), bmin, bmax, bsum))


q = int(input())
for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1

    if info_a[x]==info_b[y]:
        print('Yes')
    else:
        print('No')
