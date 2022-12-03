import sys
h, w = map(int, input().split())
a = []
sum_row = []
sum_col = [0]*(w)
for _ in range(h):
    a_row = list(map(int, sys.stdin.readline().split()))
    a.append(a_row)
    sum_row.append(sum(a_row))
    for j in range(w):
        sum_col[j] += a_row[j]

b = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        b[i][j] = sum_row[i] + sum_col[j] - a[i][j]

for i in range(h):
    print(*b[i])
