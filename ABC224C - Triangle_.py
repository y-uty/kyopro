N = int(input())
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])

import itertools as itr
comb = itr.combinations(xy, 3)

ans = 0
for tri in comb:

    # if 3 points are on the same line, each slope of 2 lines made by 2 pairs out of 3 points equals.
    # To calculate exactly, (not to be float) use only multiplication. (don't use division)
    if (tri[0][1]-tri[1][1]) * (tri[0][0]-tri[2][0]) == (tri[0][1]-tri[2][1]) * (tri[0][0]-tri[1][0]):
        pass
    else:
        ans += 1

print(ans)
