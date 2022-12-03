import sys
n = int(input())
plane = [[0]*(1002) for _ in range(1002)]

# 1次元配列の効率的な区間プロットと言えばいもす法
# 2次元配列(平面上)でも、領域のプロットにいもす法が使える
# 加算する長方形領域の左上内隅+1, 左下の下-1, 右上の右-1, 右下隅の斜め下+1
# その後、左から右に各行累積和→上から下に各列累積和の順で処理すればOK

# この問題では、長方形領域の四隅の座標が与えられることから、
# 左上以外の隅で右や下を考える必要はないことに注意
# たとえば、左上と右上のx座標がx=1, 4のとき、+1したいのは1, 2, 3で、4で-1したいため
# また、2次元座標と2次元配列では「y座標の大きい方から小さい方へ」の向きが逆であることにも注意

# 四隅のプロット
for _ in range(n):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())
    # 左上
    plane[ry][lx] += 1
    # 右上
    plane[ry][rx] -= 1
    # 左下
    plane[ly][lx] -= 1
    # 右下
    plane[ly][rx] += 1


# 累積和
# x座標の小さい方から大きい方へ
for i in range(1002):
    csum = 0
    for j in range(1002):
        plane[i][j] += csum
        csum = plane[i][j]

# y座標の大きい方から小さい方へ
for j in range(1002):
    csum = 0
    for i in range(1001, -1, -1):
        plane[i][j] += csum
        csum = plane[i][j]

# 重なっている枚数のカウント
cnt = [0]*(n+1)
for i in range(1001):
    for j in range(1001):
        cnt[plane[i][j]] += 1

# 答えの出力
print(*cnt[1:], sep='\n')
