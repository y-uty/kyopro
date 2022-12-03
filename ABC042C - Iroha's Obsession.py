import bisect
import itertools
n, k = map(int, input().split())
d = set(list(map(int, input().split())))

okd = []
for i in range(10):
    if i not in d:
        okd.append(str(i))

anscand = []
for i in range(1, 6):
    x = list(itertools.product(okd, repeat=i))
    for anstmp in x:
        anscand.append(int(''.join(anstmp)))

print(anscand[bisect.bisect_left(anscand, n)])
