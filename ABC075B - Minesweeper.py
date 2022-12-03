H, W = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(str(input())))

# vector - clockwise from upper left
vx = [-1, 0, 1, -1, 1, -1, 0, 1]
vy = [1, 1, 1, 0, 0, -1, -1, -1]

for i in range(H):
    ans = ''
    for j in range(W):
        cnt_mine = 0
        for k in range(8):
            cx = j + vx[k]
            cy = i + vy[k]
            if (cx < 0) or (cx >= W): continue
            if (cy < 0) or (cy >= H): continue

            if S[cy][cx] == '#': cnt_mine += 1
        
        if S[i][j] == '#':
            ans += '#'
        else:
            ans += str(cnt_mine)

    print(ans)
