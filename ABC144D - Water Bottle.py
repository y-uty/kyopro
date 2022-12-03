import math
a, b, x = map(int, input().split())

# 傾ける角、もしくはその垂直からの差分の角を含む直角三角形において、
# その角の向かいにある辺hを求め、arctan(h)によって角度を求める
if 2*x <= a*a*b:
    # x = 1/2 * b * h * a
    deg = math.degrees(math.atan((2*x)/(a*b*b)))
    print(90-deg)

else:
    # a^2 * b - x = 1/2 * h * a^2
    deg = math.degrees(math.atan(2*(a*a*b-x)/(a**3)))
    print(deg)
