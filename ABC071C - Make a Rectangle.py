N = int(input())
A = list(map(int, input().split()))

import collections
br = collections.defaultdict(int)
pb = []
for a in A:
    br[a] += 1

for k, v in br.items():
    if v >= 2:
        pb.append([k, v])

pb.sort()

if len(pb) == 0:
    print(0)
elif len(pb) == 1:
    if pb[0][1] >= 4:
        print(pb[0][0]**2)
    else:
        print(0)
else:
    if pb[-1][1] >= 4:
        print(pb[-1][0]**2)
    else:
        print(pb[-1][0]*pb[-2][0])