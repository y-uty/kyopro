# ライブラリの準備
import sys
import numpy as np
lb, ub = -10**4, 10**4

# 入力の受け取りと変数の準備
n, k = map(int, input().split()) # k=100
a = list(map(int, input().split())) # a_d <= 100, thus n <= 100*100=10^4
stb = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    stb.append([x, y])

anslist, anscnt = [], 0 # 出力の格納
# 傾きと切片が既出かどうか
seen_a = [0]*(2*(10**4)+1)
seen_b = [0]*(2*(10**4)+1)

# 処理本体
# step1: 乱数で座標を選んで、ACして正の得点を得る
# step2: 直線を作るたびに、点数がよくなっているかを調べて、悪くなる直線(を引く2点は選ばない)
import math
while k>36:

    # 乱数で2点の座標を得る
    ranlist = np.random.randint(lb, ub, 4)
    px, py = math.floor(ranlist[0]), math.floor(ranlist[1])
    qx, qy = math.floor(ranlist[2]), math.floor(ranlist[3])
    anslist.append([px, py, qx, qy])
    k -= 1

# 疎の部分に直線を引く
x1,x2,x3,x4,x5 = 7500,7700,8000,8500,9000
x6,x7,x8,x9 = 6500, 5000, 3000, 2000
anslist.append([-x1, 0, -x1, 1])
anslist.append([-x2, 0, -x2, 1])
anslist.append([-x3, 0, -x3, 1])
anslist.append([-x4, 0, -x4, 1])
anslist.append([-x5, 0, -x5, 1])
anslist.append([-x6, 0, -x6, 1])
anslist.append([-x7, 0, -x7, 1])
anslist.append([-x8, 0, -x8, 1])
anslist.append([-x9, 0, -x9, 1])

anslist.append([x1, 0, x1, 1])
anslist.append([x2, 0, x2, 1])
anslist.append([x3, 0, x3, 1])
anslist.append([x4, 0, x4, 1])
anslist.append([x5, 0, x5, 1])
anslist.append([x6, 0, x6, 1])
anslist.append([x7, 0, x7, 1])
anslist.append([x8, 0, x8, 1])
anslist.append([x9, 0, x9, 1])

anslist.append([0, -x1, 1, -x1])
anslist.append([0, -x2, 1, -x2])
anslist.append([0, -x3, 1, -x3])
anslist.append([0, -x4, 1, -x4])
anslist.append([0, -x5, 1, -x5])
anslist.append([0, -x6, 1, -x6])
anslist.append([0, -x7, 1, -x7])
anslist.append([0, -x8, 1, -x8])
anslist.append([0, -x9, 1, -x9])

anslist.append([0, x1, 1, x1])
anslist.append([0, x2, 1, x2])
anslist.append([0, x3, 1, x3])
anslist.append([0, x4, 1, x4])
anslist.append([0, x5, 1, x5])
anslist.append([0, x6, 1, x6])
anslist.append([0, x7, 1, x7])
anslist.append([0, x8, 1, x8])
anslist.append([0, x9, 1, x9])

anscnt += 36

# 点数の確認


# 解の出力
anscnt = len(anslist)
print(anscnt)
for ans in anslist:
    print(*ans)

# 確認用: ファイル出力
# pt = './test_out_ahc0121.txt'
# with open(pt, mode='w') as f:
#     f.write(str(anscnt) + '\n')
#     for ans in anslist:
#         s1, s2, s3, s4 = str(ans[0]), str(ans[1]), str(ans[2]), str(ans[3])
#         s = ' '.join([s1, s2, s3, s4]) + '\n'
#         f.write(s)
