import sys
import math
t = int(input())
l, X, Y = map(int, input().split())
r = l/2

q = int(input())
for _ in range(q):
    e = int(sys.stdin.readline())

    # 観覧車の回転角度
    theta = 2 * math.pi * e / t

    # E869120君のy, z座標
    if e <= t/4:
        y, z = -r*math.sin(theta), -r*math.cos(theta)+r
    elif e <= t/2:
        theta = theta - math.pi/2
        y, z = -r*math.cos(theta), r*math.sin(theta)+r
    elif e <= 3*t/4:
        theta = theta - math.pi
        y, z = r*math.sin(theta), r*math.cos(theta)+r
    else:
        theta = theta - 3*math.pi/2
        y, z = r*math.cos(theta), -r*math.sin(theta)+r
    
    # x-y平面上の距離
    dist = math.sqrt(X**2 + (Y-y)**2)

    # x-y平面からの高さ
    height = z

    # 俯角の計算 tanθ = z / √{X^2+(Y-y)^2}
    ans = math.degrees(math.atan(height/dist))
    print(ans)
