import sys
n, m, q = map(int, input().split())

# 列車が走る区間[Li, Ri]を、L-R平面座標上にプロットする
# 二次元累積和を取ると、任意の長方形領域内(境界含む)にプロットされた点の個数がわかる

LRplane = [[0]*(n+2) for _ in range(n+2)] # 0~N+1までのN+2個の座標

# [L, R]のプロット
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())

    LRplane[l][r] += 1

# 累積和を取る
for i in range(1, n+2):
    for j in range(1, n+2):
        LRplane[i][j] += LRplane[i][j-1]

for j in range(1, n+2):
    for i in range(1, n+2):
        LRplane[i][j] += LRplane[i-1][j]

# クエリに答える
for _ in range(q):
    pi, qi = map(int, sys.stdin.readline().split())

    ans = LRplane[qi][qi]-LRplane[pi-1][qi]-LRplane[qi][pi-1]+LRplane[qi-1][pi-1]
    print(ans)
