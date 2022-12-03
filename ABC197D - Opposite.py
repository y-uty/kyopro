import math
n = int(input())
x0 , y0 = map(int, input().split())
xn_2 , yn_2 = map(int, input().split())

# 2点を結ぶ線分の中点pcの座標
xc, yc = (x0+xn_2)/2, (y0+yn_2)/2

# p0, p1が成す角度θ
rad = math.pi*2/n

# pcを原点と見たときのp0の座標
x0, y0 = x0-xc, y0-yc

# 原点周りにp0をθ回転
x1 = math.cos(rad)*x0 - math.sin(rad)*y0
y1 = math.sin(rad)*x0 + math.cos(rad)*y0

# pcを元の座標に戻す
x1, y1 = x1+xc, y1+yc

# x1, y1を出力
print(x1, y1)
