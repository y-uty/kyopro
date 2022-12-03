n, m = map(int, input().split())
cake = [
    list(map(int, input().split())) for _ in range(n)
]

# ある変数の「合計の絶対値」の最大化 -> 合計の最大化(正方向に大きく) or 合計の最小化(負方向に大きく) の
# どちらか2パターンを考えればよく、逆にそれ以外に最適な取り方は存在しない
# つまり、大きい順に取る or 小さい順に取る で合計して絶対値の大きい方を選べばよい

# 変数が複数になっても、それぞれの変数の大小は互いに影響しないので
# 変数ごとに独立に上記の問題を考えればよく、
# 従ってk個の変数で全パターンを試すには、2(合計の大きい順or小さい順) ^ k 通りを調べれば良い

anslist = []
# x, y, zそれぞれを+/-どちらに最大化した合計の絶対値を取るかの8パターン
for i in range(8):
    b = bin(i)[2:].zfill(3)
    cake_sort = []
    # 左からxyz ; 0は+, 1は-とする
    for j in range(n):
        xj, yj, zj = cake[j]

        if b[0]=='1': xj *= -1
        if b[1]=='1': yj *= -1
        if b[2]=='1': zj *= -1

        # パターンに応じて符号を反転させたx+y+zの大きい順にM個選ぶ
        cake_sort.append((xj+yj+zj, xj, yj, zj))
    
    cake_sort.sort(reverse=True)

    xsum, ysum, zsum = 0, 0, 0
    for k in range(m):
        _, xk, yk, zk = cake_sort[k]
        xsum += xk
        ysum += yk
        zsum += zk

    anslist.append(abs(xsum)+abs(ysum)+abs(zsum))

# 8パターンのうちの最大値が答え
print(max(anslist))
