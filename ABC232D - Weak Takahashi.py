H, W = map(int, input().split())

# グリッドを一次元配列に圧縮して考える
# i*W + j ( i:0~H-1 , j:0~W-1 )
C = []
for i in range(H):
    c = list(input())
    C.extend(c)

dist = [0] * (H*W)
dist[0] = 1
nowdist = 1

from collections import deque
todo = deque()

# BFS的探索により、行けるところまで最短経路で行く
# ただし、今回は各ノードからの行き先は高々2つ（なのでfor文は使わない）
# 次の場所へ辿り着くたびに何個目かを記録していく

# 一歩目、右へ行ければ
if W>2: # 場外でない
    if C[1]=='.': # (1, 2)が壁でない
        todo.appendleft(1)
        nowdist += 1
        dist[1] = nowdist
# 一歩目、下へ行ければ
if H>2: # 場外でない
    if C[W]=='.': # (2, 1)が壁でない
        todo.appendleft(W)
        nowdist += 1
        dist[W] = nowdist

# それ以降の歩み
while len(todo) > 0:
    v = todo.pop()

    # 右へ行ければ
    if v%W < (v+1)%W: # 場外でない＝幅で割ったあまりが増加する（折り返した場合は0に戻る）
        if C[v+1]=='.': # 壁でない
            if dist[v+1] == 0: # 行ったことあるならskip
                todo.appendleft(v+1)
                nowdist += 1
                dist[v+1] = nowdist
    # 下へ行ければ
    if v+W <= H*W-1: # 場外でない＝高さ×幅の大きさを超えない
        if C[v+W]=='.': # 壁でない
            if dist[v+W] == 0: # 行ったことあるならskip
                todo.appendleft(v+W)
                nowdist += 1
                dist[v+W] = nowdist


# 歩いてきた場所で最大値の場所が最終到達点
# その場所を幅で割った商が下への移動距離、余りが右への移動距離となる
g = dist.index(max(dist))
down, right = divmod(g, W)
print(1+right+down)
