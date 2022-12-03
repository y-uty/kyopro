H, W = map(int, input().split())

S = []
for _ in range(H):
    S.append(list(str(input())))

vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]

for i in range(H):
    for j in range(W):
    # 自マスが # のときのみ判定
    # 4近傍に # が1つもない場合、指定の塗り方はできない
        if S[i][j] == '.': continue

        cnt = 0
        for k in range(4):
            cx = j + vx[k]
            cy = i + vy[k]
            if (cx < 0) or (cx >= W): continue
            if (cy < 0) or (cy >= H): continue

            if S[cy][cx] == '#': cnt += 1
        
        if cnt == 0:
            print('No')
            exit()

print('Yes')