h, w = map(int, input().split())

a_grid = []

import collections
a_column = collections.defaultdict(int)

for _ in range(h):
    a_row = str(input())
    if set(list(a_row)) == set(['.']):
        pass
    else:
        a_grid.append(a_row)

    for j in range(w):
        if a_row[j] == '#':
            a_column[j] += 1

for i in range(len(a_grid)):
    ans_row = ''
    for j in range(w):
        if a_column[j] > 0:
            ans_row += a_grid[i][j]
    print(ans_row)