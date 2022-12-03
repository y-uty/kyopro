import sys
import collections
h, w = map(int, input().split())
maze = []
Cx, Cy = map(int, sys.stdin.readline().split())
Dx, Dy = map(int, sys.stdin.readline().split())
v_start = (Cx-1)*w+(Cy-1)
v_end = (Dx-1)*w+(Dy-1)

for _ in range(h):
    s = list(str(sys.stdin.readline()).replace('\n', ''))
    maze.append(s)


# 下記2種類の移動手段があるときは、効率的な実装として01-BFSが有効
#   A. ノーコストの手段で移動する
#   B. 何らかのコストや回数制限のある手段で移動する

# 今回、ワープ魔法の回数を求めたいのだから、
# ワープ魔法にのみコストがかかり、徒歩はノーコストとみなせればよい
# その上で、徒歩で到達できるなら徒歩で、無理ならワープを使うことを考えればよく、
# 結局は最小コストで目的地に向かう探索を行えばよい

# 01-BFSの場合、よりコストが少ない探索を優先するのにheapqは不要で、dequeでよい
# なぜならば1手先のコストの差は高々1(増える: +1 or 変わらない: +0)であり、
# それは0の場合をdequeの先頭、1の場合をdequeの末尾に追加するだけで
# 0の場合を優先的に探索することができるからである


## 4近傍移動ベクトル
vx = [0, 1, 0, -1]
vy = [1, 0, -1, 0]
## 周囲5*5マスへ一度で移動できる
vx2 = [-1, 1, -1,  1] + [ 0,  1,  2,  2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1] 
vy2 = [ 1, 1, -1, -1] + [-2, -2, -2, -1, 0, 1, 2, 2, 2,  2,  2,  1,  0, -1, -2, -2]

INF = h*w
cost = [INF]*(h*w)
visited = [False]*(h*w)

nx = collections.deque()
nx.append(v_start)
cost[v_start] = 0

# 01-BFSで最短経路におけるstep数を記録していく
while nx:
    t = nx.popleft()
    x = t%w
    y = t//w

    # 移動可能な座標をサーチ
    for k in range(4):
        cx = x + vx[k]
        cy = y + vy[k]
        if (cx < 0) or (cx >= w): continue # 横にはみでる
        if (cy < 0) or (cy >= h): continue # 縦にはみでる

        if maze[cy][cx] == '.':
            if cost[cx+cy*w] > cost[t]:
                cost[cx+cy*w] = cost[t]
                nx.appendleft(cx+cy*w) # 0コスト移動は先頭に追加


    # ワープ可能な座標をサーチ
    for k in range(20):
        cx = x + vx2[k]
        cy = y + vy2[k]
        if (cx < 0) or (cx >= w): continue # 横にはみでる
        if (cy < 0) or (cy >= h): continue # 縦にはみでる

        if maze[cy][cx] == '.':
            if cost[cx+cy*w] > cost[t] + 1:
                cost[cx+cy*w] = cost[t] + 1
                nx.append(cx+cy*w) # 1コスト移動は末尾に追加

if cost[v_end]==h*w:
    print(-1)
else:
    print(cost[v_end])
