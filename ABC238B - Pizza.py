n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict
a_dict = defaultdict(list)

for i in range(360):
    # 新しいkeyの要素をつくりながらappend
    a_dict[i] = 0

asum = 0
for j in range(n):
    asum += a[j]
    acut = asum % 360
    a_dict[acut] = 1

cut = [0]
for k in range(len(a_dict)):
    if a_dict[k] == 1:
        cut.append(k)
cut.append(360)

amax = 0
for l in range(len(cut)-1):
    if cut[l+1] - cut[l] > amax:
        amax = cut[l+1] - cut[l]

print(amax)