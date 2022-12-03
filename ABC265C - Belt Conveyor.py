h, w = map(int, input().split())
grid = []
for _ in range(h):
    g_row = list(str(input()))
    grid.append(g_row)

passed = [[False]*w for _ in range(h)]
passed[0][0] = True

i = 0
j = 0
while True:
    cur = grid[i][j]
    next_i, next_j = i, j
    if cur == 'U':
        next_i -= 1
    elif cur == 'D':
        next_i += 1
    elif cur == 'L':
        next_j -= 1
    else:
        next_j += 1

    if next_i < 0 or next_i >= h or next_j < 0 or next_j >= w:
        break
    else:
        if passed[next_i][next_j]:
            print(-1)
            exit()
        else:
            passed[next_i][next_j] = True
            i, j = next_i, next_j

print(i+1, j+1)
