n = int(input())

import collections
yfixed_x = collections.defaultdict(list)

for _ in range(n):
    x, y = map(int, input().split())
    yfixed_x[y].append(x)

y_list = list(yfixed_x.keys())

ans = 0

import itertools
for i in range(len(y_list)):
    if len(yfixed_x[y_list[i]]) < 2:
        continue

    x_comb_y1 = itertools.combinations(yfixed_x[y_list[i]], 2)
    
    for x_pair_y1 in x_comb_y1:
        for j in range(i+1, len(y_list)):
            if len(set(x_pair_y1) & set(yfixed_x[y_list[j]]))==2:
                ans += 1

print(ans)