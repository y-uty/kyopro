h, w = map(int, input().split())
maze = []
for _ in range(h):
    s = str(input())
    maze.append(list(s))

## vector - 4-neibor clockwise from above
vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]

ans = [0]*(h*w)

import collections

# 「始点を固定して最短経路でいけるところまで」を全ての座標を始点として繰り返す
for i in range(h*w):
    if maze[i//w][i%w]=='#': continue # 始点が壁の場合スキップ

    nx = collections.deque()
    nx.append(i)
    seen = [-1]*(h*w)
    seen[i] = 0
    # BFSで最短経路におけるstep数を記録していく
    while nx:
        t = nx.popleft()
        x = t%w
        y = t//w

        # 4近傍移動ベクトルを用いて移動可能な座標をサーチ
        for k in range(4):
            cx = x + vx[k]
            cy = y + vy[k]
            if (cx < 0) or (cx >= w): continue # 横にはみでる
            if (cy < 0) or (cy >= h): continue # 縦にはみでる

            if maze[cy][cx] == '.' and seen[cx+cy*w] < 0:
                nx.append(cx+cy*w)
                seen[cx+cy*w] = seen[t]+1

    ans[i] = max(seen)

print(max(ans))