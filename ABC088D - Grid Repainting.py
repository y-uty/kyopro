import collections
h, w = map(int, input().split())
maze = []
cnt_white = 0
for _ in range(h):
    s = str(input())
    s_list = list(s)
    maze.append(s_list)
    cnt_w_row = collections.Counter(s_list)
    cnt_white += cnt_w_row['.']

## vector - 4-neibor clockwise from above
vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]

nx = collections.deque()
nx.append(0)
seen = [-1]*(h*w)
seen[0] = 0
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

shortest = seen[h*w-1]

if shortest == -1:
    print(-1)
else:
    print(cnt_white-(shortest+1))