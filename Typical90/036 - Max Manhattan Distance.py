import sys
n, q = map(int, input().split())

# マンハッタン距離は、45度回転することでチェビシェフ距離になる
# ある点からマンハッタン距離が一定の領域は菱形で、45度回転すると正方形になるイメージ
# チェビシェフ距離は Max( x座標の差の絶対値, y座標の差の絶対値 ) 
# よって、45度回転後の座標で、x座標で左or右最も遠い点か、y座標で上or下最も遠い点が
# マンハッタン距離が最大となる2点である

# よって45度回転後の座標はすべてx=左端のx, x=右端のx, y=上端のy, y=下端のyの
# 4直線に囲まれた長方形領域におさまり、
# 任意の点で、上下左右の領域境界までの(ユークリッド)距離4つのうち最大となるものが、
# 最大のマンハッタン距離である

p_rotated = []
x_rotated = []
y_rotated = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_r45 = x-y
    y_r45 = x+y
    p_rotated.append([x_r45, y_r45])
    x_rotated.append(x_r45)
    y_rotated.append(y_r45)

x_rotated.sort()
x_rotated_min = x_rotated[0]
x_rotated_max = x_rotated[-1]

y_rotated.sort()
y_rotated_min = y_rotated[0]
y_rotated_max = y_rotated[-1]

for _ in range(q):
    q = int(sys.stdin.readline())
    q -= 1
    x_rotated_qry, y_rotated_qry = p_rotated[q]
    print(max(  abs(x_rotated_qry-x_rotated_min),
                abs(x_rotated_qry-x_rotated_max),
                abs(y_rotated_qry-y_rotated_min),
                abs(y_rotated_qry-y_rotated_max))
            )
